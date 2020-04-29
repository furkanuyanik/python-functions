import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')

def tokenize_of_words(text):
  return word_tokenize(text.lower());

def get_frequency_word(text, word):
  words = tokenize_of_words(text)
  freqDist = nltk.FreqDist(w.lower() for w in words)
  return freqDist[word]

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur non ipsum leo. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
freq = get_frequency_word(text, "lorem")

print(freq)