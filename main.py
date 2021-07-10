import tkinter as tk
import nltk
from nltk import text
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

# creating gui part
root = tk.Tk()
root.title('News Summarizer')
root.geometry('1200x600')

# title part
tlabel = tk.Label(root, text="Title")
tlabel.pack()

# adding box for the title
title = tk.Text(root, height = 1, width = 140)
title.config(state='disabled', bg = '#dddddd') # light gray
title.pack()

# author title
alabel = tk.Label(root, text="Author")
alabel.pack()
# adding box for author
author = tk.Text(root, height = 1, width = 140)
author.config(state='disabled', bg = '#dddddd') # light gray
author.pack()

# publication title
plabel = tk.Label(root, text="Publishing Date")
plabel.pack()
# adding box for the publication
publication = tk.Text(root, height = 1, width = 140)
publication.config(state='disabled', bg = '#dddddd') # light gray
publication.pack()

# summary title
slabel = tk.Label(root, text = "Summary")
slabel.pack()
# adding box for Summary
summary = tk.Text(root, height= 20, width = 140)
summary.config(state= 'disabled', bg = '#dddddd')
summary.pack()

# sentiment analysis title
selabel = tk.Label(root, text = 'Sentiment Analysis')
selabel.pack()
# adding box for Sentiment analysis
sentiment = tk.Text(root, height= 1, width= 240)
sentiment.config(state='disabled', background= '#dddddd')
selabel.pack()

# URL title
ulabel = tk.Label(root, title = 'URL')
ulabel.pack()
# adding box for URL
url = tk.Text(root, height= 1, width= 140)
url.pack()

root.mainloop()