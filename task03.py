from geron import square_triangle

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

maxTriangle = square_triangle(max(one), max(two), max(three))
minTriangle = square_triangle(min(one), min(two), min(three))
print(f"Triangle with max size square is {maxTriangle}")
print(f"Triangle with min size square is {minTriangle}")