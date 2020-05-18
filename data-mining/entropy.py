from scipy.stats import entropy

def find_entropy(data):
  for column in data.columns.tolist():
    print(column, ": ", entropy(data[column]))
