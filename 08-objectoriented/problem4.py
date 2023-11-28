import numpy as np


class ComplexNumber:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def conjugate(self):
        return ComplexNumber(self.real, -self.imag)

    def __abs__(self):
        return np.sqrt(self.real ** 2 + self.imag ** 2)

    def __eq__(self, other):
        return (self.real == other.real) and (self.imag == other.imag)

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        real = self.real * other.real + self.imag * other.imag
        imag = -self.real * other.imag + self.imag * other.real
        d = other.real ** 2 + other.imag ** 2

        return ComplexNumber(real / d, imag / d)

    def __str__(self):
        if self.imag >= 0:
            return "(" + str(self.real) + "+" + str(self.imag) + "j)"
        else:
            return "(" + str(self.real) + "-" + str(-self.imag) + "j)"


def test_ComplexNumber(a, b):
    py_cnum, my_cnum = complex(a, b), ComplexNumber(a, b)

    if my_cnum.real != a or my_cnum.imag != b:
        print("__init__() set self.real or self.imag incorrectly")

    if py_cnum.conjugate().imag != my_cnum.conjugate().imag:
        print("conjugate() failed for", py_cnum)

    if str(py_cnum) != str(my_cnum):
        print("__str__() failed for", py_cnum)

    if abs(py_cnum) != abs(my_cnum):
        print("__abs__() failed for", py_cnum)

    if py_cnum + py_cnum != my_cnum + my_cnum:
        print("__add__() failed for", py_cnum)

    if py_cnum - py_cnum != my_cnum - my_cnum:
        print("__sub__() failed for", py_cnum)

    if py_cnum * py_cnum != my_cnum * my_cnum:
        print("__mul__() failed for", py_cnum)

    if py_cnum / py_cnum != my_cnum / my_cnum:
        print("__truediv__() failed for", py_cnum)

    if (py_cnum != py_cnum) and (my_cnum != my_cnum):
        print("__eq__() failed for", py_cnum)

    if py_cnum != py_cnum != (my_cnum != my_cnum):
        print("__ne__() failed for", py_cnum)

    print("Tests finished.")


test_ComplexNumber(3, 4)
test_ComplexNumber(3, -4)