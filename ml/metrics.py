from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
import numpy as np


def evaluate_prediction(y_true, y_pred):
    """ evaluate prediction performance, given the ground truth

    :param y_true: correct target values
    :param y_pred: predicted values
    :return: confusion matrix, tp, tn, fp, fn precision, recall, F-score, and support
    """
    cm = confusion_matrix(y_true, y_pred)
    precision, recall, fscore, support = precision_recall_fscore_support(y_true, y_pred)
    return cm, tp_tn_fp_fn(cm), precision, recall, fscore, support


def tp_tn_fp_fn(cm):
    """ get true positive, true negative, false positive and false negative from the confusion matrix

    :param cm: confusion matrix
    :return: tp, tn, fp, fn
    """
    nb_class = len(cm)
    stats = np.zeros((4, nb_class))
    hor_sum = np.sum(cm, axis=1)
    ver_sum = np.sum(cm, axis=0)
    total_sum = np.sum(cm)
    for i in range(nb_class):
        stats[0, i] = cm[i][i]  # tp
        stats[1, i] = total_sum + cm[i][i] - hor_sum[i] - ver_sum[i]  # tn
        stats[2, i] = ver_sum[i] - cm[i][i]  # fp
        stats[3, i] = hor_sum[i] - cm[i][i]  # fn
    return stats
