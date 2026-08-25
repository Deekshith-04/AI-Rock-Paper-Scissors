import cv2
import mediapipe as mp
import csv
import os
import time

# ============================================================
# SETTINGS
# ============================================================

SAMPLES_PER_GESTURE = 500

GESTURES = [
    ("Rock", "✊"),
    ("Paper", "✋"),
    ("Scissors", "✌")
]

OUTPUT_FILE = "dataset/gesture_dataset_v3.csv"

# Time between saved samples
SAMPLE_DELAY = 0.05

# ============================================================
# MEDIAPIPE
# ============================================================

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

# ============================================================
# DATASET SETUP
# ============================================================

os.makedirs("dataset", exist_ok=True)

columns = []

for i in range(21):
    columns.extend([
        f"x{i}",
        f"y{i}",
        f"z{i}"
    ])

columns.append("label")

# Always create a NEW dataset
file = open(
    OUTPUT_FILE,
    "w",
    newline=""
)

writer = csv.writer(file)
writer.writerow(columns)

# ============================================================
# CAMERA
# ============================================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Could not open camera.")
    file.close()
    exit()

# ============================================================
# INSTRUCTIONS
# ============================================================

print()
print("================================================")
print("        GESTURE DATASET V3 COLLECTION")
print("================================================")
print()
print("We will collect:")
print("  ✊ Rock     - 500 samples")
print("  ✋ Paper    - 500 samples")
print("  ✌ Scissors - 500 samples")
print()
print("IMPORTANT:")
print("Show ONLY the gesture currently being collected.")
print("Move your hand slightly during collection.")
print("Keep the entire hand visible.")
print()
print("Press Q inside the camera window to quit.")
print()

# ============================================================
# COLLECTION
# ============================================================

total_samples = 0

for gesture, symbol in GESTURES:

    count = 0

    print()
    print("------------------------------------------------")
    print(f"NEXT GESTURE: {symbol} {gesture}")
    print("------------------------------------------------")
    print()
    print(f"Make the {gesture} gesture.")
    input(f"Press ENTER when you are ready for {gesture}...")

    # --------------------------------------------------------
    # 3 SECOND COUNTDOWN
    # --------------------------------------------------------

    for seconds in [3, 2, 1]:

        start = time.time()

        while time.time() - start < 1:

            ret, frame = cap.read()

            if not ret:
                continue

            frame = cv2.flip(frame, 1)

            cv2.putText(
                frame,
                f"GET READY: {gesture}",
                (30, 60),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.2,
                (0, 255, 255),
                3
            )

            cv2.putText(
                frame,
                f"Starting in {seconds}",
                (30, 110),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 255),
                2
            )

            cv2.imshow(
                "Gesture Dataset V3",
                frame
            )

            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                file.close()
                cap.release()
                cv2.destroyAllWindows()
                exit()

    print(f"Collecting {gesture}...")

    # --------------------------------------------------------
    # COLLECT SAMPLES
    # --------------------------------------------------------

    while count < SAMPLES_PER_GESTURE:

        ret, frame = cap.read()

        if not ret:
            continue

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = hands.process(rgb)

        detected = False

        if results.multi_hand_landmarks:

            hand = results.multi_hand_landmarks[0]

            wrist = hand.landmark[0]

            features = []

            # Normalize landmarks relative to wrist
            for landmark in hand.landmark:

                x = landmark.x - wrist.x
                y = landmark.y - wrist.y
                z = landmark.z - wrist.z

                features.extend([
                    x,
                    y,
                    z
                ])

            # Draw landmarks
            mp_draw.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            detected = True

        # ----------------------------------------------------
        # DISPLAY
        # ----------------------------------------------------

        cv2.putText(
            frame,
            f"COLLECTING: {symbol} {gesture}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            f"Samples: {count}/{SAMPLES_PER_GESTURE}",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        if detected:

            cv2.putText(
                frame,
                "HAND DETECTED",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            # Save sample
            writer.writerow(
                features + [gesture]
            )

            count += 1
            total_samples += 1

            file.flush()

            # Small delay between samples
            time.sleep(SAMPLE_DELAY)

        else:

            cv2.putText(
                frame,
                "NO HAND",
                (20, 120),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

        cv2.imshow(
            "Gesture Dataset V3",
            frame
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):

            print()
            print("Collection stopped by user.")

            file.close()
            cap.release()
            cv2.destroyAllWindows()

            exit()

    print(f"{gesture}: {count} samples collected.")

# ============================================================
# FINISH
# ============================================================

file.close()

cap.release()

cv2.destroyAllWindows()

print()
print("================================================")
print("           DATASET COLLECTION COMPLETE")
print("================================================")
print()
print(f"Saved to: {OUTPUT_FILE}")
print(f"Total samples: {total_samples}")
print()
print("Rock     : 500")
print("Paper    : 500")
print("Scissors : 500")
print()