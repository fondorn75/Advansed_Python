# Задание 5
# Создайте три (или более) отдельных классов животных
# Например, рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.


class fish:
    def __init__(self, name: str, head: str, body: str, tail: str, fins: str):
        self.name = name
        self.head = head
        self.body = body
        self.tail = tail
        self.fins = fins

    def swim(self):
        return "i can swim!"


class birds:
    def __init__(self, name: str, beak: str, wings: str, feathers: str, color: str):
        self.name = name
        self.beak = beak
        self.wings = wings
        self.feathers = feathers
        self.color = color

    def fly(self):
        return "i can fly!"


class dogs:
    def __init__(self, name: str, breed: str, weight: int, height: int, color: str):
        self.name = name
        self.breed = breed
        self.weight = weight
        self.height = height
        self.color = color

    def bark(self):
        return "I can bark!"


if __name__ == '__main__':
    dog = dogs('Шарик', 'Дворняжка', 40, 300, 'Коричневый')
    print(f'{dog.name = }, {dog.color = }, {dog.breed = }, {dog.weight = } kg, {dog.height = } mm')
    print(dog.bark())
