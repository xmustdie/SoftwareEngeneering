def fibbonachi(n):
    f0 = 1
    yield f0
    f1 = 1
    yield f1
    with open('fib.txt', 'a') as file:
        file.write(f"{f0}\n{f1}\n")
    for i in range(n - 2):
        f0, f1 = f1, f0 + f1
        with open('fib.txt', 'a') as file:
            file.write(f"{f1}\n")
        yield f1


for num in fibbonachi(200):
    pass
print(num)
