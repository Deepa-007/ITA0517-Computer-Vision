import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png", 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Opening", opening)

cv2.imwrite("opening.jpg", opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
