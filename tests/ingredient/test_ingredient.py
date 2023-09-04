from src.models.ingredient import (
    Ingredient,
    restriction_map,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo gorgonzola")

    assert hash(ingredient1) == hash(ingredient1)
    assert hash(ingredient1) != hash(ingredient2)
    assert ingredient1 == ingredient1
    assert ingredient1 != ingredient2
    assert repr(ingredient1) == "Ingredient('queijo mussarela')"
    assert ingredient1.name == "queijo mussarela"
    correct_restrictions = restriction_map().get("queijo mussarela", set())
    assert ingredient1.restrictions == correct_restrictions
