class Player:
    __hand_value = None
    __hand = []
    __player_wealth = None

    def __init__(self, hand, hand_value, wealth):
        self.set_hand(hand)
        self.set_hand_value(hand_value)
        self.set_player_wealth(wealth)

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

    def get_player_wealth(self):
        return self.__player_wealth

    def set_hand(self, hand):
        self.__hand = hand

    def set_hand_value(self, hand_value):
        self.__hand_value = hand_value

    def set_player_wealth(self, player_wealth):
        self.__player_wealth = player_wealth
