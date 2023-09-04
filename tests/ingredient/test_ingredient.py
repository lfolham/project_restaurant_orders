from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("bacon")

    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient2)
    assert ingredient1 != ingredient2
    assert repr(ingredient1) != "Ingredient('mussarela')"
    assert ingredient1.name != "queijo mussarela"

    incorrect_restrictions = {Restriction.LACTOSE}
    assert ingredient1.restrictions == incorrect_restrictions
