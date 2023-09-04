import pytest

from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    dish1 = Dish("Lasanha", 20.0)
    assert dish1.name == "Lasanha"

    with pytest.raises(TypeError):
        Dish("Lasanha", "20.0")

    with pytest.raises(ValueError):
        Dish("Lasanha", -20.0)

    dish2 = Dish("Lasanha", 20.0)

    assert hash(dish1) == hash(dish2)
    assert dish1 == dish2

    dish3 = Dish("Pizza", 25.0)

    assert hash(dish1) != hash(dish3)
    assert dish1 != dish3

    assert repr(dish1) == "Dish('Lasanha', R$20.00)"

    ingredient = Ingredient("queijo mussarela")

    dish1.add_ingredient_dependency(ingredient, 2)
    assert dish1.recipe.get(ingredient) == 2

    expected_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    assert dish1.get_restrictions() == expected_restrictions

    assert dish1.get_ingredients() == {ingredient}
