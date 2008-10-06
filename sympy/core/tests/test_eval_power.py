from sympy.core import Rational, Symbol, Basic, S, Real, Integer
from sympy.functions.elementary.miscellaneous import sqrt

def test_rational():
    a = Rational(1, 5)

    assert a**Rational(1, 2) == a**Rational(1, 2)
    assert 2 * a**Rational(1, 2) == 2 * a**Rational(1, 2)

    assert a**Rational(3, 2) == a * a**Rational(1, 2)
    assert 2 * a**Rational(3, 2) == 2*a * a**Rational(1, 2)

    assert a**Rational(17, 3) == a**5 * a**Rational(2, 3)
    assert 2 * a**Rational(17, 3) == 2*a**5 * a**Rational(2, 3)

def test_large_rational():
    e = (Rational(123712**12-1,7)+Rational(1,7))**Rational(1,3)
    assert e == 234232585392159195136 * (Rational(1,7)**Rational(1,3))

def test_negative_real():
    def feq(a,b):
        return abs(a - b) < 1E-10

    assert feq(S.One / Real(-0.5), -Integer(2))

def test_expand():
    x = Symbol('x')
    assert (2**(-1-x)).expand() == Rational(1,2)*2**(-x)

def test_issue153():
    #test that is runs:
    a = sqrt(2*(1+sqrt(2)))

def test_issue350():
    #test if powers are simplified correctly
    #see also issue 896
    a = Symbol('a')
    assert ((a**Rational(1,3))**Rational(2)) == a**Rational(2,3)
    assert ((a**Rational(3))**Rational(2,5)) == (a**Rational(3))**Rational(2,5)

    a = Symbol('a', real=True)
    b = Symbol('b', real=True)
    assert (a**2)**b == abs(a)**(2*b)
    assert sqrt(1/a) != 1/sqrt(a)
    assert (a**3)**Rational(1,3) != a

    z = Symbol('z')
    k = Symbol('k',integer=True)
    m = Symbol('m',integer=True)
    assert (z**k)**m == z**(k*m)
    #assert Number(5)**Rational(2,3)==Number(25)**Rational(1,3)

    a = Symbol('a', positive=True)
    assert (a**3)**Rational(2,5) == a**Rational(6,5)

def test_issue767():
    assert --sqrt(sqrt(5)-1)==sqrt(sqrt(5)-1)
