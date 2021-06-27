# Data members -
# numerator - integer(համարիչ)
# denumerator - integer(հայտարար)
#
# Data Methods
# Constructor - not only assign values to data member, but also simplify,
# For example if we have an object obj = Rational(6,8), should create an object with values (3,4). Use GCD algorithm, for simplifying.
import math
class NegativeNumberError(Exception):
    pass

class Rational:
    def __init__(self, x, y):
        x, y = self.normalization(x, y)
        self.nominator, self.denominator = x, y


    @staticmethod
    def gcd(a, b):
        x = 0
        for i in range(1, b + 1):
            if b % i == 0 and a % i == 0:
                x = i
        return x

    def normalization(self, x, y):
        z = self.gcd(x, y)
        return x // z, y // z

    def __repr__(self):
        return "{}-{}".format(self.nominator, self.denominator)

    def lcm(self, x, y):
        n = max(x, y)
        while True:
            if n % x == 0 and n % y == 0:
                lcm = n
                break
            n += 1
        return lcm

    def __add__(self, other):
        y = self.lcm(self.nominator, self.denominator)
        x = self.nominator * y // self.denominator + other.nominator * y // other.denominator
        return Rational(x, y)

    def __sub__(self, other):
        y = self.lcm(self.nominator, self.denominator)
        x = abs(self.nominator * y // self.denominator - other.nominator * y // other.denominator)
        return Rational(x, y)

    def __mul__(self, other):
        return Rational(self.nominator * other.nominator, self.denominator * other.denominator)

    def __truediv__(self, other):
        return Rational(self.nominator * other.denominator, self.denominator * other.nominator)

    def __eq__(self, other):
        y = self.lcm(self.nominator, self.denominator)
        if self.nominator * y / self.denominator == other.nominator * y / other.denominator:
            return True
        else:
            return False

    def __gt__(self, other):
        y = self.lcm(self.nominator, self.denominator)
        if self.nominator * y / self.denominator > other.nominator * y / other.denominator:
            return True
        else:
            return False

    def __ge__(self, other):
        y = self.lcm(self.nominator, self.denominator)
        if self.nominator * y / self.denominator >= other.nominator * y / other.denominator:
            return True
        else:
            return False

    def __lt__(self, other):
        y = self.lcm(self.nominator, self.denominator)
        if self.nominator * y / self.denominator < other.nominator * y / other.denominator:
            return True
        else:
            return False

    def __le__(self, other):
        y = self.lcm(self.nominator, self.denominator)
        if self.nominator * y / self.denominator <= other.nominator * y / other.denominator:
            return True
        else:
            return False

    def __pow__(self, p):
        return Rational(self.nominator ** p, self.denominator ** p)


r = Rational(-6,8)
r1 = Rational(1, 2)

print(r + r1)
print(r - r1)
print(r * r1)
print(r / r1)
print(r == r1)
print(r > r1)
print(r >= r1)
print(r < r1)
print(r <= r1)
print(r ** 5)