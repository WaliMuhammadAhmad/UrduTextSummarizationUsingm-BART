# Urdu Text Summarization using m-BART

Welcome to the Urdu Text Summarization repository powered by m-BART! ✨

This project is based on a multilingual variant of the BART model, designed to generate concise and coherent summaries for Urdu text. It uses a finetuned m-BART model and offers a Flask-based web application as a simple GUI for interaction.

## About Model

m-BART (Multilingual BART) is an extension of the BART model pretrained on a large-scale multilingual dataset. BART is built for sequence-to-sequence tasks, and m-BART extends this for multilingual applications.  
This model has been trained on ~67,000 Urdu news articles and is optimized specifically for Urdu summarization tasks.

## 🚀 Getting Started

### Model Checkpoints

You can manually download the model [Checkpoints](https://mega.nz/file/dzExhC6J#fsPYKjU0zAYA8J-255f90gbvlzd5XBhtSCwKKWkhQCQ) and place them in a folder named `ckpt` inside the cloned repo.

If not provided or placed incorrectly, the model and tokenizer will automatically be downloaded from Hugging Face Hub and saved locally in the `ckpt` directory.

> ### _Docker Image_
>
> You can run this project using Docker for quick setup and deployment.
>
> 1. **Build the Docker image:**
>
>    ```bash
>    docker build -t urdu-summarizer .
>    ```
>
> 2. **Run the container:**
>    If you have checkpoints locally, can optionally mount your local `ckpt/` dir to avoid downloading model files:
>
>    ```bash
>    docker run -v $(pwd)/ckpt:/app/ckpt -p 5000:5000 urdu-summarizer
>    ```
>
> 3. Visit [`http://localhost:5000`](http://localhost:5000) in your browser.

### Env Setup

**pip**

```bash
pip install -r requirements.txt
```

**conda**

```bash
conda env create -f environment.yaml
conda activate urdu-summarizer
```

### Running Web App

1. Start the app:

```bash
python app.py
```

2. Open your browser and go to `http://localhost:5000`.
3. Paste your Urdu text to get instant summaries.

## Notebooks

The `notebooks` directory contains three Jupyter notebooks. These notebooks can be used to:

- Load and run inference on the model.
- Finetune m-BART on your own Urdu dataset.
- Push the trained model to the Hugging Face Model Hub.

## App GUI Preview

![App Screenshot](./Urdu%20Text%20Summarization%20-%20Google%20Chrome%20Screenshot.png)

## 📬 Contact

For any questions or suggestions, please reach out at [wali.muhammad.ahmad@gmail.com](mailto:wali.muhammad.ahmad@gmail.com).
