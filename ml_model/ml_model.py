from sklearn import tree
import pandas as pd 
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score, log_loss

train_url = "https://raw.githubusercontent.com/MichaelFortanely/InlineTesting/main/ml_model/example.csv"

train = pd.read_csv(train_url)

train.columns = train.columns.astype(str)

train = train.fillna(0)

train.to_csv("inline_features.csv", index = False)

Y = train.isLOI
X = train.drop(columns = ['isLOI', 'line_number', 'line'])

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

test_preds = clf.predict(X_test)
test_file = pd.DataFrame({"Test Id": X_test[X_test.columns[0]], "Line of Interest":test_preds})
test_file.to_csv("inline_test_sol.csv", index = False)

# results
print("Accuracy:", accuracy_score(y_test, test_preds))
print("Entropy:", log_loss(y_test, test_preds))
