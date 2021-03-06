from Base_container import Base_container


class Stack(Base_container):

    def __init__(self):
        super().__init__()
        self.__valid = False

        pass

    def __str__(self):
        if len(self._Base_container__content)>5:
            print("...")
            for item in self._Base_container__content[-5:]:
                print(item)
        else:
            for item in self._Base_container__content:
                print(item)
        return "\n"

    def check_top(self):
        invalid = ['2', '3', '4', 'J', 'Q', 'A']
        for value in invalid:
            if self.content[-1].value == value:
                return
        if self.content[-1].value == 'K' and (self.content[-1].suit == '♥' or self.content[-1].suit == '♠'):
            return
        self.__valid = True

    @property
    def valid(self):
        return self.__valid


