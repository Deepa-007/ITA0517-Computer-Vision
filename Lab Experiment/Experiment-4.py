import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png", 0)

equalized = cv2.equalizeHist(img)

cv2.imshow("Original Image", img)
cv2.imshow("Histogram Equalized", equalized)

cv2.imwrite("histogram_equalized.jpg", equalized)

cv2.waitKey(0)
cv2.destroyAllWindows()
