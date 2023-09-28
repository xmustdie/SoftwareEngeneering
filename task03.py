def summary():
    try:
        x = int(input("Enter number: "))
        return 2 + x
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")
    return 0


print(summary())
