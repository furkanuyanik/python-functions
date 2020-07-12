from sklearn.model_selection import train_test_split
import tensorflow.python.keras
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.layers import InputLayer
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import Dropout
from tensorflow.python.keras.constraints import maxnorm
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix

def artifical_neural_network(data, y_column):
  X = data.drop(y_column, axis=1)
  y = data[y_column]

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1234)

  model = Sequential()
  model.add(Dense(64, input_dim=X.shape[1], activation='relu', kernel_constraint=maxnorm(3)))
  model.add(Dropout(rate=0.1))
  model.add(Dense(32, activation='relu', kernel_constraint=maxnorm(5)))
  model.add(Dropout(rate=0.1))
  model.add(Dense(1, activation='sigmoid'))

  model.compile(loss = "binary_crossentropy", optimizer = 'adam', metrics=['accuracy'])

  train_acc = model.evaluate(X_train, y_train, verbose=0)
  test_acc = model.evaluate(X_test, y_test, verbose=0)

  history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=50, batch_size=50)

  # predict probabilities for test set
  yhat_probs = model.predict(X_test, verbose=0)
  
  # predict crisp classes for test set
  yhat_classes = model.predict_classes(X_test, verbose=0)
  
  # reduce to 1d array
  yhat_probs = yhat_probs[:, 0]
  yhat_classes = yhat_classes[:, 0]

  # accuracy: (tp + tn) / (p + n)
  accuracy = accuracy_score(y_test, yhat_classes)
  print('Accuracy: %f' % accuracy)
  
  # precision tp / (tp + fp)
  precision = precision_score(y_test, yhat_classes)
  print('Precision: %f' % precision)
  
  # recall: tp / (tp + fn)
  recall = recall_score(y_test, yhat_classes)
  print('Recall: %f' % recall)
  
  # f1: 2 tp / (2 tp + fp + fn)
  f1 = f1_score(y_test, yhat_classes)
  print('F1 score: %f' % f1)

  # kappa
  kappa = cohen_kappa_score(y_test, yhat_classes)
  print('Cohens kappa: %f' % kappa)
  
  # ROC AUC
  auc = roc_auc_score(y_test, yhat_probs)
  print('ROC AUC: %f' % auc)
  
  # confusion matrix
  # [[tn fp]
  # [fn tp]]
  matrix = confusion_matrix(y_test, yhat_classes)
  print(matrix)