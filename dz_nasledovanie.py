class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        return self.brand, self.year


class Car(Vehicle):
    def __init__(self, brand, year, type):
        super().__init__(brand, year)
        self.type = type

    def display_info(self):
        return self.brand, self.year, self.type


class Motorcycle(Vehicle):
    def __init__(self, brand, year, kind):
        super().__init__(brand, year)
        self.kind = kind

    def display_info(self):
        return self.brand, self.year, self.kind


choise = input('Введите тип транспортного средства: ')
if choise.lower() == 'мотоцикл':
    brand = input('Введите марку мотоцикла: ')
    year = input('Введите год выпуска мотоцикла: ')
    kind = input('Введите вид мотоцикла(2х колёсный, трицикл или квадроцикл): ')
    motorcycle = Motorcycle(brand, year, kind)
    for k, v in vars(motorcycle).items():
        print(k, v)
elif choise.lower() == 'автомобиль':
    brand = input('Введите марку автомобиля: ')
    year = input('Введите год выпуска автомобиля: ')
    type = input('Введите вид автомобиля(седан, джип, минивэн): ')
    car = Car(brand, year, type)
    for k, v in vars(car).items():
        print(k, v)
else:
    print('Что то пошло не так!')


