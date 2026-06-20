import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    y_train, X_test = np.asarray(y_train), np.asarray(X_test)
    labels,counts = np.unique(y_train, return_counts=True)
    # print(labels)
    largest = labels[np.argmax(counts)]
    size_ = X_test.shape

    # print(largest, size_)
    return np.full(size_, fill_value=largest)