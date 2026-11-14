import math


def compute_monitoring_metrics(
    system_type: str, y_true: list, y_pred: list
) -> dict:
    if system_type == "classification":
        tp = fp = fn = tn = 0
        for yt, yp in zip(y_true, y_pred):
            if yt == 1 and yp == 1:
                tp += 1
            elif yt == 0 and yp == 1:
                fp += 1
            elif yt == 1 and yp == 0:
                fn += 1
            else:
                tn += 1

        n = len(y_true)
        accuracy = (tp + tn) / n if n > 0 else 0.0
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (
            (2 * precision * recall) / (precision + recall)
            if (precision + recall) > 0
            else 0.0
        )

        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1,
        }

    elif system_type == "regression":
        n = len(y_true)
        mae = sum(abs(yt - yp) for yt, yp in zip(y_true, y_pred)) / n
        rmse = math.sqrt(
            sum((yt - yp) ** 2 for yt, yp in zip(y_true, y_pred)) / n
        )

        return {
            "mae": mae,
            "rmse": rmse,
        }

    elif system_type == "ranking":
        sorted_indices = sorted(
            range(len(y_pred)), key=lambda i: y_pred[i], reverse=True
        )
        top_3 = sorted_indices[:3]
        hits = sum(1 for i in top_3 if y_true[i] == 1)
        total_relevant = sum(1 for yt in y_true if yt == 1)

        precision_at_3 = hits / 3.0
        recall_at_3 = hits / total_relevant if total_relevant > 0 else 0.0

        return {
            "precision_at_3": precision_at_3,
            "recall_at_3": recall_at_3,
        }