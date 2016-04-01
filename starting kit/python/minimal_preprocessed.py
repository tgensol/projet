from __future__ import division, print_function
import os

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_svmlight_file

"""
Minimal code to load the preprocessed data, train a classic Random Forest,
computes the predictions on the valid and the test sets and write them to
files ('valid.predict' & 'test.predict').

Tested with :
- Anaconda 2.3.0
- Python 2.7
- Python 3.5
"""

# Change the path to your data location :
data_dir = os.path.abspath('../data/')

if __name__ == '__main__':
    print('I am at your service, Master.')
    # Load the sparse training data :
    X_train, y_train = load_svmlight_file(
        os.path.join(data_dir, 'train_preprocessed.data'))
    # Now X_train contains a 'scipy.sparse.csr.csr_matrix'
    # And y_train is a simple numpy array of float64
    # (even if the labels are only 0 or 1)

    # Load the sparse validation data :
    X_valid, y_valid = load_svmlight_file(
        os.path.join(data_dir, 'valid_preprocessed.data'))
    # Now X_valid contains a 'scipy.sparse.csr.csr_matrix'
    # And y_valid is a simple numpy array of float64
    # (even if the labels are only 0 or 1)

    # Load the sparse validation data :
    X_test, y_test = load_svmlight_file(
        os.path.join(data_dir, 'test_preprocessed.data'))
    # Now X_test contains a 'scipy.sparse.csr.csr_matrix'
    # And y_test is a simple numpy array of float64
    # (even if the labels are only 0 or 1)

    # Declaration of the model algorithm
    clf = RandomForestClassifier()
    # Most of the classifiers can take sparse matrix as inputs
    #  (they automatically convert it if necessary)
    # fit() function is used to train the classifier
    clf.fit(X_train, y_train)

    # Computes the prediction thanks to the predict() function
    # for the validation set
    valid_predictions = clf.predict(X_valid)
    # and the test set
    test_predictions = clf.predict(X_test)

    # Before writing the predictions you have to convert the predictions arrays
    # to integers in order to write a well formatted submission file
    valid_predictions = np.array(valid_predictions, dtype=int)
    test_predictions = np.array(test_predictions, dtype=int)
    # Now let's write the submission files
    np.savetxt('valid.predict', valid_predictions, fmt='%d')
    np.savetxt('test.predict', test_predictions, fmt='%d')

    print('Done.')
