import tkinter as tk
import nltk
from nltk import text
from textblob import TextBlob
from newspaper import Article

def summarize():
    # punkt is a trained model and a tokenizer
    # punkt is a tokenizer that divides a text into a list of sentences
    nltk.download('punkt')
    # in order to get the summarization of article i'm passing the url
    # url = "https://edition.cnn.com/2021/04/09/tech/elon-musk-neuralink-pong-scli-intl/index.html"

    # we need to get article from text box
    url = utext.get('1.0', "end").strip()
    article = Article(url)
    # downloading the article
    article.download()
    # parsing the article
    article.parse()
    # calling the nlp method
    article.nlp()

    # print(f'Title of the article: {article.title}')
    # print(f'Authors of the article: {article.authors}')
    # print(f'Publication Date: {article.publish_date}')
    # print(f'Article Summary: {article.summary}')

    # adding content to individual text boxes instead of printing like above
    title.config(state= 'normal')
    author.config(state= 'normal')
    publication.config(state= 'normal')
    summary.config(state= 'normal')
    sentiment.config(state= 'normal')

    # changing the content
    # first deleting everything thats in there
    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    # performing sentiment analysis
    # turning the article into textblob for sentiment analysis
    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.property < 0  else "neutral"}')

    # when after done with them, we should disable them again. so that user cannot change
    title.config(state= 'disabled')
    author.config(state= 'disabled')
    publication.config(state= 'disabled')
    summary.config(state= 'disabled')
    sentiment.config(state= 'disabled')

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
sentiment = tk.Text(root, height= 1, width= 140)
sentiment.config(state='disabled', background= '#dddddd')
sentiment.pack()

# URL title
ulabel = tk.Label(root, text = 'URL')
ulabel.pack()
# adding box for URL
utext = tk.Text(root, height= 1, width= 140)
utext.pack()

# adding button
btn = tk.Button(root, text="Summarize", command = summarize)
btn.pack()

root.mainloop() # mainloop method is used when we want to execute when we want to run our app
