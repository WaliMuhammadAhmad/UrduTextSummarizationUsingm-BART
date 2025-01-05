import os
import torch
from flask import Flask, render_template, request
from transformers import AutoTokenizer, MBartForConditionalGeneration, pipeline

app = Flask(__name__)

model_ckpt = "ckpt" # local dir
hf_model_id = "iHateNLP/MBart-Urdu-Text-Summarization"

def model_files_exist(directory):
    required_files = ['config.json', 'generation_config.json', 'pytorch_model.bin', 'sentencepiece.bpe.model', 'special_tokens_map.json', 'tokenizer.json', 'tokenizer_config.json', 'training_args.bin']
    return all(os.path.exists(os.path.join(directory, f)) for f in required_files)

# Check if local model files exist
if os.path.exists(model_ckpt) and model_files_exist(model_ckpt):
    print("Loading model and tokenizer from local checkpoint...")
    tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
    model = MBartForConditionalGeneration.from_pretrained(model_ckpt)
else:
    print("Local checkpoint not found. Downloading model and tokenizer from Hugging Face Hub...")
    tokenizer = AutoTokenizer.from_pretrained(hf_model_id)
    model = MBartForConditionalGeneration.from_pretrained(hf_model_id)

    os.makedirs(model_ckpt, exist_ok=True)
    tokenizer.save_pretrained(model_ckpt)
    model.save_pretrained(model_ckpt)
    print(f"Model and tokenizer saved to local checkpoint: {model_ckpt}")


def process_text(input_text):
    size = tokenizer(input_text, return_tensors="pt")["input_ids"].shape[1]
    generator = pipeline('text2text-generation', model=model, tokenizer=tokenizer, do_sample=False, device="cuda"if torch.cuda.is_available() else "cpu")
    result = generator(input_text, max_length=size + 100)
    return result[0]['generated_text']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_text = request.form['inputText']
    processed_text = process_text('Text: ' + input_text)
    return render_template('index.html', input_text=input_text, output_text=processed_text)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
