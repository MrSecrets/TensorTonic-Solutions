import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """

    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)    

    # indices = np.lexsort(y_score)[::-1]
    indices = np.argsort(y_score)[::-1]
    # # print(indices)
    y_true = y_true[indices]
    y_score = y_score[indices]

    distinct = np.where(np.diff(y_score))[0]
    end_thresholds = np.r_[distinct, y_true.size - 1]
    # print(distinct)
    cum_TP = np.cumsum(y_true)[end_thresholds]
    cum_FP = np.cumsum(1-y_true)[end_thresholds]
    
    tpr = cum_TP/cum_TP[-1]
    fpr = cum_FP/cum_FP[-1]
    
    tpr = np.r_[0, tpr]
    fpr = np.r_[0, fpr]
    thresholds = np.r_[float("inf"), y_score[end_thresholds]]


    return (fpr, tpr, thresholds)