import cv2

from hand_detector import HandDetector
from classifier import Classifier


# CREATE DETECTOR AND CLASSIFIER

detector = HandDetector()
classifier = Classifier()


# OPEN CAMERA

cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print("Could not open the camera")
    exit()


# LOOP

while True:

    success, frame = cap.read()

    if not success:

        print("Could not read the camera")
        break


    # MIRROR EFFECT

    frame = cv2.flip(frame, 1)


    # OPENCV USES BGR
    # MEDIAPIPE REQUIRES RGB

    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )


    # DETECT HAND

    hands, handedness = detector.detect(rgb_frame)

    # PROCESS HAND

    if hands:

        for index, hand in enumerate(hands):

            # Get whether the hand is Left or Right
            hand_type = handedness[index][0].category_name

            # CLASSIFY GESTURE

            gesture = classifier.classify(
                hand,
                hand_type
            )

            # DRAW LANDMARKS

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


                # Draw landmark number

                cv2.putText(
                    frame,
                    str(i),
                    (x + 5, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 255, 255),
                    1
                )

            # DISPLAY GESTURE

            cv2.putText(
                frame,
                gesture,
                (50, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                2,
                (0, 255, 0),
                3
            )

            # DISPLAY HAND TYPE

            cv2.putText(
                frame,
                hand_type,
                (50, 110),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 255, 255),
                2
            )


    # DISPLAY

    cv2.imshow(
        "Gesture Recognition",
        frame
    )


    # PRESS Q TO EXIT

    if cv2.waitKey(1) & 0xFF == ord("q"):

        break


# CLOSE

cap.release()
cv2.destroyAllWindows()