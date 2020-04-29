import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

def tokenize_of_words(text):
  return word_tokenize(text.lower());

def remove_duplicated_words(text):
  temp = []
  [temp.append(' ' + w + ' ') for w in tokenize_of_words(text) if (' ' + w + ' ') not in temp]
  return " ".join(tokenize_of_words("".join(temp)))

print(remove_duplicated_words("I am Furkan Uyanik. I am Furkan Uyanik."))