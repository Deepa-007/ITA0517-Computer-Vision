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

fourcc = cv2.VideoWriter_fourcc(*"mp4v")

slow = cv2.VideoWriter(
    os.path.join(output_dir, "Experiment07_SlowMotion.mp4"),
    fourcc, fps / 2, (width, height)
)

fast = cv2.VideoWriter(
    os.path.join(output_dir, "Experiment07_FastMotion.mp4"),
    fourcc, fps * 2, (width, height)
)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    slow.write(frame)
    fast.write(frame)

    cv2.imshow("Video Processing", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
slow.release()
fast.release()
cv2.destroyAllWindows()

print("Slow and fast videos saved successfully!")
