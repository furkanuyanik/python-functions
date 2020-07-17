def pearson_correlation(data, y_column, rate):  
  import seaborn as sns
  import matplotlib.pyplot as plt
  
  plt.figure(figsize=(32,30))
  cor = data.corr()
  sns.heatmap(cor, annot=True, cmap=plt.cm.Reds)
  plt.show()

  cor_target = abs(cor[y_column])
  
  relevant_features = cor_target[cor_target > rate]

  print(relevant_features)

  return relevant_features