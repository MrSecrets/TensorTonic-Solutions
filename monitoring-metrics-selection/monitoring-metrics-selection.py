import math
def compute_monitoring_metrics(system_type, y_true, y_pred):
    """
    Compute the appropriate monitoring metrics for the given system type.
    """
    # Write code here
    n = len(y_true)
    # print(system_type)
    match system_type:
        case "classification":
            TP = TN = FP = FN = 0
            for i in range(n):
                if y_true[i]:
                    if y_pred[i]:
                        TP+=1
                    else:
                        FN+=1
                else:
                    if not y_pred[i]:
                        TN+=1
                    else:
                        FP+=1

            accuracy = (TP+TN)/n
            precision = TP/(TP+FP) if TP+FP!=0 else 0
            recall = TP/(TP+FN) if TP+FN!=0 else 0
            f1 = (2*precision*recall)/(precision+recall) if precision+recall!=0 else 0
            return [("accuracy", accuracy), ("f1", f1), ("precision", precision), ("recall", recall)]

        case "regression":
            mae , rmse = 0, 0
            for i in range(n):
                diff = abs(y_true[i] - y_pred[i])
                mae += diff
                rmse += diff**2
            mae = mae/n
            rmse = math.sqrt(rmse/n)
            return [("mae", mae), ("rmse", rmse)]

        case "ranking":
            combined = list(zip(y_pred, y_true))
            combined.sort(reverse=True)
            total_relevent = sum(y_true)
            relevent_3 = 0
            for i in range(3):
                relevent_3 += combined[i][1]
            precision_at_3 = relevent_3/3
            if total_relevent == 0:
                recall_t_3 = 0
            else:
                recall_t_3 = relevent_3/total_relevent
            return [("precision_at_3", precision_at_3), ("recall_at_3", recall_t_3)]

        case _:
            # print(n)
            return [()]