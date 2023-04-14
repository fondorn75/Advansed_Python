import pytest
from quadratic import quadraticEquation


def test_Quadratic():
    assert quadraticEquation(2, -5, -4)
    assert quadraticEquation(4, -2, -8)


def test_TypeError():
    with pytest.raises(TypeError):
        quadraticEquation(4, -2, '-8')


if __name__ == '__main__':
    pytest.main(['-v'])
