from geron import square_triangle

a = int(input("Enter a > 0 :"))
b = int(input("Enter b > 0 :"))
c = int(input("Enter c > 0 :"))

if a <= 0 or b <= 0 or c <= 0:
    print("fatal error, argument must be greater than 0")
elif a + b < c or a + c < b or b + c < a:
    print("fatal error, there's not triangle")
else:
    square = square_triangle(a, b, c)
    print(f"Square of triangle is {round(square, 3)}")
