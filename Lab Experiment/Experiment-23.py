import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png", 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Top Hat", top_hat)

cv2.imwrite("top_hat.jpg", top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
