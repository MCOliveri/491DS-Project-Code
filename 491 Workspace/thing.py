import nltk
nltk.download("book")
from nltk.book import *

text3.concordance("renown")

from nltk.tokenize import word_tokenize

sentence = "ghty men which were of old , men of renown . And God saw that the wickedness o"
tokens = word_tokenize(sentence)
print(tokens)