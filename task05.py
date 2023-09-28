def square_triangle(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class IllegalArgumentException(Exception):
    def __init__(self, message):
        self.message = message


a = int(input("Enter a > 0 : "))
b = int(input("Enter b > 0 : "))
c = int(input("Enter c > 0 : "))

try:
    if a <= 0 or b <= 0 or c <= 0:
        raise IllegalArgumentException("Fatal error, argument must be greater than 0")
    elif a + b < c or a + c < b or b + c < a:
        raise IllegalArgumentException("Fatal error, there's not triangle")
    else:
        square = square_triangle(a, b, c)
        print(f"Square of triangle is {round(square, 3)}")
except IllegalArgumentException as e:
    print(f"{e.message}")
