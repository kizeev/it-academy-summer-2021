"""Создайте  модель из жизни. Это может быть бронирование комнаты в отеле,
покупка билета в транспортной компании, или простая РПГ. Создайте несколько
объектов классов, которые описывают ситуацию. Объекты должны содержать как
атрибуты так и методы класса для симуляции различных действий. Программа должна
инстанцировать объекты и эмулировать какую-либо ситуацию - вызывать методы,
взаимодействие объектов и т.д.
"""

from random import choice


class Hero:
    """Класс для создания героя игры"""

    def __init__(self, name, strength=10):
        self.name = name
        self.__level = 1
        self.__health = 100
        self.strength = strength

    def __str__(self):
        return self.name

    def status_hero(self):
        """Показать характеристики героя"""
        return f'{self.name}: level {self.__level}, health {self.__health},' \
               f' strength {self.strength}'

    def move(self):
        """Перемещать героя"""
        print(f'{self.name} moves')

    def attack(self, target_hero, power_attack):
        """Атаковать другого героя"""
        if self.strength - power_attack < 0:
            print(f'{self.name} doesn\'t have so much strength')
        else:
            print(f'{self.name} attacks {target_hero}')
            self.strength -= power_attack
            target_hero.__health -= power_attack
            target_hero.__damage(self)

    def __damage(self, attacking_hero):
        """Оценить нанесенный урон.

        Если убил противника - уровень повышается"""
        if self.__health <= 0:
            print(f'{self.name} died.')
            attacking_hero.__up_level()

    def __up_level(self):
        """Повысить уровень героя с увеличением его силы"""
        self.__level += 1
        self.strength += 10
        print(f'{self.name} level up')


class Human(Hero):
    """Класс для создания Героя расы Люди.

    Герои расы Люди имееют повышенную силу"""

    race = "Human"

    def __init__(self, name, strength):
        Hero.__init__(self, name, strength)
        self.strength += 10
        self.artifact_of_strength = ['iron glove',
                                     'two-handed sword',
                                     'oak shield'
                                     ]

    def __getitem__(self):
        random_artefact = choice(self.artifact_of_strength)
        print(f'{self.name} gets {random_artefact}')


class Elf(Hero):
    """Класс для создания героя расы Эльфы.

    Герои расы Эльфы имеют магические способности, но слабее"""

    race = "Elf"

    def __init__(self, name, magic=10):
        Hero.__init__(self, name)
        self.strength -= 5
        self.magic = magic
        self.artifact_of_magic = ['moon ring',
                                  'staff of fate',
                                  'magician crown'
                                  ]

    def __getitem__(self):
        random_artefact = choice(self.artifact_of_magic)
        print(f'{self.name} gets {random_artefact}')

    def status_hero(self):
        """Показать характеристики магического героя"""
        return Hero.status_hero(self) + f', magic {self.magic}'

    def spell_sleep(self, target_hero):
        """Применить заклинание на противника"""
        if self.magic < 2:
            print(f'{self.name} doesn\'t have so much magic')
        else:
            self.magic -= 2
            print(f'{self.name} make magic. {target_hero} sleeps')


if __name__ == '__main__':
    artur = Human('King Artur', strength=40)
    legolas = Elf('Legolas')
    print(artur.status_hero())
    print(legolas.status_hero())
    artur.move()
    artur.attack(legolas, 5)
    legolas.spell_sleep(artur)
    mike = Human('St_Michail', strength=95)
    mike.attack(artur, 101)
    print(artur.status_hero())
    print(legolas.status_hero())
    print(mike.status_hero())
    mike.__getitem__()
    legolas.__getitem__()
