test_list = [5, 2, 3, 6, 84, 9, 8, 12, 1, 54]
test_list2 = [1540, 806, 8161, 4874, 7469, 15208, 228, 5462, 5829]
test_list3 = ['дядя', 'проверка', 'остаться', 'собираться', 'билет', 'обозначить', 'формальный', 'известный', 'время',
              'рубеж']


def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


print(f"before sort: {test_list}")
print(f"after sort: {bubble_sort(test_list)}")
print()
print(f"before sort: {test_list2}")
print(f"after sort: {bubble_sort(test_list2)}")
print()
print(f"before sort: {test_list3}")
print(f"after sort: {bubble_sort(test_list3)}")
