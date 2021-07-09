import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

# punkt is a trained model and a tokenizer
# punkt is a tokenizer that divides a text into a list of sentences
nltk.download('punkt')

# in order to get the summarization of article i'm passing the url
url = "https://edition.cnn.com/2021/04/09/tech/elon-musk-neuralink-pong-scli-intl/index.html"

# directing article to url
article = Article(url)
# downloading the article
article.download()
# parsing the article
article.parse()
# calling the nlp method
article.nlp()

print(f'Title of the article: {article.title}')
print(f'Authors of the article: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Article Summary: {article.summary}')

# turning the article into textblob for sentiment analysis
analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.property < 0  else "neutral"}')