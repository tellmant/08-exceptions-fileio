import unittest

import pytest

from main import *


class MyTestCase(unittest.TestCase):

    # unittest of problem 1
    def test_smallest_factor(self):
        self.assertEqual(smallest_factor(1), 1)
        # possible error (function will return 1)
        self.assertEqual(smallest_factor(25), 5)
        self.assertEqual(smallest_factor(11), 11)
        self.assertEqual(smallest_factor(15), 3)
        self.assertEqual(smallest_factor(7), 7)
        self.assertEqual(smallest_factor(9), 3)
        self.assertEqual(smallest_factor(2), 2)
        assert smallest_factor(13) == 13
        assert smallest_factor(1) == 1
        assert smallest_factor(24) == 2
        # possible error (function will return 1)
        assert smallest_factor(25) == 5

    # unittest of problem 2
    def test_month_length(self):
        self.assertEqual(month_length("January"), 31)
        self.assertEqual(month_length("February", True), 29)
        self.assertEqual(month_length("February", False), 28)
        self.assertEqual(month_length("March"), 31)
        self.assertEqual(month_length("April"), 30)
        self.assertEqual(month_length("May"), 31)
        self.assertEqual(month_length("June"), 30)
        self.assertEqual(month_length("July"), 31)
        self.assertEqual(month_length("August"), 31)
        self.assertEqual(month_length("September"), 30)
        self.assertEqual(month_length("October"), 31)
        self.assertEqual(month_length("November"), 30)
        self.assertEqual(month_length("December"), 31)
        self.assertEqual(month_length("undefined"), None)

    # unittest of problem 3
    def test_operate(self):
        self.assertEqual(operate(1, 2, '+'), 3)
        self.assertEqual(operate(1, 2, '-'), -1)
        self.assertEqual(operate(1, 2, '*'), 2)
        self.assertEqual(operate(1, 2, '/'), 0.5)

        with pytest.raises(TypeError) as excinfo:
            operate(1, 2, 3)
        assert excinfo.value.args[0] == "oper must be a string"

        with pytest.raises(ValueError) as excinfo:
            operate(1, 2, 'a')
        assert excinfo.value.args[0] == "oper must be one of '+', '/', '-', or '*'"

        with pytest.raises(ValueError) as excinfo:
            operate(1, 0, '/')
        assert excinfo.value.args[0] == "division by zero is undefined"

    # unittest of problem 5
    def test_count_sets(self):
        assert count_sets(['1RGf', '2BSs', '3PHf']) == 1
        assert count_sets(['2PSs', '3RSs', '1GOs']) == 1
        assert count_sets(['1RGf', '2RSf', '3POs']) == 0
        assert count_sets(['1GOs', '2GSs', '3PHf', '2POe']) == 0
        assert count_sets(['2POe', '1GOs', '2PSs', '3POe']) == 0
        assert count_sets(['3POs', '1GOs', '2POe', '3POs']) == 0

    def test_is_set(self):
        assert is_set('1RGf', '2BSs', '3PHf') == True
        assert is_set('1RGf', '2RSf', '3POs') == False
        assert is_set('1111', '2222', '3333') == True
        assert is_set('1234', '1234', '1234') == True
        assert is_set('1012', '1122', '1020') == False


# unittest of problem 4
@pytest.fixture
def set_up_fractions():
    frac_1_3 = Fraction(1, 3)
    frac_1_2 = Fraction(1, 2)
    frac_n2_3 = Fraction(-2, 3)
    return frac_1_3, frac_1_2, frac_n2_3


def test_fraction_init(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3.numer == 1
    assert frac_1_2.denom == 2
    assert frac_n2_3.numer == -2
    frac = Fraction(30, 42)
    assert frac.numer == 5
    assert frac.denom == 7
    with pytest.raises(ValueError) as excinfo:
        Fraction(1, 0)
    assert excinfo.value.args[0] == "denominator cannot be zero"
    with pytest.raises(TypeError) as excinfo:
        Fraction(1.5, 3)
    assert excinfo.value.args[0] == "numerator and denominator must be integers"


def test_fraction_str(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert str(frac_1_3) == "1 / 3"
    assert str(frac_1_2) == "1 / 2"
    assert str(frac_n2_3) == "-2 / 3"
    assert str(Fraction(2, 1)) == "2"


def test_fraction_float(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert float(frac_1_3) == 1 / 3
    assert float(frac_1_2) == .5
    assert float(frac_n2_3) == -2 / 3


def test_fraction_eq(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 == Fraction(1, 2)
    assert frac_1_3 == Fraction(2, 6)
    assert frac_n2_3 == Fraction(8, -12)
    assert frac_1_2 == 0.5


def test_fraction_add(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3 + frac_1_2 == Fraction(7, 6)


def test_fraction_sub(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 - frac_1_3 == Fraction(-5, 6)


def test_fraction_mul(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3 * frac_1_2 == Fraction(1, 6)


def test_fraction_true_div(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 / frac_1_3 == Fraction(3, 2)
    with pytest.raises(ZeroDivisionError) as excinfo:
        frac_1_2 / Fraction(0, 1)
    assert excinfo.value.args[0] == "cannot divide by zero"
