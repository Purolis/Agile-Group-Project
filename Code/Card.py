class Card:
    __suite = None
    __val = None

# --- CONSTRUCTORS -----------------------------------------------
    def __init__(self, suite, val):
        self.set_suite(suite)
        self.set_val(val)

# --- GETTERS -----------------------------------------------
    def get_human_suite(self):
        output = None
        if self.get_suite() == 0:
            output = "Hearts"
        elif self.get_suite() == 1:
            output = "Spades"
        elif self.get_suite() == 2:
            output = "Clubs"
        else:
            output = "Diamonds"
        return output

    def get_human_value(self):
        output = "None"
        if self.get_val() == 1:
            output = "Ace"
        elif self.get_val() == 11:
            output = "Ace"
        elif self.get_val() == 12:
            output = "Queen"
        elif self.get_val() == 13:
            output = "King"
        else:
            output = str(self.get_val())
        return output

    def get_suite(self):
        return self.__suite

    def get_val(self):
        return self.__val

# --- SETTERS -----------------------------------------------
    def set_suite(self, suite):
        try:
            self.__suite = int(suite) % 4
        except ValueError as exc:
            print("Value error in Suite")

    def set_val(self, val):
        try:
            self.__val = (int(val) % 13)
        except ValueError as exc:
            print("Value Error in val")

#--- TO_STRING -----------------------------------------------
    def __str__(self):
        return str(self.get_human_value()) + " of " + str(self.get_human_suite())




