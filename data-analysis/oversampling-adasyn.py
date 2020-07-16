from imblearn.over_sampling import ADASYN
from collections import Counter

def ADASYN(data, y_column):
  X = data.drop(y_column, axis = 1)
  y = data[y_column]

  print("Old records count: ", Counter(y))

  ada = ADASYN(sampling_strategy='minority', random_state=420, n_neighbors=5)
  X_res, y_res = ada.fit_resample(X, y)
  
  print("New recods count: ", Counter(y_res))

  data = pd.DataFrame(X_res, columns = df.drop(y_column, axis=1).columns.tolist()) 
  data[y_column] = y_res

  return data