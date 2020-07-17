from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

def feature_importance(data):
  X = data.iloc[:, 0:len(data.columns)]  
  y = data.iloc[:, -1]    

  model = RandomForestClassifier()
  model.fit(X,y)

  feat_importances = pd.Series(model.feature_importances_, index=X.columns)
  feat_importances.nlargest(100).plot(kind='bar')

  plt.show()