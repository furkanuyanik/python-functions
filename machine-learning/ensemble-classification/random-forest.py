def random_forest(data, y_column):
  from numpy import mean
  from sklearn.model_selection import cross_validate
  from sklearn.model_selection import RepeatedStratifiedKFold
  from imblearn.ensemble import BalancedBaggingClassifier
  
  # generate dataset
  X = data.drop(y_column, axis = 1)
  y = data[y_column]
  
  # define model
  model = BalancedBaggingClassifier()

  # define evaluation procedure
  cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

  scores = cross_validate(model, X, y, scoring=('accuracy',
           'recall',
           'precision',
           'balanced_accuracy',
           'f1',
           'roc_auc'),cv=cv, n_jobs=-1)
  
  return scores

report = random_forest(df, y_column)