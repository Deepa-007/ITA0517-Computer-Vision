import cv2
image = cv2.imread(r"C:\Users\DELL\Desktop\Image 1.png")
blur = cv2.GaussianBlur(image, (5, 5), 10)
cv2.imwrite('blurred_image.jpg', blur)
cv2.imshow('Blurred Image', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
