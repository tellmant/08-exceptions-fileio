def smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n == 1: return 1
    # possible error (the range function in Python excludes the upper bound)
    # for i in range(2, int(n**.5)):
    for i in range(2, int(n ** .5) + 1):
        if n % i == 0: return i
    return n


def month_length(month, leap_year=False):
    """Return the number of days in the given month."""
    if month in {"September", "April", "June", "November"}:
        return 30
    elif month in {"January", "March", "May", "July", "August", "October", "December"}:
        return 31

    if month == "February":
        if not leap_year:
            return 28
        else:
            return 29
    else:
        return None


def operate(a, b, oper):
    """Apply an arithmetic operation to a and b."""
    if type(oper) is not str:
        raise TypeError("oper must be a string")
    elif oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        if b == 0:
            raise ValueError("division by zero is undefined")
        return a / b
    raise ValueError("oper must be one of '+', '/', '-', or '*'")


class Fraction(object):
    """Reduced fraction class with integer numerator and denominator."""

    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("denominator cannot be zero")
        elif type(numerator) is not int or type(denominator) is not int:
            raise TypeError("numerator and denominator must be integers")

        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        common_factor = gcd(numerator, denominator)
        self.numer = numerator // common_factor
        self.denom = denominator // common_factor

    def __str__(self):
        if self.denom != 1:
            return "{} / {}".format(self.numer, self.denom)
        else:
            return str(self.numer)

    def __float__(self):
        return self.numer / self.denom

    def __eq__(self, other):
        if type(other) is Fraction:
            return self.numer == other.numer and self.denom == other.denom
        else:
            return float(self) == other

    def __add__(self, other):
        return Fraction(self.numer * other.numer + self.denom * other.denom,
                        self.denom * other.denom)

    def __sub__(self, other):
        return Fraction(self.numer * other.numer - self.denom * other.denom,
                        self.denom * other.denom)

    def __mul__(self, other):
        return Fraction(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        if self.denom * other.numer == 0:
            raise ZeroDivisionError("cannot divide by zero")
        return Fraction(self.numer * other.denom, self.denom * other.numer)


# problem 6
def count_sets(cards):
    """Return the number of sets in the provided Set hand.

    Parameters
    ----------
    cards : list of str
        Each str represents a card.  The str encodes the
        count, color, shape, and filling of the card:
            first character: 1, 2, or 3
            second character: R, G, or P
            third character: o, s, or h
            fourth character: f, e, or s

    Returns
    -------
    count : int
        The number of sets in the hand.
    """
    def check_feature(feature, cards):
        features = [card[feature] for card in cards]
        return all_equal(features) or not any_equal(features)

    def all_equal(elements):
        return len(set(elements)) == 1

    def any_equal(elements):
        for i in range(len(elements) - 1):
            for j in range(i + 1, len(elements)):
                if elements[i] == elements[j]:
                    return True
        return False

    return sum(
        1 if check_feature(i, cards) else 0
        for i in range(4)
    ) // 3


def is_set(a, b, c):
    """Determine if the three cards make a valid set.

    Parameters
         a, b, c (str): string representation of 4-bit integers in base 3.
            For example, "1012", "1122", and "1020" (which is not a set).
    Returns:
        True if a, b, and c form a set, meaning the ith digit of a, ,b,
            and c are either the same or all different for i=1,2,3,4.
        False if a,b, and c do not form a set.
    """
    def check_feature(feature):
        return (a[feature] == b[feature] == c[feature]) or (a[feature] != b[feature] != c[feature])

    return all(check_feature(i) for i in range(4))