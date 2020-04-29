import nltk
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
nltk.download('punkt')

def tokenize_of_words(text):
  return word_tokenize(text.lower());
  
def tokenize_of_sentences(text):
  return sent_tokenize(text.lower());

print(tokenize_of_words("I am Furkan Uyanik."))
print(tokenize_of_sentences("I am Furkan Uyanik. I am Computer Engineering."))