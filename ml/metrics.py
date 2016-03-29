from sklearn.metrics import confusion_matrix, precision_recall_fscore_support


def evaluate_prediction(y_true, y_pred):
    """ evaluate prediction performance, given the ground truth

    :param y_true: correct target values
    :param y_pred: predicted values
    :return: confusion matrix (tp, tn, fp and fn), precision, recall, and F-score
    """
    cm = confusion_matrix(y_true, y_pred)

    precision, recall, fscore, _ = precision_recall_fscore_support(y_true, y_pred)
    return cm, precision, recall, fscore
