#task1
class Auto:
    def __init__(self, model, year, fabrik, engine_volume, color, price):
        self.model = model
        self.year = year
        self.fabrik = fabrik
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def getInfo(self):
        return (f"\nНазва моделі '{self.model}',  \nрік випуску: {self.year},"
                f"\nвиробник: {self.fabrik},\nоб’єм двигуна: {self.engine_volume}, "
                f"\nколір машини: {self.color}, \nціна: {self.price}")

    def update(self, new_price):
        self.price = new_price

class AutoCollection:
    def __init__(self):
        self.cars = []

    def add_auto(self, car):
        self.cars.append(car)

    def search(self, search_object):
        results = []
        for car in self.cars:
            if (search_object in car.model or
                search_object in str(car.year) or
                search_object in car.fabrik or
                search_object in str(car.engine_volume) or
                search_object in car.color or
                search_object in car.price):
                results.append(car.getInfo())
        return results if results else ["\nЗбігів не знайдено"]

auto_collection = AutoCollection()
Auto1 = Auto("BMW X5", "1999", "Germany BMW", "100", "black", "20000 $")
Auto2 = Auto("Mercedes benz G5", "1999", "Germany Mercedes", "600", "pink", "150000 $")
print(Auto1.getInfo())
Auto2.update("250000 $")
auto_collection.add_auto(Auto1)
auto_collection.add_auto(Auto2)

search_results = auto_collection.search("Mercedes")
for result in search_results:
    print(result)

search_results = auto_collection.search("BMW")
for result in search_results:
    print(result)

search_results = auto_collection.search("Audi")
for result in search_results:
    print(result)