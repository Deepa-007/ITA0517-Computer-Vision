import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png", 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

eroded = cv2.erode(img, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Eroded Image", eroded)

cv2.imwrite("eroded_image.jpg", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
