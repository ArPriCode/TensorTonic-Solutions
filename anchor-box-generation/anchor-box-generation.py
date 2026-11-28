import math

def generate_anchors(feature_size: int, image_size: float, scales: list[float], aspect_ratios: list[float]) -> list[list[float]]:
    stride = image_size / feature_size
    wh = [(s * math.sqrt(r) / 2.0, s / (math.sqrt(r) * 2.0)) for s in scales for r in aspect_ratios]
    
    anchors = []
    for i in range(feature_size):
        cy = (i + 0.5) * stride
        for j in range(feature_size):
            cx = (j + 0.5) * stride
            for hw, hh in wh:
                anchors.append([cx - hw, cy - hh, cx + hw, cy + hh])
                
    return anchors