import cv2
import os

video_path = r"D:\Computer vision\Indian_Road.mp4"
output_dir = r"D:\Computer vision\outputs"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
if fps <= 0:
    fps = 25

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(
    os.path.join(output_dir, "Experiment28_VehicleDetection.mp4"),
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps, (width, height)
)

bg = cv2.createBackgroundSubtractorMOG2(
    history=500, varThreshold=50, detectShadows=False
)

previous_gray = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if previous_gray is not None:
        difference = cv2.absdiff(gray, previous_gray)
        _, motion_mask = cv2.threshold(
            difference, 30, 255, cv2.THRESH_BINARY
        )
        movement = cv2.countNonZero(motion_mask)

        if movement > gray.size * 0.25:
            bg = cv2.createBackgroundSubtractorMOG2(
                history=500, varThreshold=50,
                detectShadows=False
            )
            previous_gray = gray.copy()

            cv2.putText(
                frame, "Camera Moving - Please Wait",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 0, 255), 2
            )

            out.write(frame)
            cv2.imshow("Vehicle Detection", frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
            continue

    previous_gray = gray.copy()

    mask = bg.apply(frame)
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )

    mask = cv2.morphologyEx(
        mask, cv2.MORPH_OPEN, kernel
    )
    mask = cv2.morphologyEx(
        mask, cv2.MORPH_CLOSE, kernel
    )

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        if cv2.contourArea(contour) > 2500:
            x, y, w, h = cv2.boundingRect(contour)

            if w > 35 and h > 30:
                cv2.rectangle(
                    frame, (x, y), (x+w, y+h),
                    (0, 255, 0), 2
                )
                cv2.putText(
                    frame, "Vehicle", (x, y-8),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 255, 0), 2
                )

    out.write(frame)
    cv2.imshow("Vehicle Detection", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Vehicle detection video saved successfully!")
