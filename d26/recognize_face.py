import cv2
import json
import numpy as np
from tensorflow.keras.models import load_model

model = load_model(
    "face_recognition_model.h5"
)


with open("class_names.json", "r") as f:
    class_indices = json.load(f)

class_names = {
    v: k for k, v in class_indices.items()
}

print("Loaded Classes:")
print(class_names)

CONFIDENCE_THRESHOLD = 85

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

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
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:

        face = frame[y:y+h, x:x+w]

        face = cv2.resize(
            face,
            (224, 224)
        )

        face = face.astype(
            "float32"
        ) / 255.0

        face = np.expand_dims(
            face,
            axis=0
        )

        pred = model.predict(
            face,
            verbose=0
        )

        idx = np.argmax(pred)

        confidence = np.max(pred) * 100

        if confidence < CONFIDENCE_THRESHOLD:

            name = "Unknown"
            color = (0, 0, 255)

        else:

            name = class_names[idx]
            color = (0, 255, 0)

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            color,
            2
        )

        cv2.putText(
            frame,
            f"{name} {confidence:.1f}%",
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

    cv2.imshow(
        "Face Recognition",
        frame
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()