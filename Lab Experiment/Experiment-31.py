import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png", 0)

_, segmented = cv2.threshold(
    img,
    127,
    255,
    cv2.THRESH_BINARY
)

cv2.imshow("Original Image", img)
cv2.imshow("Segmented Image", segmented)

cv2.imwrite("segmented_image.jpg", segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()
