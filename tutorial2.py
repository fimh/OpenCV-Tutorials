import cv2
import random

img = cv2.imread('assets/logo.jpg', cv2.IMREAD_UNCHANGED)
print(img.shape)

# Change first 100 rows to random pixels
for i in range(300, 400):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

# Copy part of image
tag = img[200:250, 200:300]
img[500:550, 500:600] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
