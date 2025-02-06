from flask import Flask, render_template, request
from newspaper import Article
from transformers import pipeline

app = Flask(__name__)

# Load summarization model
summarizer = pipeline("summarization")

def extract_text(url):
    """Extract text from a news article"""
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def summarize_text(text):
    """Summarize the extracted text"""
    min_length, max_length = len(text)//10, len(text)//5
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        try:
            article_text = extract_text(url)
            summary = summarize_text(article_text)
            return render_template("index.html", article_text=article_text, summary=summary)
        except Exception as e:
            return render_template("index.html", error=str(e))
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
