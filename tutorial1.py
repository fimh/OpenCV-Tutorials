import cv2

img = cv2.imread('assets/logo.jpg', cv2.IMREAD_UNCHANGED)
img = cv2.resize(img, None, fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('new_img.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
