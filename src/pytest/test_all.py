import pytest
import sys
import os
sys.path.insert(0, os.path.abspath('./src'))
import area as a
import circumference as c
from math import pi


@pytest.mark.circle
@pytest.mark.parametrize('myinput, myref',
                         [(1, pi),
                          (0, 0),
                          (2.1, pi * 2.1**2),
                          ])
def test_circle_area(myinput,myref):
    """Test values of circle area against reference values of r >= 0, and r < 0."""
    print(myinput)
    assert a.area_circle(myinput) == myref


@pytest.mark.circle
def test_values1():
    """Make sure value errors are recognized for area_circle."""
    with pytest.raises(ValueError):
        a.area_circle(-5)


@pytest.mark.square
@pytest.mark.parametrize('myinput, myref',
                         [(1, 1),
                          (0, 0),
                          (2.1, 2.1**2),
                          ])
def test_square_area(myinput,myref):
    """Test values of square area against reference values of r >= 0, and r < 0."""
    print(myinput)
    assert a.area_square(myinput) == myref


@pytest.mark.square
def test_values2():
    """Make sure value errors are recognized for area_square."""
    with pytest.raises(ValueError):
        a.area_square(-5)


@pytest.mark.circle
@pytest.mark.parametrize('myinput, myref',
                         [(1, 2 * pi),
                          (0, 0),
                          (2.1, 2 * pi * 2.1),
                          ])
def test_circle_circumference(myinput,myref):
    """Test values of circle circumference against reference values of r >= 0, and r < 0."""
    print(myinput)
    assert c.circ_circle(myinput) == myref


@pytest.mark.circle
def test_values3():
    """Make sure value errors are recognized for area_circle."""
    with pytest.raises(ValueError):
        c.circ_circle(-5)


@pytest.mark.square
@pytest.mark.parametrize('myinput, myref',
                         [(1, 1 * 4),
                          (0, 0),
                          (2.1, 2.1 * 4),
                          ])
def test_square_circumference(myinput,myref):
    """Test values of square circumference against reference values of r >= 0, and r < 0."""
    print(myinput)
    assert c.circ_square(myinput) == myref


@pytest.mark.square
def test_values4():
    """Make sure value errors are recognized for area_square."""
    with pytest.raises(ValueError):
        c.circ_square(-5)
