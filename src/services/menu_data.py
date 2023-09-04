import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        with open(source_path, encoding="utf-8") as file:
            menu_reader = csv.DictReader(file)

            for row in menu_reader:
                name = row["dish"]
                price = float(row["price"])
                ingredient_name = row["ingredient"]
                quantity = int(row["recipe_amount"])

                dish = self._find_or_create_dish(name, price)
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, quantity)

    def _find_or_create_dish(self, name: str, price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == name:
                return dish

        dish = Dish(name, price)
        self.dishes.add(dish)
        return dish
