import datetime
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

#task2

class Book:
    def __init__(self, title, author, birth_year, publisher, genre, price):
        self.title = title
        self.author = author
        self.birth_year = birth_year
        self.publisher = publisher
        self.genre = genre
        self.price = price

    def getInfo(self):
        return (f"\nНазва книги '{self.title}',  \nавтор: {self.author},"
                f"\nрік видання: {self.birth_year}, "
                f"\nвидавництво: {self.publisher},"
                f"\nжанр: {self.genre},"
                f"\nціна: {self.price}")

    def calculate_age(self):
        year_now = datetime.datetime.now().year
        return f"Вік книги: {year_now - self.birth_year} роки/ів"

book_1 = Book("Ворон", "Едгар Аллан По", 1850, "Абабагаламага", "хорор", "150 грн")
print(book_1.getInfo())
print(book_1.calculate_age())

#task3
class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Введіть назву стадіону: ")
        self.opening_date = input("Введіть дату відкриття (формат: рік-місяць-день): ")
        self.country = input("Введіть країну: ")
        self.city = input("Введіть місто: ")
        self.capacity = int(input("Введіть місткість стадіону: "))

    def display_data(self):
        print(f"Назва стадіону: {self.name}")
        print(f"Дата відкриття: {self.opening_date}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity}")

    def update_capacity(self, new_capacity):
        self.capacity = new_capacity
        print(f"Місткість стадіону оновлено на {self.capacity} місць.")

stadium = Stadium("Національний стадіон", "2003-10-01", "Україна", "Київ", 70000)
stadium.display_data()
stadium.update_capacity(80000)
stadium.input_data()
stadium.display_data()