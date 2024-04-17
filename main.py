# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
#
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы,
# если требуется (например, различный звук для `make_sound()`).
#
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
#
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
# о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
#
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут
# иметь специфические методы (например, `feed_animal()` для `ZooKeeper`
# и `heal_animal()` для `Veterinarian`).
#
# Дополнительно:
#
# Попробуйте добавить дополнительные функции в вашу программу, такие как
# сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('Животное кричит')

    def eat(self):
        print('Животное ест')


class Bird(Animal):
    def __init__(self, name, age, feathers, sound='Чирик'):
        super().__init__(name, age)
        self.feathers = feathers
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def eat(self):
        print('Птица клюет')

    def fly(self):
        print('Птица летает')


class Mammal(Animal):
    def __init__(self, name, age, fur, sound='Р-р-р'):
        super().__init__(name, age)
        self.fur = fur
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def eat(self):
        print('Млекопитающее ест')

    def walk(self):
        print('Млекопитающее идет')


class Reptile(Animal):
    def __init__(self, name, age, scales, sound='Ш-ш-ш'):
        super().__init__(name, age)
        self.scales = scales
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def eat(self):
        print('Рептилия глотает еду')

    def crawl(self):
        print('Рептилия ползет')


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


animals_list = [Bird('орел', 6, 'коричневый', 'SQUEAK'),
                Mammal('медведь', 12, 'белый'),
                Reptile('питон', 27, 'желтый')]

animal_sound(animals_list)

