# Доработаем задачи 5.
# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animals:
    def __init__(self, name: str):
        self.name = name

    def printAnimals(self):
        return 'I am Animal!'


class Fishes(Animals):
    def __init__(self, name: str, head: str, body: str, tail: str, fins: bool):
        super().__init__(name)
        self.head = head
        self.body = body
        self.tail = tail
        self.fins = fins

    def swim(self):
        return "i can swim!"


class Birds(Animals):
    def __init__(self, name: str, beak: str, wings: str, feathers: str, color: str):
        super().__init__(name)
        self.beak = beak
        self.wings = wings
        self.feathers = feathers
        self.color = color

    def fly(self):
        return "i can fly!"


class Dogs(Animals):
    def __init__(self, name: str, breed: str, weight: int, height: int, color: str):
        super().__init__(name)
        self.breed = breed
        self.weight = weight
        self.height = height
        self.color = color

    def bark(self):
        return "I can bark!"


if __name__ == '__main__':
    fish = Fishes('Рыбка', 'Удлиненная', 'Узкое', 'Двойной', True)
    print(f'{fish.name = }, {fish.body = }, {fish.fins = }, {fish.tail = }, {fish.head = }')
    print(fish.swim())
    print(fish.printAnimals())
