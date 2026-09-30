class Classifier:

    def __init__(self):
        pass


    def get_raised_fingers(self, hand):

        finger_states = []

        # INDEX FINGER

        if hand[8].y < hand[6].y:
            finger_states.append(1)
        else:
            finger_states.append(0)


        # MIDDLE FINGER

        if hand[12].y < hand[10].y:
            finger_states.append(1)
        else:
            finger_states.append(0)



        # RING FINGER

        if hand[16].y < hand[14].y:
            finger_states.append(1)
        else:
            finger_states.append(0)


        # LITTLE FINGER

        if hand[20].y < hand[18].y:
            finger_states.append(1)
        else:
            finger_states.append(0)


        return finger_states


    def classify(self, hand):

        finger_states = self.get_raised_fingers(hand)

        # GESTURES

        if finger_states == [0, 0, 0, 0]:
            return "FIST"

        elif finger_states == [1, 0, 0, 0]:
            return "ONE"

        elif finger_states == [1, 1, 0, 0]:
            return "TWO"

        elif finger_states == [1, 1, 1, 0]:
            return "THREE"

        elif finger_states == [1, 1, 1, 1]:
            return "FOUR"

        else:
            return "UNKNOWN"