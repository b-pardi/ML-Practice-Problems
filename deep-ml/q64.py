import numpy as np

# 64 easy
def gini_impurity(y):
    """
    Calculate Gini Impurity for a list of class labels.

    :param y: List of class labels
    :return: Gini Impurity rounded to three decimal places
    """
    y_np = np.array(y)
    y_unique, y_count = np.unique(y_np, return_counts=True)
    probs = y_count / len(y)
    impurity = 1 - np.sum(np.square(probs))
    return np.round(impurity, 3)


if __name__ == '__main__':
    y = [0, 1, 1, 1, 0]
    print(gini_impurity(y))