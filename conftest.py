import pytest
import bun
from burger import Burger


@pytest.fixture
def kratornaya_bulka():
    name = 'Краторная булка N-200i'
    price = 1255
    return bun.Bun(name, price)


@pytest.fixture
def cosmic_burger():
    return Burger()