def create_set(input_list):
    result = set()
    for e in input_list:
        el = e
        while True:
            if el in result:
                el = str(el) + str(e)
            else:
                result.add(el)
                break
    return result


list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(create_set(list_1))
print(create_set(list_2))
print(create_set(list_3))
