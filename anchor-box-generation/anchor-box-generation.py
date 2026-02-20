import math
def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    # Write code here
    # stride = image_size/feature_size
    # anchors = []
    # for scale in scales:
    #     for ratio in aspect_ratios:
    #         sqrt_r = math.sqrt(ratio)
    #         # scale = scale*stride
    #         w = (scale * sqrt_r) /2
    #         h = (scale / sqrt_r) /2
    #         for i in range(feature_size):
    #             for j in range(feature_size):
    #                 cx = (j+0.5)*stride
    #                 cy = (i+0.5)*stride
    #                 anchor = [cx-w, cy-h, cx+w, cy+h]
    #                 anchors.append(anchor)

    # return anchors


    stride = image_size / feature_size
    anchors = []

    for i in range(feature_size):
        for j in range(feature_size):
            cx = (j + 0.5) * stride
            cy = (i + 0.5) * stride

            for scale in scales:
                for ratio in aspect_ratios:
                    sqrt_r = math.sqrt(ratio)

                    w = scale * sqrt_r
                    h = scale / sqrt_r

                    x_min = cx - w / 2
                    y_min = cy - h / 2
                    x_max = cx + w / 2
                    y_max = cy + h / 2

                    anchors.append([x_min, y_min, x_max, y_max])

    return anchors