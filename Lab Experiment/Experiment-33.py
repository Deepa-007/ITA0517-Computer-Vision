import cv2
import numpy as np

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

img = np.ones(
    (height, width, 3),
    dtype=np.uint8
) * 255

cv2.rectangle(
    img,
    (50, 50),
    (width - 50, height - 50),
    (0, 0, 255),
    3
)

cv2.imshow("Rectangle", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
