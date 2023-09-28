def check_id(tuple1, el):
    if el not in tuple1:
        return ()
    x = tuple1.index(el)
    result = tuple1[x:]
    if el not in result[1:]:
        return result
    y = result[1:].index(el) + 2
    return result[:y]


input_data = (((1, 2, 3), 8),
              ((1, 8, 3, 4, 8, 8, 9, 2), 8),
              ((1, 2, 8, 5, 1, 2, 9), 8))

for e in input_data:
    print(check_id(e[0], e[1]))
