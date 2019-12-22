import pytest
from mycalc import __version__
from mycalc.calc import plus


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.parametrize('a,b,ans', [
    (1, 2, 3),
    (5, 6, 11),
    (-1, 5, 4),
    (-3, -5, -8)
])
def test_plus(a, b, ans):
    assert plus(a, b) == ans
