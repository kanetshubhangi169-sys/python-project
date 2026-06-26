import cv2
import os

name = input("Enter Person Name: ").strip()

path = os.path.join("dataset", name)

os.makedirs(path, exist_ok=True)

count = len(os.listdir(path))

cap = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

print("\nPress S = Save Image")
print("Press Q = Quit\n")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_detector.detectMultiScale(
        gray,
        1.3,
        5
    )

    current_face = None

    for (x, y, w, h) in faces:

        padding = 40

        x1 = max(0, x - padding)
        y1 = max(0, y - padding)

        x2 = min(
            frame.shape[1],
            x + w + padding
        )

        y2 = min(
            frame.shape[0],
            y + h + padding
        )

        current_face = frame[
            y1:y2,
            x1:x2
        ]

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f"Saved: {count}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Collect Data",
        frame
    )

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):

        if current_face is not None:

            count += 1

            current_face = cv2.resize(
                current_face,
                (224, 224)
            )

            filename = os.path.join(
                path,
                f"{count}.jpg"
            )

            cv2.imwrite(
                filename,
                current_face
            )

            print(
                f"Saved -> {filename}"
            )

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()