# GRAD-E1282: Natural Language Processing
# Instructor: Dr. Sascha Göbel

## Term paper - Nicolas Reichardt, 245611

---

## NLP-Driven Analysis of AI Regulation: Comparing the EU AI Act and U.S. AI Executive Order

## Abstract
This project explores the themes and topics surrounding AI regulation in Europe and the USA using Natural Language Processing (NLP) techniques. Through text extraction, cleaning, tokenization, and feature extraction, the project aims to uncover insights from the two main legal documents: (1) the EU AI Act and (2) the American AI Executive Order . The analysis is conducted as part of my NLP class at the Hertie School taught by Dr. Sascha Göbel.

For more information and results, see the accompanying [paper](NLP_Research_Note_Reichardt.pdf).

---

## Repository Structure
```
nlp-research-note/
├── data/
│   ├── raw/                     # Raw PDF files
│   ├── extracted_text/          # Extracted text from PDFs
│   ├── cleaned_text/            # Cleaned text files
│   ├── tokens/                  # Tokenized text files
│   ├── embeddings/              # Word2Vec embeddings
├── notebooks/
│   ├── NLP_pipeline.ipynb       # Main Jupyter notebook for the pipeline
├── utils/
│   ├── extract_pdf_contents.py  # PDF text extraction utility
│   ├── clean_texts.py           # Text cleaning utility
│   ├── BoW_model.py             # Bag-of-Words 
│   ├── word_frequency.py        # Frequency distribution
│   ├── word2vec_module.py       # Word2Vec model 
│   ├── tsne_visualization.py    # t-SNE visualization 
├── plots/                       
├── requirements.txt
├── NLP_Research_Note_Reichardt.pdf            
├── README.md                    
```

---

## Installation and Setup

### Prerequisites
- Python 3.10 or higher

### Clone the Repository
```bash
git clone https://github.com/your-username/nlp-research-note.git
cd nlp-research-note
```

### Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Download Pretrained Word2Vec Model

The Word2Vec model is too large to include in the repository. Download it using:

```python
import gensim.downloader as api
model = api.load("word2vec-google-news-300")
```
---

## Usage

### Run the Jupyter Notebook
1. Start Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
2. Open `notebooks/NLP_pipeline.ipynb` and run the cells step by step.

---

## Features
- **Text Extraction**: Extracts text from legal PDF documents.
- **Text Cleaning**: Cleans and preprocesses the extracted text.
- **Tokenization**: Tokenizes the cleaned text using SpaCy.
- **Feature Extraction**: Computes Bag of Words (BoW) and Word2Vec embeddings.
- **Visualization**: Generates t-SNE plots for Word2Vec embeddings.
- **Mathematical Analysis**: Measures similarity and performs dimensionality reduction.

---

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## AI use statement:

Generative AI tools like GitHub Copilot and Claude were consulted for writing support, LaTeX formatting, and general coding/linting support. All final answers were developed and verified by the author.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.