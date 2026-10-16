import cv2
image = cv2.imread(r"C:\Users\DELL\Desktop\Image 1.png")
height, width = image.shape[:2]
scale_factor = 3.0
bigger_image = cv2.resize(image, (int(width * scale_factor), int(height * scale_factor)))
scale_factor = 0.5
smaller_image = cv2.resize(image, (int(width * scale_factor), int(height * scale_factor)))
cv2.imshow('original image', image)
cv2.imshow('Bigger image', bigger_image)
cv2.imshow('smaller image', smaller_image)
cv2.imwrite('Bigger_image.jpg', bigger_image)
cv2.imwrite('smaller_image.jpg', smaller_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
