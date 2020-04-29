import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
nltk.download('punkt')

def tokenize_of_words(text):
  return word_tokenize(text.lower());

def get_stemming_words(text):
  temp = [];
  porter_stemmer = PorterStemmer() 
  for w in tokenize_of_words(text): 
    temp.append(porter_stemmer.stem(w));
  return " ".join(temp)

print(get_stemming_words("I am developer. I am writing something."))