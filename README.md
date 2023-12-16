# Urdu Text Summarization using m-BART

Welcome to the Urdu Text Summarization repository powered by m-BART! ✨

This project focuses on leveraging the power of m-BART, a multilingual variant of the BART model, to generate concise and coherent summaries for Urdu text. Whether you're interested in exploring the pretrained model or using it for your Urdu text summarization tasks, we've got you covered.


## About m-BART:

m-BART (Multilingual BART) is an extension of the BART model pretrained on a large-scale multilingual dataset. BART itself is designed for sequence-to-sequence tasks, and m-BART inherits these capabilities with a focus on multilingual applications. This repository uses m-BART for the task of Urdu text summarization.


## Urdu Text Summarization Model repo:

This repository contains:

- **Checkpoints:** Pretrained model checkpoints for Urdu text summarization.
- **Notebook:** Jupyter notebook used for experimenting with m-BART.
- **Web App:** A Flask web application for easy text summarization. Run the app locally and get summaries in a snap.


## Project Structure:

Urdu-Text-Summarization/
│
├── Checkpoints/
│ ├── finetunedmBartLarge67kWith50news147Scripts
│     ├── ...
│
├── Notebook/
│ ├── notebook4summarization.ipynb
│
├── requirements.txt
|
├── Flask App/
│ ├── templates/
│ │ ├── index.html
| | ├── favicon.ico
│ ├── web.py
│


## 🚀 Getting Started

### Model Checkpoints:

1. Download the model [Checkpoints](https://mega.nz/file/dzExhC6J#fsPYKjU0zAYA8J-255f90gbvlzd5XBhtSCwKKWkhQCQ).
2. Unzip the checkpoints.
3. Place it in the cloned directory -or- add its path in the web.py

### Requirements:

1. You can find all the required libraries to run the model in the requirements.txt.
2. 
```bash
pip install -r requirements.txt
```

### Running Web App:

1. Run `python web.py` in the terminal to start the Flask application.
3. Open your browser and visit `http://localhost:5000`.
4. Paste your Urdu text and get instant summaries!


## Training Details:

The model has been trained on a diverse dataset consisting of approximately 67,000 Urdu news articles. Please note that the model is tailored for Urdu language-specific summarization tasks.


## 📬 Contact:

For any questions or suggestions, please reach out at [wali.muhammad.ahmad@gmail.com.com].
