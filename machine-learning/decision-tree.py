def decision_tree(data, y_column):
  X = data.drop(y_column, axis=1)
  y = data[y_column]

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

  from sklearn.tree import DecisionTreeClassifier
  from sklearn import metrics

  clf = DecisionTreeClassifier()

  # Train Decision Tree Classifer
  clf = clf.fit(X_train, y_train)

  #Predict the response for test dataset
  y_pred = clf.predict(X_test)

  print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

  from sklearn.tree import export_graphviz
  from sklearn.externals.six import StringIO  
  from IPython.display import Image  
  import pydotplus

  dot_data = StringIO()
  export_graphviz(clf, out_file=dot_data,  
                  filled=True, rounded=True,
                  special_characters=True,feature_names = X.columns.tolist(),class_names=['0','1'])
  graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
  graph.write_png('decision_tree.png')
  Image(graph.create_png())