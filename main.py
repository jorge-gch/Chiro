import cv2

from hand_detector import HandDetector
from classifier import Classifier



detector = HandDetector()
classifier = Classifier()


# OPEN CAMERA

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara")
    exit()


# LOOP

while True:

    success, frame = cap.read()

    if not success:
        print("No se pudo leer la cámara")
        break

    # Mirror effect
    frame = cv2.flip(frame, 1)

    # OpenCV uses BGR
    # MediaPipe requires RGB
    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # DETECT HAND

    hands = detector.detect(rgb_frame)

    # DRAW LANDMARKS

    if hands:

        for hand in hands:
            gesture = classifier.classify(hand)

            for i, landmark in enumerate(hand):

                # Convert normalized coordinates
                # to pixels

                x = int(
                    landmark.x * frame.shape[1]
                )

                y = int(
                    landmark.y * frame.shape[0]
                )

                # Draw point
                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (0, 255, 0),
                    -1
                )

                # Landmark number
                cv2.putText(
                    frame,
                    str(i),
                    (x + 5, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    1
                )
            cv2.putText(
            frame,
            gesture,
            (50, 70),
            cv2.FONT_HERSHEY_SIMPLEX,
            2,
            (0, 255, 0),
            3
)


    # DISPLAY

    cv2.imshow(
        "Reconocimiento de gestos",
        frame
    )


    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break



# CLOSE

cap.release()
cv2.destroyAllWindows()