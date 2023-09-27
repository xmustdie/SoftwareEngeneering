def average(*numbers):
    total = 0
    for i in numbers:
        total += i
    return total / len(numbers)


if __name__ == '__main__':
    result = average(1, 2, 3, 4, 5, 6)
    print(f"Average is {result}")
