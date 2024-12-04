from contents import pantry, recipes
from recipe_options import quantity

def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """
    Add an item and its required amount to the shopping list.

    If the item already exists in the shopping list, the function updates the amount
    by adding the new amount to the existing value. Otherwise, the item is added to the list.

    :param data: The shopping list where items will be added.
                 This is a list of dictionaries, where each dictionary represents an item
                 with keys for the item's name and the required amount.
    :type data: dict
    :param item: The name of the item to add to the shopping list.
    :type item: str
    :param amount: The amount of the item required.
    :type amount: int
    :return: None
    :rtype: None
    """
    if item in data:
        data[item] += amount
    else:
        data[item] = amount

# display_dict = {str(index + 1); meal for index, meal in enumerate(recipies)}
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)

for things in shopping_list.items():
    print(things)