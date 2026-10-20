import cv2
import os

def count_faces(image, face_cascade):
    # Convert image to grayscale for detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces with stricter parameters to avoid false background detections
    faces = face_cascade.detectMultiScale(
        gray_image,
        scaleFactor=1.2,
        minNeighbors=10,
        minSize=(30, 30)
    )
    
    # Draw green bounding boxes around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    return len(faces)

# Set your input image path here
image_path = r"D:\Computer vision\Number of people.png"

# Load the pretrained Haar Cascade classifier for frontal face detection
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print(f"Error: Could not load Haar Cascade classifier from {cascade_path}")
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

# Count faces and draw bounding boxes
face_count = count_faces(image, face_cascade)

# Overlay the total face count text on the image
text = f"Total Faces Detected: {face_count}"
cv2.putText(image, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

# Print total faces detected in console
print(f"Total Faces Detected: {face_count}")

# Display the processed image with resizable window flag
window_title = "Face Counting using OpenCV"
cv2.namedWindow(window_title, cv2.WINDOW_NORMAL)
cv2.imshow(window_title, image)

# Define output filename and save the processed image in the current script directory
output_filename = "Experiment-38__face counting.jpg"
output_path = os.path.join(os.getcwd(), output_filename)

success = cv2.imwrite(output_path, image)

if success:
    print(f"Output saved successfully at: {output_path}")
else:
    print("Error: Failed to save the output image.")

# Wait for a key press and close all OpenCV display windows
cv2.waitKey(0)
cv2.destroyAllWindows()
