import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png", 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

black_hat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow("Original Image", img)
cv2.imshow("Black Hat", black_hat)

cv2.imwrite("black_hat.jpg", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
