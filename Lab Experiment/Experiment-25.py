import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blur, 50, 150)

contours, _ = cv2.findContours(
    edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)

    if w > 30 and h > 30:
        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

cv2.imshow("Object Recognition", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
