import cv2

img = cv2.imread(r"C:\Users\DELL\Desktop\Image 1.png", 0)

sobel_x = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)

cv2.imwrite('sobel_x.jpg', sobel_x)
cv2.imshow('Sobel X', sobel_x)

cv2.waitKey(0)
cv2.destroyAllWindows()
