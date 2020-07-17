def light_gbm(data, y_column):
  from numpy import mean
  from numpy import std
  from lightgbm import LGBMClassifier
  from sklearn.model_selection import cross_validate
  from sklearn.metrics import make_scorer
  from sklearn.model_selection import RepeatedStratifiedKFold
  from matplotlib import pyplot

  X = data.drop(y_column,axis=1)
  y = data[y_column]

  model = LGBMClassifier()

  cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
  
  scores = cross_validate(model, X, y, scoring=('accuracy',
           'recall',
           'precision',
           'balanced_accuracy',
           'f1',
           'roc_auc'),cv=cv, n_jobs=-1)
  
  return scores
