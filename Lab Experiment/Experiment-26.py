import cv2
import os

video_path = r"D:\Computer vision\Demonslayer_Video.mp4"
output_dir = r"D:\Computer vision\outputs"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 25

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

out = cv2.VideoWriter(
    os.path.join(output_dir, "Experiment26_Reversed.mp4"),
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps, (width, height)
)

for frame in reversed(frames):
    out.write(frame)
    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()

print("Reversed video saved successfully!")
