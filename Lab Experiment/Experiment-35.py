import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png")

text = input("Enter text: ")

cv2.putText(
    img,
    text,
    (50, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 255),
    2
)

cv2.imshow("Text on Image", img)

cv2.imwrite("text_image.jpg", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
