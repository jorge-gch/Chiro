import math


class Classifier:

    def __init__(self):
        pass


    def get_raised_fingers(self, hand, hand_type):

        fingers = []

        # -----------------------------------------
        # THUMB
        # -----------------------------------------

        if hand_type == "Right":

            if hand[4].x < hand[3].x:
                fingers.append(1)
            else:
                fingers.append(0)

        else:

            if hand[4].x > hand[3].x:
                fingers.append(1)
            else:
                fingers.append(0)


        # -----------------------------------------
        # INDEX
        # -----------------------------------------

        if hand[8].y < hand[6].y:
            fingers.append(1)
        else:
            fingers.append(0)


        # -----------------------------------------
        # MIDDLE
        # -----------------------------------------

        if hand[12].y < hand[10].y:
            fingers.append(1)
        else:
            fingers.append(0)


        # -----------------------------------------
        # RING
        # -----------------------------------------

        if hand[16].y < hand[14].y:
            fingers.append(1)
        else:
            fingers.append(0)


        # -----------------------------------------
        # PINKY
        # -----------------------------------------

        if hand[20].y < hand[18].y:
            fingers.append(1)
        else:
            fingers.append(0)


        return fingers


    def distance(self, point1, point2):

        dx = point1.x - point2.x
        dy = point1.y - point2.y

        return math.sqrt(
            dx ** 2 + dy ** 2
        )


    def classify(self, hand, hand_type):

        fingers = self.get_raised_fingers(
            hand,
            hand_type
        )


        # -----------------------------------------
        # OK 👌
        # -----------------------------------------

        thumb_index_distance = self.distance(
            hand[4],
            hand[8]
        )

        if thumb_index_distance < 0.07:

            return "OK"


        # -----------------------------------------
        # FIST ✊
        # -----------------------------------------

        if fingers == [0, 0, 0, 0, 0]:

            return "FIST"


        # -----------------------------------------
        # THUMBS UP 👍
        # -----------------------------------------

        if fingers == [1, 0, 0, 0, 0]:

            return "THUMBS UP"


        # -----------------------------------------
        # ONE ☝️
        # -----------------------------------------

        if fingers == [0, 1, 0, 0, 0]:

            return "ONE"


        # -----------------------------------------
        # TWO ✌️
        # -----------------------------------------

        if fingers == [0, 1, 1, 0, 0]:

            return "TWO"


        # -----------------------------------------
        # THREE
        # -----------------------------------------

        if fingers == [0, 1, 1, 1, 0]:

            return "THREE"


        # -----------------------------------------
        # ROCK 🤘
        # -----------------------------------------

        if fingers == [0, 1, 0, 0, 1]:

            return "ROCK"


        # -----------------------------------------
        # CALL ME 🤙
        # -----------------------------------------

        if fingers == [1, 0, 0, 0, 1]:

            return "CALL ME"


        # -----------------------------------------
        # OPEN HAND ✋
        # -----------------------------------------

        if fingers == [1, 1, 1, 1, 1]:

            return "OPEN HAND"


        return "UNKNOWN"