str_inpt = input("Item: ").strip().lower()
Fruits = {"apple":130,"avocado":50,"banana":110,"cantaloupe":50,"grapefruit":60,"grapes":90,
          "honeydew melon":50,"kiwifruit":90,"lemon":15,"lime":20,"nectarine":60,"pear":100,"sweet cherries":100}
for k in Fruits:
    if str_inpt == k:
        print(f"Calories: {Fruits[k]}")
