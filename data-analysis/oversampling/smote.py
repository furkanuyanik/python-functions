from collections import Counter
from imblearn.over_sampling import SMOTE

def smote(data, y_column):
  X = data.drop(y_column, axis = 1)
  y = data[y_column]
  print('Original dataset shape %s' % Counter(y))

  sm = SMOTE(random_state=42)
  X_res, y_res = sm.fit_resample(X, y)
  print('Resampled dataset shape %s' % Counter(y_res))

  data = pd.DataFrame(X_res, columns = df.drop(y_column, axis=1).columns.tolist()) 
  data[y_column] = y_res

  return data