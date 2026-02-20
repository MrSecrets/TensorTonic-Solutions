import math
def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here
    stride = image_size/feature_size
    anchors = []
    for i in range(feature_size):
        cy = (i+0.5)*stride
        for j in range(feature_size):
            cx = (j+0.5)*stride
            for scale in scales:
                for ratio in aspect_ratios:
                    sqrt_r = math.sqrt(ratio)
            # scale = scale*stride
                    w = (scale * sqrt_r) /2
                    h = (scale / sqrt_r) /2
                    anchor = [cx-w, cy-h, cx+w, cy+h]
                    anchors.append(anchor)

    return anchors
