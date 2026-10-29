# #1
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(f"{self.title} - {self.author}, {self.pages} გვ.")

book1 = Book("ვეფხისტყაოსანი", "შოთა რუსთაველი,", 250)
book2 = Book("კადმოსის მემკვიდრენი", "ჯემალ ქარჩხაძე,", 320)
book3 = Book("ბახტრიონი","ილია ჭავჭავაძე,", 180)

book1.info()
book2.info()
book3.info()

# # 2

class Car:
    wheels = 4
    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

car1 = Car("BMW", "Black", 2020)
car2 = Car("Toyota", "White", 2024)
print(car1.brand,car1.wheels)
print(car2.brand,car2.wheels)

car2.wheels = 3

print(car1.wheels)
print(car2.wheels)
print(Car.wheels)

## 3

class Player:
    players_count = 0
    def __init__(self, name, level = 1):
        self.name = name
        self.level = level
        Player.players_count += 1

print(Player.players_count)

player1 = Player("ანა")
player2 = Player("დავითი", 5)
player3 = Player(name = "მარიამი", level = 3)

print(f"სულ მოთამაშე: {Player.players_count}")

print(player1.name, player1.level)
print(player2.name, player2.level)
print(player3.name, player3.level)

