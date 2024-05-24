import pytest
from bun import Bun
from burger import Burger
from data import NameOfIngridients


@pytest.fixture
def kratornaya_bulka():
    name = NameOfIngridients.BUN_ONE
    price = NameOfIngridients.PRICE_BUN
    return Bun(name, price)


@pytest.fixture
def cosmic_burger():
    return Burger()