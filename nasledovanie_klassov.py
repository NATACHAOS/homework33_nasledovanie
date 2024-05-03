class Car:
    """Машина"""
    price = 1000000  # цена машины

    def horse_power(self):  # метод, который пишет мощность машины
        print('Мощность 600 л.с.')

    def __str__(self):  # метод, который выводит информацию на консоль
        return '{} цена {} рублей'.format(self.__class__.__name__, self.price)


class Nissan(Car):
    price = 1000500  # цена Ниссан

    def horse_power(self):  # метод, который пишет мощность Ниссана
        print('Мощность 700 л.с.')


class Kia(Car):
    price = 1100000  # цена Киа

    def horse_power(self):  # метод, который пишет мощность Киа
        print('Мощность 750 л.с.')


# создаем объекты
my_car = Car()
my_nissan = Nissan()
my_kia = Kia()
print(my_car)  # выводим инф. о цене Машины
my_car.horse_power()  # вызываем метод Машины
print(my_nissan)
my_nissan.horse_power()
print(my_kia)
my_kia.horse_power()
