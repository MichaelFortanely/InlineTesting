from sklearn import tree
import pandas as pd 
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.metrics import accuracy_score, log_loss

def setup_train_set(train_file, clf):

    # get training set
    train = pd.read_csv(train_file, index_col=0)
    train.columns = train.columns.astype(str)
    # train.rename(columns={"Unnamed: 0": 'Test Id'}, inplace=True)
    train = train.fillna(0)
    train.to_csv("../inline_features.csv", index = False)

    # train and test split
    Y = train.isLOI
    X = train.drop(columns = ['isLOI', 'line_number', 'line'])
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 42)
    clf = clf.fit(X_train, y_train)

    # predict and store results
    test_preds = clf.predict(X_test)
    test_file = pd.DataFrame({"Test Id": X_test[X_test.columns[0]], "Line of Interest":test_preds})
    test_file.to_csv("../inline_test_sol.csv", index = False)

    # results on test set
    print("Based on", train_file+",", "the test set yielded these results:")
    print("Accuracy:", accuracy_score(y_test, test_preds))
    print("Entropy:", log_loss(y_test, test_preds))

def inline_worthiness(clf, prgm_stmt_file):

    # get the features
    prgm_features = prgm_stmt_file.drop(columns = ['line_number', 'line'])
    prgm_features = prgm_features.fillna(0)
    # print(prgm_features)

    # results on user set
    inline_worthiness = clf.predict(prgm_features)
    return inline_worthiness

def test_inline():

    # get data set
    train = pd.read_csv("./example.csv", index_col=0)
    train.columns = train.columns.astype(str)
    train = train.fillna(0)
    # print(train)

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

    # SIMULATE USER INPUT
    import sys
    sys.path.append('../')
    import parsing
    import ml_model.decision_tree as decision_tree
    prgm_lines = parsing.create_single_set("import math.set\nhello")
    prgm_stmt_file = decision_tree.run_user_tree(prgm_lines)

    # get the features
    prgm_features = prgm_stmt_file.drop(columns = ['line_number', 'line'])
    # prgm_features.rename(columns={"Unnamed: 0": 'Test Id'}, inplace=True)
    prgm_features = prgm_features.fillna(0)
    # prgm_features.insert(0, "Test Id", [x for x in range(len(prgm_features))])
    # print("PROGRAM:\n", prgm_features)

    # results on user set
    inline_worthiness = clf.predict(prgm_features)
    # prgm_worthiness = pd.DataFrame({"Line of Interest": inline_worthiness})
    # prgm_worthiness.insert(0, "Test Id", [x for x in range(len(prgm_worthiness))])
    # print(inline_worthiness)
    return inline_worthiness

# test_inline()