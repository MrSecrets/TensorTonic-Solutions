import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    # Your code here
    points = np.asarray(points)
    T = np.asarray(T)
    
    if points.ndim==1:
        points_h = np.append(points, 1)
        p_ =  (T @ points_h.T).T
        return p_[:3]

    else:
        ones = np.ones((points.shape[0], 1))
        points_h = np.hstack((points, ones))
        p_ =  (T @ points_h.T).T
        return p_[:, :3]