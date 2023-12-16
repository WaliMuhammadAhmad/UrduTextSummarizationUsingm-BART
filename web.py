# web.py

from flask import Flask, render_template, request
from transformers import AutoTokenizer, MBartForConditionalGeneration, pipeline

app = Flask(__name__)

model_ckpt = "finetunedmBartLarge67kWith50news147Scripts"
tokenizer = AutoTokenizer.from_pretrained(model_ckpt)
model = MBartForConditionalGeneration.from_pretrained(model_ckpt)

def process_text(input_text):
    size = tokenizer(input_text, return_tensors="tf")["input_ids"].shape[1]
    generator = pipeline('text2text-generation', model=model, tokenizer=tokenizer, do_sample=False)
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

if __name__ == '__main__':
    app.run(debug=True)
