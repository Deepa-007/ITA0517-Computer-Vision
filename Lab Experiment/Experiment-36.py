import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = (0, 0, 0)
upper = (180, 255, 100)

mask = cv2.inRange(hsv, lower, upper)

background = cv2.bitwise_and(
    img,
    img,
    mask=mask
)

cv2.imshow("Original Image", img)
cv2.imshow("Background", background)

cv2.waitKey(0)
cv2.destroyAllWindows()
