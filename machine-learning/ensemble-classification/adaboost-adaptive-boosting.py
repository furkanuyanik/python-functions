def ada_boost(data, y_column):
  X = data.drop(y_column,axis=1)
  y = data[y_column]

  from numpy import mean
  from numpy import std
  from sklearn.model_selection import cross_validate
  from sklearn.model_selection import RepeatedStratifiedKFold
  from sklearn.ensemble import AdaBoostClassifier

  model = AdaBoostClassifier()

  cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    
  scores = cross_validate(model, X, y, scoring=('accuracy',
           'recall',
           'precision',
           'balanced_accuracy',
           'f1',
           'roc_auc'),cv=cv, n_jobs=-1)
  
  return scores