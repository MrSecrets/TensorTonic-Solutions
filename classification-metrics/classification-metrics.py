import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    # Write code here
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)

    classess =np.unique(y_true) 
    k,n = len(classess), len(y_true) #classess, length
    confusion = np.zeros((k,k))
    for a, p in zip(y_true, y_pred):
        confusion[a,p] +=1
    # print(confusion)

    TP = np.diag(confusion)
    FP = np.sum(confusion, axis=0) - TP
    FN = np.sum(confusion, axis=1) - TP
    TN = np.sum(confusion) - (TP+FP+FN)

    if average=="micro":
        micro_tp = np.sum(TP)
        micro_fp = np.sum(FP)
        micro_fn = np.sum(FN)
        micro_tn = np.sum(TN)

        precision = micro_tp / (micro_tp + micro_fp)
        recall    = micro_tp / (micro_tp + micro_fn)
        f1 = 2 * precision * recall / (precision + recall)
    
    else:
        base_precision = TP / (TP + FP)
        base_recall = TP/(TP+FN)
        base_f1 = 2 * (base_precision * base_recall)/(base_precision + base_recall)

        if average == "macro":
            precision = np.mean(base_precision)
            recall = np.mean(base_recall)
            f1 = np.mean(base_f1)
        elif average == "binary":
            precision = base_precision[pos_label]
            recall = base_recall[pos_label]
            f1 = base_f1[pos_label]
        elif average=="weighted":
            support = np.sum(confusion, axis=1)
            precision = np.average(base_precision, weights=support)
            recall = np.average(base_recall, weights=support)
            f1 = np.average(base_f1, weights=support)

    accuracy = np.trace(confusion) / np.sum(confusion)
    
    return {
        "accuracy" : accuracy,
        "precision" : precision,
        "recall" : recall,
        "f1" : f1
    }
    