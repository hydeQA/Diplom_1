import pytest
from unittest.mock import Mock
from burger import Burger
from bun import Bun
from ingredient import Ingredient

class TestBurger:
    def test_set_buns(self, cosmic_burger):
        mock_bun = Mock(spec=Bun)
        cosmic_burger.set_buns(mock_bun)
        assert cosmic_burger.bun == mock_bun


    def test_add_ingredient(self, cosmic_burger):
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.type = 'Соус'
        mock_ingredient.name = 'Соус Spicy-X'
        mock_ingredient.price = 90
        cosmic_burger.add_ingredient(mock_ingredient)
        assert len(cosmic_burger.ingredients) == 1
        assert cosmic_burger.ingredients[0] == mock_ingredient
        assert cosmic_burger.ingredients[0].type == 'Соус'
        assert cosmic_burger.ingredients[0].name == 'Соус Spicy-X'
        assert cosmic_burger.ingredients[0].price == 90


