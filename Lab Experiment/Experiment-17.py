import cv2

img = cv2.imread(r"D:\Computer vision\Original pic.png")

watermarked = img.copy()

cv2.putText(
    watermarked,
    "WATERMARK",
    (50, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

cv2.imshow("Original Image", img)
cv2.imshow("Watermarked Image", watermarked)

cv2.imwrite("watermarked_image.jpg", watermarked)

cv2.waitKey(0)
cv2.destroyAllWindows()
