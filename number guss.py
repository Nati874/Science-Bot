import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize
from nltk.corpus import stopwords



stop=set(stopwords.words('english'))
x='|2+3*4|'
print(word_tokenize(x))
