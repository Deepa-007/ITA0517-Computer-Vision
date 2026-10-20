import cv2
import numpy as np

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

img = np.ones(
    (height, width, 3),
    dtype=np.uint8
) * 255

center = (width // 2, height // 2)
radius = min(width, height) // 4

cv2.circle(
    img,
    center,
    radius,
    (255, 0, 0),
    3
)

cv2.imshow("Circle", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
