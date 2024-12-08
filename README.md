# Flask Grammar Corrector

A simple web application built with Flask that corrects grammatical and spelling errors in a text or file provided by the user. The app uses **Gramformer** for grammar correction and **TextBlob** for spelling corrections, with a frontend built using HTML and CSS.

---

## Features

- **Grammar Correction**: Powered by Gramformer, it corrects grammatical issues in the input text.
- **Spelling Correction**: Uses TextBlob to identify and correct spelling errors.
- **File Support**: Allows users to upload text files for error correction.

---

## Technology Stack

### Backend
- **Flask**: Python-based web framework for building the application.
- **Gramformer**: For grammar correction.
- **TextBlob**: For spelling corrections.

### Frontend
- **HTML**: Structure of the web pages.
- **CSS**: Styling of the web pages.

---

## Prerequisites

To run this application, ensure you have the following installed:

1. **Python 3.7 or higher**
2. **Pip**: Python package installer
3. Required Python libraries (detailed below)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/flask-grammar-corrector.git
cd flask-grammar-corrector
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Install the required libraries using pip:
```bash
pip install -r requirements.txt
```

### 4. Required Libraries
Include the following in your `requirements.txt` file:
```text
flask
textblob
transformers
sentencepiece
torch
```

- **Flask**: Web framework
- **TextBlob**: For spelling corrections
- **Transformers**: Required by Gramformer
- **SentencePiece**: Tokenizer dependency for Gramformer
- **Torch**: PyTorch library for Gramformer

### 5. Download Gramformer Models
Gramformer requires specific models for grammar correction. Include the following in your code setup:
```python
from gramformer import Gramformer

gf = Gramformer(models=1)  # 1 for correcting grammar
```
Ensure that the necessary models are downloaded when you run the app.

### 6. Run the Application
Start the Flask development server:
```bash
python app.py
```
Visit the app at `http://127.0.0.1:5000/` in your browser.

---

## Usage

1. Enter or paste text in the input field.
2. Upload a `.txt` file for processing (optional).
3. Click on "Correct Text".
4. View and download corrected text.

---

## Documentation and References

- [Flask Documentation](https://flask.palletsprojects.com/en/latest/)
- [Gramformer GitHub](https://github.com/PrithivirajDamodaran/Gramformer)
- [TextBlob Documentation](https://textblob.readthedocs.io/en/dev/)
- [Transformers Documentation](https://huggingface.co/docs/transformers/)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)

---

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. For major changes, please discuss them first by opening an issue.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
