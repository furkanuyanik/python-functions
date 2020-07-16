def set_min_max_normalization(data):
  for column in data.columns.tolist():
    v = data[column]   
    data[column] = (v - v.min()) / (v.max() - v.min())
    return data