import mediapipe as mp

from mediapipe.tasks import python
from mediapipe.tasks.python import vision


class HandDetector:

    def __init__(self):

        # Model path
        base_options = python.BaseOptions(
            model_asset_path="models/hand_landmarker.task"
        )

        # Detector configuration
        options = vision.HandLandmarkerOptions(
            base_options=base_options,
            num_hands=1,
            min_hand_detection_confidence=0.5,
            min_hand_presence_confidence=0.5,
            min_tracking_confidence=0.5
        )

        # Create detector
        self.detector = vision.HandLandmarker.create_from_options(
            options
        )


    def detect(self, frame):

        """
        Receives an RGB image and returns
        the hand landmarks.
        """

        # Convert the OpenCV frame to a MediaPipe image
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=frame
        )

        # Detect
        result = self.detector.detect(mp_image)

        return result.hand_landmarks