import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png")

roi = img[50:250, 50:250]

cv2.imshow("Original Image", img)
cv2.imshow("Cropped ROI", roi)

cv2.imwrite("cropped_image.jpg", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
