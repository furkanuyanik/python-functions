from sklearn.linear_model import LogisticRegression 
from sklearn.metrics import confusion_matrix, classification_report 
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

def logistic_regression(data, y_column):
  X = data.drop(y_column, axis = 1)
  y = data[y_column]

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 1234)

  lr = LogisticRegression() 
    
  lr.fit(X_train, y_train)
    
  print(lr)
  
  predictions = lr.predict(X_test)
  
  lr_probs = lr.predict_proba(X_test)
  lr_probs = lr_probs[:, 1]
  
  lr_auc = roc_auc_score(y_test, lr_probs)
  
  print('Logistic: ROC AUC=%.3f' % (lr_auc))
  print(confusion_matrix(y_test, predictions)) 