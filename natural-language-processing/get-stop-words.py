import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def get_stop_words():
  return set(stopwords.words('english'))

print(get_stop_words())