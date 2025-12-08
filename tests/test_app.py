import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(root / "src"))

from app import *

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(-3, 7) == 4

def test_add3():
    assert add(0, 0) == 0


def test_sub():
    assert sub(10, 3) == 7

def test_sub2():
    assert sub(-5, -5) == 0

def test_sub3():
    assert sub(3, 10) == -7


def test_mul():
    assert mul(4, 5) == 20

def test_mul2():
    assert mul(-3, 6) == -18

def test_mul3():
    assert mul(0, 99) == 0


def test_div():
    assert div(10, 2) == 5

def test_div2():
    assert div(-9, 3) == -3

def test_div3():
    assert div(5, 2) == 2.5


def test_sqrt():
    assert sqrt(25) == 5

def test_sqrt2():
    assert sqrt(0) == 0

def test_sqrt3():
    assert math.isclose(sqrt(2), math.sqrt(2))


def test_percent():
    assert percent(50, 10) == 5

def test_percent2():
    assert percent(200, 25) == 50

def test_percent3():
    assert percent(0, 100) == 0


def test_log():
    assert log(1) == 0

def test_log2():
    assert math.isclose(log(math.e), 1)

def test_log3():
    assert log(10) == math.log(10)


def test_sin():
    assert math.isclose(sin(0), 0)

def test_sin2():
    assert math.isclose(sin(math.pi/2), 1)

def test_sin3():
    assert math.isclose(sin(math.pi), 0, abs_tol=1e-9)


def test_cos():
    assert math.isclose(cos(0), 1)

def test_cos2():
    assert math.isclose(cos(math.pi), -1)

def test_cos3():
    assert math.isclose(cos(math.pi/2), 0, abs_tol=1e-9)


def test_tan():
    assert math.isclose(tan(0), 0)

def test_tan2():
    assert math.isclose(tan(math.pi/4), 1)

def test_tan3():
    assert math.isclose(tan(-math.pi/4), -1)


def test_square():
    assert square(5) == 25

def test_square2():
    assert square(-4) == 16

def test_square3():
    assert square(0) == 0


def test_cube():
    assert cube(3) == 27

def test_cube2():
    assert cube(-2) == -8

def test_cube3():
    assert cube(0) == 0
