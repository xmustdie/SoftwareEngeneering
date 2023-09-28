variants = [[2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4],
            [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4],
            [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]]
for rates in variants:
    rates = [e for e in rates if e != 2]
    rates = [4 if e == 3 else e for e in rates]
    print(rates)
