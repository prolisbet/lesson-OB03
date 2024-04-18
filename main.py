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
        print(f'{self.name} кричит')

    def eat(self):
        print(f'{self.name} ест')


class Bird(Animal):
    def __init__(self, name, age, cover, sound='Чирик'):
        super().__init__(name, age)
        self.cover = cover
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def fly(self):
        print(f'{self.name} летает')


class Mammal(Animal):
    def __init__(self, name, age, cover, sound='Р-р-р'):
        super().__init__(name, age)
        self.cover = cover
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def walk(self):
        print(f'{self.name} идет')


class Reptile(Animal):
    def __init__(self, name, age, cover, sound='Ш-ш-ш'):
        super().__init__(name, age)
        self.cover = cover
        self.sound = sound

    def make_sound(self):
        print(self.sound)

    def crawl(self):
        print(f'{self.name} ползет')


class Zoo():
    def __init__(self):
        self.animals_list = []
        self.employees_list = []

    def add_animal(self, animal, name, age, cover, sound):
        if animal.lower() == 'птица' or 'млекопитающее' or 'рептилия':
            if animal.lower() == 'птица':
                new_animal = Bird(name, age, cover, sound)
            elif animal.lower() == 'млекопитающее':
                new_animal = Mammal(name, age, cover, sound)
            else:
                new_animal = Reptile(name, age, cover, sound)
            self.animals_list.append(new_animal)
            return new_animal
        else:
            return 'Введено не верное животное'

    def add_employee(self, name, age, job):
        if job.lower() == 'смотритель зоопарка' or 'ветеринар':
            if job.lower() == 'смотритель зоопарка':
                new_employee = ZooKeeper(name, age)
            else:
                new_employee = Veterinarian(name, age)
            self.employees_list.append(new_employee)
            return new_employee
        else:
            return 'Введена не верная должность'

    def info_zoo_animals(self):
        print('Список животных в зоопарке:')
        for i, animal in enumerate(self.animals_list, start=1):
            print(f'{i}. {animal.name}, '
                  f'возраст - {animal.age}, '
                  f'покров - {animal.cover}, '
                  f'звук - {animal.sound}' )
        print()

    

    def info_zoo_employees(self):
        print('Список сотрудников в зоопарке:')
        for i, employee in enumerate(self.employees_list, start=1):
            print(f'{i}. {employee.name}, '
                  f'возраст - {employee.age}, '
                  f'должность - {employee.job}')
        print()

class ZooKeeper():
    def __init__(self, name, age, job='смотритель зоопарка'):
        self.name = name
        self.age = age
        self.job = job

    def feed_animal(self, animal):
        print(f'{self.name} кормит животное {animal.name}')


class Veterinarian():
    def __init__(self, name, age, job='ветеринар'):
        self.name = name
        self.age = age
        self.job = job

    def heal_animal(self, animal):
        print(f'{self.name} лечит животное {animal.name}')


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
    print()


animals_list1 = [Bird('орел', 6, 'коричневые перья', 'SQUEAK'),
                 Mammal('медведь', 12, 'белый мех'),
                 Reptile('питон', 27, 'желтая чешуя')]

animal_sound(animals_list1)

zoo1 = Zoo()

bird1 = zoo1.add_animal('птица', 'орел', 6, 'коричневые перья', 'SQUEAK')
mammal1 = zoo1.add_animal('млекопитающее', 'медведь', 12, 'белый мех', 'Р-р-р')
reptile1 = zoo1.add_animal('рептилия', 'питон', 27, 'желтая чешуя', 'Ш-ш-ш')

zookeeper1 = zoo1.add_employee('Роман', 29, 'смотритель зоопарка')
zookeeper2 = zoo1.add_employee('Ольга', 36, 'смотритель зоопарка')
vet1 = zoo1.add_employee('Афанасий', 42, 'ветеринар')

zoo1.info_zoo_animals()
zoo1.info_zoo_employees()

mammal1.make_sound()
mammal1.walk()
mammal1.eat()

reptile1.make_sound()
reptile1.crawl()
reptile1.eat()

zookeeper2.feed_animal(mammal1)
vet1.heal_animal(bird1)