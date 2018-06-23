"""
Tests for Rational numbers defined by the class.
"""

import numtheory.Rational

#############

# Test Data #

#############

A = Rational(1,2) #Half
B = Rational(1,3) #Third

A1 = Rational(-1,2)
A2 = Rational(1,-2)
A3 = Rational(-1,-2)

#####################

# Test Constructors #

#####################

def test_main_constructor():
    assert A.numerator / A.denominator == 0.5
    
    assert Rational(2) == Rational(2,1)

    # Ensure denominator always positive
    assert A.denominator > 0 and A1.denominator > 0 and A2.denominator > 0 and A3.denominator > 0
    
    flag = False
    try:
        err = Rational(1,0)
    except ValueError:
        flag = True

    assert flag == True

def test_from_str():
    assert Rational.from_str("1,2") == A



#################

# Test Equality #

#################


def test_eq():
    assert A == A
    assert Rational(2,1) == 2



###################

# Test operations #

###################

def test_addition():
    assert A + B == Rational(5,6)
    assert A + B == B + A
    assert 1 + A == Rational(3,2)
    assert A + 1 == 1 + A

def test_subtraction():
    assert A - B == Rational(1,6)
    assert A - 1 == Rational(-1,2)
    assert 1 - A == Rational(1,2)


def test_multiplication():
    assert A * B == Rational(1,6)
    assert B * A == A * B
    assert 2 * A == 1
    assert 2 * A == A * 2


def test_division():
    assert A / B == Rational(3,2)
    assert A / 2 == Rational(1,4)
    assert 2 / A == 1


def test_power():
    assert A ** 2 == Rational(1,4)
    assert A ** 0 == 1
    assert A ** -1 == 2
    assert A ** -3 == 8


def test_iadd():
    a = A
    a += B
    assert a == A + B


def test_isub():
    a = A
    a -= B
    assert a == A - B


def test_imul():
    a = A
    a *= B
    assert a == A * B


def test_idiv():
    a = A
    a /= B
    assert a == A / B


def test_ipow():
    a = A
    a *= 4
    assert a == Rational(1, 16)


