import cv2
import os

# Set your input image path here
image_path = r"D:\Computer vision\Smile image.png"

# Load the pretrained Haar Cascade classifiers for face and smile detection
face_cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
smile_cascade_path = cv2.data.haarcascades + 'haarcascade_smile.xml'

face_cascade = cv2.CascadeClassifier(face_cascade_path)
smile_cascade = cv2.CascadeClassifier(smile_cascade_path)

if face_cascade.empty():
    print(f"Error: Could not load face cascade classifier from {face_cascade_path}")
    exit()

if smile_cascade.empty():
    print(f"Error: Could not load smile cascade classifier from {smile_cascade_path}")
    exit()

# Load the input image
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to load image at path '{image_path}'. Please verify the path.")
    exit()

# Resize image if it exceeds screen dimensions to ensure proper display fit
max_width, max_height = 1000, 700
h, w = image.shape[:2]
if w > max_width or h > max_height:
    scaling_factor = min(max_width / w, max_height / h)
    image = cv2.resize(image, (int(w * scaling_factor), int(h * scaling_factor)), interpolation=cv2.INTER_AREA)

# Convert the image to grayscale for detection
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces first
faces = face_cascade.detectMultiScale(
    gray_image,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

smile_found = False

# Detect smiles within each detected face Region of Interest (ROI)
for (x, y, w, h) in faces:
    roi_gray = gray_image[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

    smiles = smile_cascade.detectMultiScale(
        roi_gray,
        scaleFactor=1.7,
        minNeighbors=20,
        minSize=(25, 25)
    )

    if len(smiles) > 0:
        smile_found = True

    # Draw green rectangular bounding boxes around detected smiles
    for (sx, sy, sw, sh) in smiles:
        cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

if not smile_found:
    print("Warning: No smiles detected in the provided image.")

# Display the processed image with resizable window flag
window_title = "Smile Detection using OpenCV"
cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)
cv2.imshow(window_title, image)

# Define output filename and save the processed image in the current script directory
output_filename = "Experiment-30__smile detection.jpg"
output_path = os.path.join(os.getcwd(), output_filename)

success = cv2.imwrite(output_path, image)

if success:
    print(f"Output saved successfully at: {output_path}")
else:
    print("Error: Failed to save the output image.")

# Wait for a key press and close all OpenCV display windows
cv2.waitKey(0)
cv2.destroyAllWindows()
