import data
import hw1
import unittest

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

# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input = "Tarantula"
        result = hw1.vowel_count(input)
        expected = 4
        self.assertEqual(expected, result)
    def test_vowel_count_2(self):
        input = "MoUsy"
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    # Part 2
    def test_short_lists_1(self):
        input = [[2, 5], [9, 5, 3, 2], [4, 7, 8], [5], [5, 6]]
        result = hw1.short_lists(input)
        expected = [[2, 5], [5, 6]]
        self.assertEqual(expected, result)
    def test_short_lists_2(self):
        input = [[4, 0, 2, 3], [9], [], [5], [5, 6, 8]]
        result = hw1.short_lists(input)
        expected = []
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs_1(self):
        input = [[4, 0, 2, 3], [9], [1, 5], [5, 9], [5, 6, 8], [9, 3], [10, 2]]
        result = hw1.ascending_pairs(input)
        expected = [[4, 0, 2, 3], [9], [1, 5], [5, 9], [5, 6, 8], [3, 9], [2, 10]]
        self.assertEqual(expected, result)
    def test_ascending_pairs_2(self):
        input = [[3, 5, 7], [10, 9], [1, 3], [5, 4]]
        result = hw1.ascending_pairs(input)
        expected = [[3, 5, 7], [9, 10], [1, 3], [4, 5]]
        self.assertEqual(expected, result)
    # Part 4
    def test_add_prices_1(self):
        result = hw1.add_prices(data.Price(109, 45), data.Price(90, 87))
        expected = data.Price(200, 32)
        self.assertEqual(expected, result)
    def test_add_prices_2(self):
        result = hw1.add_prices(data.Price(209, 41), data.Price(10,30))
        expected = data.Price(219, 71)
        self.assertEqual(expected, result)
    # Part 5
    def test_rectangle_area_1(self):
        result = hw1.rectangle_area(data.Rectangle(data.Point(4.0, 9.0), data.Point(10.0, 8.0)))
        expected = 6.0
        self.assertEqual(expected, result)
    def test_rectangle_area_2(self):
        result = hw1.rectangle_area(data.Rectangle(data.Point(13.0, 3.0), data.Point(28.0, -3.0)))
        expected = 90.0
        self.assertEqual(expected, result)

    # Part 6
    def test_books_by_author_1(self):
        result = hw1.books_by_author("Dr. Seuss", [data.Book(["Dr. Seuss"], "The Lorax"), data.Book(["Roal Dahl"], "The Giant"), data.Book(["Dr. Seuss"], "Green Eggs and Ham")])
        expected = [data.Book(["Dr. Seuss"], "The Lorax"), data.Book(["Dr. Seuss"], "Green Eggs and Ham")]
        self.assertEqual(expected, result)
    def test_books_by_author_2(self):
        result = hw1.books_by_author("Ann Patchett", [data.Book(["Roal Dahl"], "The Giant"), data.Book(["Ann Patchett"], "Commonwealth"), data.Book(["Coleen Hoover"], "It Ends With Us")])
        expected = [data.Book(["Ann Patchett"], "Commonwealth")]
        self.assertEqual(expected, result)

    # Part 7
    def test_circle_bound_1(self):
        input = data.Rectangle(data.Point(3.3, 9.9), data.Point(10.2, 5.5))
        result = hw1.circle_bound(input)
        expected = data.Circle(data.Point(6.75, 7.7), 4.09)
        self.assertEqual(expected, result)
    def test_circle_bound_2(self):
        input = data.Rectangle(data.Point(10.3, 9.4), data.Point(18.3, 5.5))
        result = hw1.circle_bound(input)
        expected = data.Circle(data.Point(14.3, 7.45), 4.45)
        self.assertEqual(expected, result)

    # Part 8
    def test_below_pay_average_1(self):
        input = [data.Employee("Jess", 18), data.Employee("Ben", 24), data.Employee("Jack", 16), data.Employee("Sarah", 21), data.Employee("Gordon", 22)]
        result = hw1.below_pay_average(input)
        expected = ["Jess", "Jack"]
        self.assertEqual(expected, result)
    def test_below_pay_average_2(self):
        input = [data.Employee("Gabe", 19), data.Employee("Sofia", 18), data.Employee("Donald", 15), data.Employee("Perry", 25), data.Employee("Luke", 20)]
        result = hw1.below_pay_average(input)
        expected = ["Gabe", "Sofia", "Donald"]
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
