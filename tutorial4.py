import numpy as np
import cv2

cap = cv2.VideoCapture(0)

print(cv2.__version__)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    img = cv2.flip(frame, 1)
    img = cv2.line(img, (0, 50), (width, 50), (0, 0, 255), 2, cv2.LINE_AA)
    img = cv2.line(img, (0, 0), (width//2, height//2), (0, 0, 255), 4)
    img = cv2.line(img, (0, height), (width//2, height//2), (0, 255, 0), 1)
    img = cv2.rectangle(img, (100, 100), (300, 300), (128, 128, 128), 1)
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), 1, cv2.LINE_AA)
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'OpenCV is Great!', (16, height - 16), font, 1, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
