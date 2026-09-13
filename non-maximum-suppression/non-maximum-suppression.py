def nms(boxes: list, scores: list, iou_threshold: float) -> list:
    """
    Returns a list of retained original indices in selection order.
    """
    if not boxes or not scores:
        return []

    # Helper function to compute Intersection over Union (IoU)
    def compute_iou(box1, box2):
        x1_min, y1_min, x1_max, y1_max = box1
        x2_min, y2_min, x2_max, y2_max = box2

        # Intersection coordinates
        x_left = max(x1_min, x2_min)
        y_top = max(y1_min, y2_min)
        x_right = min(x1_max, x2_max)
        y_bottom = min(y1_max, y2_max)

        # Intersection area
        intersection_w = max(0.0, x_right - x_left)
        intersection_h = max(0.0, y_bottom - y_top)
        intersection_area = intersection_w * intersection_h

        # Individual box areas
        area1 = (x1_max - x1_min) * (y1_max - y1_min)
        area2 = (x2_max - x2_min) * (y2_max - y2_min)

        # Union area
        union_area = area1 + area2 - intersection_area

        if union_area == 0:
            return 0.0

        return intersection_area / union_area

    # Sort indices by score descending; stable sort preserves original order on ties
    sorted_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)

    keep = []

    while sorted_indices:
        # Select highest scoring box remaining
        current = sorted_indices.pop(0)
        keep.append(current)

        # Retain only indices whose IoU with current box is strictly less than threshold
        remaining = []
        for idx in sorted_indices:
            iou = compute_iou(boxes[current], boxes[idx])
            if iou < iou_threshold:
                remaining.append(idx)
        sorted_indices = remaining

    return keep