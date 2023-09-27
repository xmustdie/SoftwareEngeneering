x = int(input("Enter integer in range [0,10]: "))
if 0 <= x <= 10:
    print("от 0 до 3 включительно" if x <= 3 else "от 3 до 6 " if x < 6 else "от 6 до 10 включительно")
else:
    print("Integer must be in range [0,10]")
