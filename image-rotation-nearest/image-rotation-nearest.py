import math
def rotate_image(image, angle_degrees):
    """
    Rotate the image counterclockwise by the given angle using nearest neighbor interpolation.
    """
    # Write code here
    w, h = len(image[0]), len(image)
    cx, cy = (w-1)/2, (h-1)/2
    result = [[0 for _ in range(w)] for _ in range(h)]

    angle = math.radians(angle_degrees)
    cos_ang = math.cos(angle)
    sin_ang = math.sin(angle)
    for x in range(w):
        dx = x-cx
        dx_cos = dx*cos_ang
        dx_sin = dx*sin_ang
        for y in range(h):
            dy = y-cy
            dy_cos = dy*cos_ang
            dy_sin = dy*sin_ang

            src_x = cx - dy_sin + dx_cos
            src_y = cy + dy_cos + dx_sin
            src_x, src_y = round(src_x), round(src_y)
            if 0<=src_x<w and 0<=src_y<h:
                result[y][x] = image[src_y][src_x]

    return result
            