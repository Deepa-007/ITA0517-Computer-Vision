import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png", 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

erosion = cv2.morphologyEx(img, cv2.MORPH_ERODE, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Morphological Erosion", erosion)

cv2.imwrite("morphological_erosion.jpg", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()
