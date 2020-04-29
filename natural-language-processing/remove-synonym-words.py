import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import PorterStemmer 
nltk.download('punkt')
nltk.download('wordnet')

def tokenize_of_words(text):
  return word_tokenize(text.lower());

def remove_synonym_words(text):
  temp = []
  for word in tokenize_of_words(text.lower()):
    for synset in wordnet.synsets(word):
      for lemma in synset.lemma_names():
          if lemma.lower() != word and lemma.find("_") == -1 and not lemma in temp and text.find(' ' + lemma + ' ') != -1:
            print(word, lemma)
            text = text.replace(' ' + lemma + ' ', ' ')
            temp.append(lemma)
            temp.append(word)
  return text

print(remove_synonym_words("I am computer engineering and computer equals a calculator."))