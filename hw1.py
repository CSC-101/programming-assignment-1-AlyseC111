import data
import math

# Representation of a price in integer dollars and cents.
class Price:
    # Initialize a new Price object.
    # input: dollars as an integer
    # input: cents as an integer
    def __init__(self, dollars: int, cents: int):
        self.dollars = dollars
        self.cents = cents


    # Provide a developer-friendly string representation of the object.
    # input: Price for which a string representation is desired.
    # output: string representation
    def __repr__(self) -> str:
        return 'Price({}, {})'.format(self.dollars, self.cents)


    # Compare the Price object with another value to determine equality.
    # input: Price against which to compare
    # input: Another value to compare to the Price
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Price and
                self.dollars == other.dollars and
                self.cents == other.cents)
class Point:
    # Initialize a new Point object.
    # input: x-coordinate as a float
    # input: y-coordinate as a float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    # Provide a developer-friendly string representation of the object.
    # input: Point for which a string representation is desired.
    # output: string representation
    def __repr__(self) -> str:
        return 'Point({}, {})'.format(self.x, self.y)


    # Compare the Point object with another value to determine equality.
    # input: Point against which to compare
    # input: Another value to compare to the Point
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Point and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y))
class Rectangle:
    # Initialize a new Rectangle object.
    # input: top-left corner as a Point
    # input: bottom-right corner as a Point
    def __init__(self, top_left: Point, bottom_right: Point):
        self.top_left = top_left
        self.bottom_right = bottom_right


    # Provide a developer-friendly string representation of the object.
    # input: Rectangle for which a string representation is desired.
    # output: string representation
    def __repr__(self) -> str:
        return 'Rectangle({}, {})'.format(self.top_left, self.bottom_right)


    # Compare the Rectangle object with another value to determine equality.
    # input: Rectangle against which to compare
    # input: Another value to compare to the Rectangle
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Rectangle and
                self.top_left == other.top_left and
                self.bottom_right == other.bottom_right)
class Circle:
    # Initialize a new Circle object.
    # input: center as a Point
    # input: radius as a float
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius


    # Provide a developer-friendly string representation of the object.
    # input: Circle for which a string representation is desired.
    # output: string representation
    def __repr__(self) -> str:
        return 'Circle({}, {})'.format(self.center, self.radius)


    # Compare the Circle object with another value to determine equality.
    # input: Circle against which to compare
    # input: Another value to compare to the Circle
    # output: boolean indicating equality
    def __eq__(self, other) -> bool:
        return (other is self or
                type(other) == Circle and
                self.center == other.center and
                math.isclose(self.radius, other.radius))
class Book:
    # Initialize a new Book object.
    # input: the book's authors as a list of strings
    # input: the book's title as a string
    def __init__(self, authors: list[str], title: str):
        self.authors = authors
        self.title = title


    # Provide a developer-friendly string representation of the object.
    # input: Book for which a string representation is desired.
    # output: string representation
    def __repr__(self):
        return "Book({}, '{}')".format(self.authors, self.title)


    # Compare the Book object with another value to determine equality.
    # input: Book against which to compare
    # input: Another value to compare to the Book
    # output: boolean indicating equality
    def __eq__(self, other):
        return (self is other or
                type(other) == Book and
                self.authors == other.authors and
                self.title == other.title)
class Employee:
    # Initialize a new Employee object.
    # input: the employee's name as a string
    # input: the employee's pay rate as an integer (for simplicity)
    def __init__(self, name: str, pay_rate: int):
        self.name = name
        self.pay_rate = pay_rate


    # Provide a developer-friendly string representation of the object.
    # input: Employee for which a string representation is desired.
    # output: string representation
    def __repr__(self):
        return "Employee('{}', {})".format(self.name, self.pay_rate)


    # Compare the Employee object with another value to determine equality.
    # input: Employee against which to compare
    # input: Another value to compare to the Employee
    # output: boolean indicating equality
    def __eq__(self, other):
        return (other is self or
                type(other) == Employee and
                self.name == other.name and
                self.pay_rate == other.pay_rate)

# Write your functions for each part in the space below.

# Part 1
# This function iterates through a string to find how many vowels it contains, then returns the
# number of vowels in the string in the form of an integer.
def vowel_count(string: str) -> int:
    count = 0
    for i in string:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            count += 1
    return count

# Part 2
# This function takes input in the form of a nested list (list[list[int]]) and returns a list of all
# the lists within the nested list that are of length 2.
def short_lists(lists: list[list[int]]) -> list:
    shortl = []
    for i in lists:
        if len(i) == 2:
            shortl.append(i)
    return shortl

# Part 3
#This function takes in a nested list and returns a new list where every list in the input list
#with a length of 2 is rearranged so the values are in ascending order.
def ascending_pairs(pairs: list[list[int]]) -> list:
    new = []
    new += pairs
    for i in new:
        if len(i) == 2:
            for u in i:
                if u > i[1]:
                    y = i[1]
                    i[1] = u
                    i[0] = y
    return new

# Part 4
# This function takes two inputs of type Price and returns a Price output with the sum of both
#prices entered, but the cents must remain below 99.
def add_prices(price1: Price, price2: Price) -> Price:
    dollars = price1.dollars + price2.dollars
    cents = price1.cents + price2.cents
    if cents > 99:
        dollars += 1
        cents -= 100
    newprice = data.Price(dollars, cents)
    return newprice

# Part 5
#This function must compute and return the area of the input rectangle of type Rectangle with
# the assumption that the rectangle is properly axis-aligned.
def rectangle_area(rect: Rectangle) -> float:
    topleft = rect.top_left
    bottomright = rect.bottom_right
    width = abs(topleft.x - bottomright.x)
    height = abs(topleft.y - bottomright.y)
    return width * height

# Part 6
#This function takes two pieces of input, one of type str and the other of type list[Book].
#It will return a list[Book] of all books in the input list written by the author specified in the first parameter.
def books_by_author(author: str, books: list[Book]) -> list[Book]:
    new = []
    for book in books:
        for authors in book.authors:
            if authors == author:
                new.append(book)
    return new
# Part 7
#This function takes in a parameter of type Rectangle and must return a Circle (defined in the provided files) object that represents a
# "bounding circle" for the provided rectangle. Such a bounding circle should be the smallest circle that
# encloses the rectangle; the circle should be centered at the center of the rectangle with radius equal
# to the distance from the center to one of the corner points.
def circle_bound(rect: Rectangle) -> Circle:
    topleft = rect.top_left
    bottomright = rect.bottom_right
    width = abs(topleft.x-bottomright.x)
    height = abs(topleft.y - bottomright.y)
    mid_point = data.Point(round(topleft.x + (width/2), 2), round(topleft.y - (height/2), 2))
    radius = round((math.sqrt(width**2 + height**2))/2, 2)
    return data.Circle(mid_point, radius)


# Part 8
#This function takes input of type list[Employee] and returns a list of type list[str] of all the employees
#being paid less than the average pay of the employees in the list.
def below_pay_average(list: list[Employee]) -> list[str]:
    l = []
    sum = 0
    employees = []
    for emp in list:
        l.append(emp.pay_rate)
    for pay in l:
        sum += pay
    average = sum / len(list)
    for emp in list:
        if emp.pay_rate < average:
            employees.append(emp.name)
    return employees



