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

    def __init__(self, name):
        self.name = name
        self.__level = 1
        self.__health = 100
        self._strength = 10

    def __str__(self):
        return self.name

    def status_hero(self):
        """Показать характеристики героя"""
        return f'{self.name}: level {self.__level}, health {self.__health},' \
               f' strength {self._strength}'

    def move(self):
        """Перемещать героя"""
        print(f'{self.name} moves')

    def attack(self, target_hero, power_attack):
        """Атаковать другого героя"""
        if self._strength - power_attack < 0:
            print(f'{self.name} doesn\'t have so much strength')
        else:
            print(f'{self.name} attacks {target_hero}')
            self._strength -= power_attack
            target_hero.__health -= power_attack
            target_hero.__damage(self)

    def __damage(self, attacking_hero):
        """Оценить нанесенный урон.

        Если убил противника - уровень повышается
        """

        if self.__health <= 0:
            print(f'{self.name} died.')
            attacking_hero.__up_level()

    def __up_level(self):
        """Повысить уровень героя с увеличением его силы"""
        self.__level += 1
        self._strength += 10
        print(f'{self.name} level up')


class Human(Hero):
    """Класс для создания Героя расы Люди.

    Герои расы Люди имееют повышенную силу
    """

    race = "Human"
    artifacts_of_strength = {
        'iron glove': 10,
        'two-handed sword': 15,
        'oak shield': 20
    }

    def __init__(self, name):
        Hero.__init__(self, name)
        random_artefact = choice(list(self.artifacts_of_strength.items()))
        print(f'{self.name} gets {random_artefact[0]}'
              f' and his strength increases by {random_artefact[1]}')
        self._strength = self._strength + 10 + int(random_artefact[1])


class Elf(Hero):
    """Класс для создания героя расы Эльфы.

    Герои расы Эльфы имеют магические способности, но слабее
    """

    race = "Elf"
    artifacts_of_magic = {
        'moon ring': 15,
        'staff of fate': 20,
        'magician crown': 25
    }

    def __init__(self, name):
        Hero.__init__(self, name)
        self._strength -= 5
        random_artefact = choice(list(self.artifacts_of_magic.items()))
        print(f'{self.name} gets {random_artefact[0]}'
              f' and his magic increases by {random_artefact[1]}')
        self._magic = 10 + int(random_artefact[1])

    def status_hero(self):
        """Показать характеристики магического героя"""
        return Hero.status_hero(self) + f', magic {self._magic}'

    def spell_sleep(self, target_hero):
        """Применить заклинание на противника"""
        if self._magic < 2:
            print(f'{self.name} doesn\'t have so much magic')
        else:
            self._magic -= 2
            print(f'{self.name} make magic. {target_hero} sleeps')


if __name__ == '__main__':
    artur = Human('King Artur')
    legolas = Elf('Legolas')
    print(artur.status_hero())
    print(legolas.status_hero())
    artur.move()
    artur.attack(legolas, 5)
    legolas.spell_sleep(artur)
    mike = Human('St_Michail')
    mike.attack(artur, 101)
    print(artur.status_hero())
    print(legolas.status_hero())
    print(mike.status_hero())
