import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png")

rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Original Image", img)
cv2.imshow("90 Degree Clockwise", rotated)

cv2.imwrite("rotated_90.jpg", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
