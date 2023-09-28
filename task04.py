test_list = [5, 2, 3, 6, 84, 9, 8, 12, 1, 54]
test_list2 = [1540, 806, 8161, 4874, 7469, 15208, 228, 5462, 5829]
test_list3 = ['дядя', 'проверка', 'остаться', 'собираться', 'билет', 'обозначить', 'формальный', 'известный', 'время',
              'рубеж']


def inverse_order(func):
    def wrapper(*args, **kwarg):
        result = func(*args, **kwarg)[::-1]
        return result
    return wrapper


@inverse_order
def bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


@inverse_order
def merge_sort(numbers):
    if len(numbers) > 1:
        mid = len(numbers) // 2
        left, right = numbers[:mid], numbers[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1
    return numbers


print(f"before sort: {test_list}")
print(f"after bubble sort: {bubble_sort(test_list)}")
print(f"after merge sort: {merge_sort(test_list)}")
print()
print(f"before sort: {test_list2}")
print(f"after bubble sort: {bubble_sort(test_list2)}")
print(f"after merge sort: {merge_sort(test_list2)}")
print()
print(f"before sort: {test_list3}")
print(f"after bubble sort: {bubble_sort(test_list3)}")
print(f"after merge sort: {merge_sort(test_list3)}")
