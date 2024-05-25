import pytest
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from database import Database
from data import NameOfIngridients

@pytest.fixture
def kratornaya_bulka():
    name = NameOfIngridients.BUN_ONE
    price = NameOfIngridients.PRICE_BUN
    return Bun(name, price)


@pytest.fixture
def cosmic_burger():
    return Burger()


@pytest.fixture
def space_ingredient():
    ingredient_type = NameOfIngridients.TYPE_ONE
    ingredient_name = NameOfIngridients.NAME_ONE
    ingredient_price = NameOfIngridients.PRICE_ONE
    return Ingredient(ingredient_type, ingredient_name, ingredient_price)

@pytest.fixture
def data_base():
    return Database()

