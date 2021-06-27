class MoneyClassError(Exception):
    def __int__(self,x, message):
        super().__init__(self)
        self.__x=x
        self.__message=message
    def __repr__(self):
        return "{}, error is {}".format(self.__message, self.__x)


class Money:
    def __init__(self, amount, currency):
        self.__amount = amount
        self.__currency = currency

    def get_amount(self):
        return self.__amount

    def set_amount(self, x):
        self.__amount = x


    def get_currency(self):
        return self.__currency

    def set_currency(self, x):
        self.__currency = x


    def __repr__(self):
        return "{}-{}".format(self.__amount, self.__currency)

    def __add__(self, other):
        self.__amount += other.__amount
        return Money(self.__amount, self.__currency)

    def __sub__(self, other):
        self.__amount -= other.__amount
        return Money(self.__amount, self.__currency)


def main():
    a = Money(1000, "USD")
    b = Money(3000, "USD")
    # print(a + b)
    # print(a - b)
    print(a.set_currency(5))
    a.set_amount(-5)
    # print(type(a))


main()