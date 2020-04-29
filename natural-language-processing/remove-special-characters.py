import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer 
nltk.download('punkt')

def tokenize_of_words(text):
  return word_tokenize(text.lower());

def remove_special_characters(text):
  temp = list(text) 
  for x in range(len(text)):
    if text[x] != ' ' and (text[x].isalnum() == False or text[x].isdigit() == True):
        temp[x] = ''

  return "".join(temp)

print(remove_special_characters("I am 100% Computer Engineering. I am writing somethings."))