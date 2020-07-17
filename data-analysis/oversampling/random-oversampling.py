from imblearn.over_sampling import RandomOverSampler
from collections import Counter

def random_oversampling(data, y_column):
  X = data.drop(y_column, axis = 1)
  y = data[y_column]

  print(Counter(y))

  oversample = RandomOverSampler(sampling_strategy='minority')
  X_res, y_res = oversample.fit_resample(X, y)
  
  print(Counter(y_res))

  data = pd.DataFrame(X_res, columns = df.drop(y_column, axis=1).columns.tolist()) 
  data[y_column] = y_res

  return data