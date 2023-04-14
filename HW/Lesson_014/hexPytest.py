import pytest
from hexametric import hexCreation


def test_Hexametric():
    assert hexCreation(154)
    assert hexCreation(235)


def test_TypeError():
    with pytest.raises(TypeError):
        hexCreation('154')


if __name__ == '__main__':
    pytest.main(['-v'])
