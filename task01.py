def fibbonachi(n):
    f0 = 1
    yield f0
    f1 = 1
    yield f1
    for i in range(n - 2):
        f0, f1 = f1, f0 + f1
        yield f1


for num in fibbonachi(200):
    pass
print(num)
