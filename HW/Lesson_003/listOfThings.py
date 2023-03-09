# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

listOfThings = {"water": 3,
                "products": 5,
                "sleepingBag": 2,
                "rug": 1,
                "dishes": 2,
                "fuel": 3,
                "kitchenUtensils": 3,
                "tent": 5,
                "documentation": 0.2,
                "firstAidKit": 1,
                "washAccessories": 0.5}

volumeOfBackpack = int(input("Введите объем рюкзака: "))

result = 0
for i in listOfThings:
    if result < volumeOfBackpack:
        result += listOfThings[i]
        print(f"{i} : {listOfThings[i]}")
    else:
        break


print(f"Грузоподъемность рюкзака: {volumeOfBackpack}, вы сможете взять {result}")
