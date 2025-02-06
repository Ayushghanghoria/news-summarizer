# News Summarizer

A simple web application that extracts and summarizes news articles using Flask and the Transformers library.

## Description

The News Summarizer application allows users to input a URL of a news article, extracts the text from the article, and provides a concise summary. It utilizes the `newspaper` library for article extraction and a pre-trained summarization model from Hugging Face's Transformers library.

## Features

- Extracts text from news articles using a URL.
- Summarizes the extracted text using a state-of-the-art NLP model.
- User-friendly web interface built with Flask.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Ayushghanghoria/news-summarizer.git
   cd news-summarizer
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter the URL of a news article in the input field and submit the form to see the extracted text and its summary.

## Dependencies

- Flask
- newspaper3k
- transformers

Make sure to install the required dependencies listed in `requirements.txt`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - The web framework used.
- [newspaper3k](https://newspaper.readthedocs.io/en/latest/) - For article extraction.
- [Transformers](https://huggingface.co/transformers/) - For text summarization.
