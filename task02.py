def remove_element(tuple1, el):
    if el in tuple1:
        x = tuple1.index(el)
        tuple1 = tuple1[:x] + tuple1[x + 1:]
    return tuple1


incoming = [((1, 2, 3), 1),
            ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3),
            ((2, 4, 6, 6, 4, 2), 9)]
for e in incoming:
    print(f"Remove first element {e[1]} from {e[0]}")
    print(remove_element(e[0], e[1]))
