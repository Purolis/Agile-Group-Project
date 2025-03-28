import array


class Dealer:
    __hand_value = None
    __hand = []

    def __init__(self, hand, hand_value):
        self.set_hand(hand)
        self.set_hand_value(hand_value)

    def draw(self, card):
        self.__hand.append(card)
        return self.__hand

    def count_hand(self):
        self.set_hand_value(0)
        for card in self.get_hand():
            self.set_hand_value(card.get_value() + self.get_hand_value())

        if self.__hand_value > 21:
            for card in self.get_hand():
                if card.get_value() == 11:
                    self.set_hand_value(self.get_hand_value() - 10) # DEBUG:: unsure about this bit

        return self.__hand_value

    def get_hand(self):
        return self.__hand

    def get_hand_value(self):
        return self.__hand_value

    def set_hand(self, hand):
        try:
            enumerate(hand)
        except Exception as err:
            print("DEBUG:ERROR:: BaseException: set_hand() error\n\ttype(hand) might not be iterable.")
            raise
        else:
            self.__hand = hand


    def set_hand_value(self, hand_value):
        try:
            hand_value = int(hand_value)
        except TypeError:
            print("DEBUG:ERROR:: set_hand_value() error.\n\tArgument for hand value is NAN.")
            raise
        except Exception as err:
            print("DEBUG:ERROR:: Unhandled BaseException...")
            raise
        else:
            self.__hand_value = hand_value
