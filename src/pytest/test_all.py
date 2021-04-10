import pytest
import area as a
import circumference as c
from math import pi
@pytest.mark.circle
@pytest.mark.parametrize('myinput, myref',
                         [(1, pi),
                          (0, 0),
                          (2.1, pi * 2.1**2),
                          (-5, pytest.raises(ValueError)),
                          ])
def circle_area_tester(myinput,myref):
    """Test values of circle area again reference values of r >= 0, and r < 0."""
    print(myinput)
    assert a.area_circle(myinput) == myref
@pytest.mark.square
@pytest.mark.parametrize('myinput, myref',
                         [(1, 1),
                          (0, 0),
                          (2.1, 2.1**2),
                          (-5, pytest.raises(ValueError)),
                          ])
def square_area_tester(myinput,myref):
    """Test values of square area again reference values of r >= 0, and r < 0."""
    print(myinput)
    assert a.area_square(myinput) == myref