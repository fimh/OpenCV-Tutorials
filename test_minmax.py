import cv2
import numpy as np

a = np.array([[2, 3, 4, 5], [5, 67, 8, 9], [1, 3, 4, 5]])
print(a)
min_val, max_val, min_indx, max_indx = cv2.minMaxLoc(a)

print(min_val, max_val, min_indx, max_indx)
