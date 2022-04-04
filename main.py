# bsp 1
def count_vowels(text):
    res = type(text) == str
    if res == True:
        a = text.count("a")
        A = text.count("A")
        e = text.count("e")
        E = text.count("E")
        i = text.count("i")
        I = text.count("I")
        o = text.count("o")
        O = text.count("O")
        u = text.count("u")
        U = text.count("U")
        sum = a + A + e + E + i + I + o + O + u + U
    else:
        sum = 42
    return sum
print(count_vowels("magdalena"))
print("\n")


#bsp 2
def hamming(text1, text2):
    if len(text1) == len(text2):
        ham = 0
        for i in range(len(text1)):
            if text1[i] != text2[i]:
                ham += 1
    else:
        ham = 0
    return ham
print(hamming("cat","hat"))
print("\n")


# bsp 3
class Vehicle:

    def __init__(self, color, fuel_type):
        self.color = color
        self.fuel_type = fuel_type

class Car(Vehicle):
    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)
        self.doors = doors

    def __str__(self):
        return("Color: " + Car.color, "Fuel type: " + Car.fuel_type, "Doors: " + Car.doors)

class Bus(Vehicle):
    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return("Color: " + Bus.color, "Fuel type: " + Bus.fuel_type, "Passengers: " + Bus.passengers)


car1 = Car("Red", "Diesel", "4")
bus1 = Bus("Blue", "Gasoline", "8")
print("Color: " + car1.color, " Fuel type: " + car1.fuel_type, " Doors: " + car1.doors)
print("Color: " + bus1.color, " Fuel type: " + bus1.fuel_type, " Passengers: " + bus1.passengers)
print("\n")


#bsp 4
class Book:

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return(self.name + ", " + self.author)

book1 = Book("Frankenstein", "Mary Shelley")
print(book1)

book2 = Book("Dune", "Frank Herbert")
book3 = Book("Animal Farm", "George Orwell")
book4 = 124
booklist = [book1, book2, book3, book4]

author1 = "Frank Herbert"

# bsp 5

class BookShelf(Book):

    def __init__(self, name, author, books):
        super().__init__(name, author)
        self.books = books

    def add_book_list(self, books):
        books = []
        for i in booklist:
            if isinstance(i, Book):
                books.append(i)
            return books

    def books_by_author(self, author):
        authorlist = []
        for i in books:
            if i.author == author1:
             authorlist.append(i.name)
        if books == []:
            authorlist = []
        return authorlist

    def get_books(self):
        namelist = []
        for i in books:
            namelist.append(i.name)
        if books == []:
            namelist = []
        return namelist

    def clear_shelf(self):
        books.clear()
        return books