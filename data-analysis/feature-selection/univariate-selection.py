def univariate_selection(data, y_column): 
  X = data.drop(y_column, axis=1)
  y = data[y_column]

  from sklearn.feature_selection import SelectKBest
  from sklearn.feature_selection import chi2

  bestfeatures = SelectKBest(score_func=chi2, k=10)
  fit = bestfeatures.fit(X,y)
  dfscores = pd.DataFrame(fit.scores_)
  dfcolumns = pd.DataFrame(X.columns)

  featureScores = pd.concat([dfcolumns,dfscores],axis=1)

  featureScores.columns = ['Specs', 'Score']  #naming the dataframe columns
  print(featureScores.nlargest(50, 'Score'))  #print 10 best features