from unittest.mock import Mock
from data import NameOfIngridients
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        mock_bun = Mock()
        cosmic_burger = Burger()
        cosmic_burger.set_buns(mock_bun)
        assert cosmic_burger.bun == mock_bun


    def test_add_ingredient(self):
        mock_ingredient = Mock()
        cosmic_burger = Burger()
        mock_ingredient.type = NameOfIngridients.TYPE_ONE
        mock_ingredient.name = NameOfIngridients.NAME_ONE
        mock_ingredient.price = NameOfIngridients.PRICE_ONE
        cosmic_burger.add_ingredient(mock_ingredient)
        assert len(cosmic_burger.ingredients) == 1
        assert cosmic_burger.ingredients[0] == mock_ingredient
        assert cosmic_burger.ingredients[0].type == NameOfIngridients.TYPE_ONE
        assert cosmic_burger.ingredients[0].name == NameOfIngridients.NAME_ONE
        assert cosmic_burger.ingredients[0].price == NameOfIngridients.PRICE_ONE


    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        cosmic_burger = Burger()
        mock_ingredient.type = NameOfIngridients.TYPE_ONE
        mock_ingredient.name = NameOfIngridients.NAME_ONE
        mock_ingredient.price = NameOfIngridients.PRICE_ONE
        cosmic_burger.add_ingredient(mock_ingredient)
        cosmic_burger.remove_ingredient(0)
        assert len(cosmic_burger.ingredients) == 0


    def test_move_ingredient(self):
        cosmic_burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient_2 = Mock()
        mock_ingredient.type = NameOfIngridients.TYPE_ONE
        mock_ingredient_2.type = NameOfIngridients.TYPE_TWO
        mock_ingredient.name = NameOfIngridients.NAME_ONE
        mock_ingredient_2.name = NameOfIngridients.NAME_TWO
        mock_ingredient.price = NameOfIngridients.PRICE_ONE
        mock_ingredient_2.price = NameOfIngridients.PRICE_TWO
        cosmic_burger.add_ingredient(mock_ingredient)
        cosmic_burger.add_ingredient(mock_ingredient_2)
        cosmic_burger.move_ingredient(0, 1)
        assert len(cosmic_burger.ingredients) == 2
        assert cosmic_burger.ingredients[0].type == NameOfIngridients.TYPE_TWO
        assert cosmic_burger.ingredients[0].name == NameOfIngridients.NAME_TWO
        assert cosmic_burger.ingredients[0].price == NameOfIngridients.PRICE_TWO
        assert cosmic_burger.ingredients[1].type == NameOfIngridients.TYPE_ONE
        assert cosmic_burger.ingredients[1].name == NameOfIngridients.NAME_ONE
        assert cosmic_burger.ingredients[1].price == NameOfIngridients.PRICE_ONE


    def test_get_price(self):
        cosmic_burger = Burger()
        mock_bun = Mock()
        mock_bun.get_price.return_value = 1255
        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 490
        cosmic_burger.bun = mock_bun
        cosmic_burger.ingredients = [mock_ingredient]
        assert cosmic_burger.get_price() == 1255 * 2 + 490


    def test_get_receipt(self):
        cosmic_burger = Burger()
        mock_bun = Mock()
        mock_bun.get_name.return_value = NameOfIngridients.BUN_ONE
        mock_ingredient = Mock()
        mock_ingredient.get_type.return_value = NameOfIngridients.TYPE_TWO
        mock_ingredient.get_name.return_value = NameOfIngridients.NAME_TWO
        mock_bun.get_price.return_value = 500
        mock_ingredient.get_price.return_value = 1500
        cosmic_burger.bun = mock_bun
        cosmic_burger.ingredients = [mock_ingredient]
        expected_receipt = '(==== Краторная булка N-200i ====)\n= начинка Сыр с астероидной плесенью =\n(==== Краторная булка N-200i ====)\n\nPrice: 2500'
        assert cosmic_burger.get_receipt() == expected_receipt

