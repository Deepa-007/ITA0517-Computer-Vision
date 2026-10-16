
import cv2
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

video_path = r"D:\Computer vision\Demonslayer_Video.mp4"
output_dir = r"D:\Computer vision\outputs"
output_file = os.path.join(
    output_dir, "Experiment40_ExtractedText.txt"
)

os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open video.")
    raise SystemExit

seen_text = set()
frame_number = 0
frame_interval = 15

with open(output_file, "w", encoding="utf-8") as file:
    file.write("EXPERIMENT 40: TEXT EXTRACTION USING OCR\n\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_number += 1

        if frame_number % frame_interval != 0:
            continue

        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Enlarge the frame
        gray = cv2.resize(
            gray, None, fx=2, fy=2,
            interpolation=cv2.INTER_CUBIC
        )

        # Improve contrast
        gray = cv2.equalizeHist(gray)

        # Extract words and their confidence scores
        data = pytesseract.image_to_data(
            gray,
            config="--oem 3 --psm 11",
            output_type=pytesseract.Output.DICT
        )

        words = []

        for i, word in enumerate(data["text"]):
            word = word.strip()

            try:
                confidence = float(data["conf"][i])
            except (ValueError, TypeError):
                continue

            # Discard uncertain OCR results
            if word and confidence >= 65:
                words.append(word)

        text = " ".join(words)
        text = " ".join(text.split())

        if text and text not in seen_text:
            seen_text.add(text)

            print(f"Frame {frame_number}: {text}")
            file.write(f"Frame {frame_number}:\n{text}\n\n")

    if not seen_text:
        file.write("No reliable text detected in the sampled frames.\n")
        print("No reliable text detected.")

cap.release()

print("\nText extraction completed!")
print("Unique text entries:", len(seen_text))
print("Saved to:", output_file)
