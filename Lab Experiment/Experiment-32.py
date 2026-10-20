import cv2
import numpy as np

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

# Create white image
img = np.ones((height, width, 3), dtype=np.uint8) * 255

# Each box is 1/10 of image size
box_h = height // 10
box_w = width // 10

# Black - Top Left
img[0:box_h, 0:box_w] = (0, 0, 0)

# Blue - Top Right
img[0:box_h, width-box_w:width] = (255, 0, 0)

# Green - Bottom Left
img[height-box_h:height, 0:box_w] = (0, 255, 0)

# Red - Bottom Right
img[height-box_h:height, width-box_w:width] = (0, 0, 255)

cv2.imshow("Four Colored Boxes", img)

cv2.imwrite("four_colored_boxes.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
