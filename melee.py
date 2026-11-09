class MeleeWeapon:

    def __init__(self, name):
        self.name = name
        self.strength = 100
    
    # Метод родительского класса.
    def slashing_blow(self):
        # При рубящем ударе уменьшаем прочность меча на 10.
        self.strength -= 10
        return f'Нанесён рубящий удар оружием {self.name}.'
    
    def sharpen(self):
        self.strength = 100
        return (f'Оружие "{self.name}" заточено.')


class Sword(MeleeWeapon):

    # Переопределяем метод родительского класса...
    def slashing_blow(self):
        # ...меняем значение снижения прочности...
        self.strength -= 5
        # ...и меняем сообщение.
        return f'Мечом {self.name} был нанесен рубящий удар.'

# Этот класс-наследник полностью наследует все методы и свойства
# родительского класса.
class Axe(MeleeWeapon):
    ...

brodex = Axe('Верный')
xiphos = Sword('Разящий')

# Для класса Sword будет вызван переопределённый метод.
print(xiphos.slashing_blow())
# Для класса Axe будет вызван метод родительского класса.
print(brodex.slashing_blow())
# Исходное значение прочности для класса Sword будет уменьшено
# на переопределённое значение.
print(xiphos.strength)
# Исходное значение просности для класса Axe будет уменьшено
# на значение, указанное в родительском классе.
print(brodex.strength)