sequence = input("Enter number sequence with space separator: ")
my_list = [int(number) for number in sequence.split(sep=" ")]
my_tuple = tuple(my_list)
print(f"this is list {my_list}")
print(f"this is tuple {my_tuple}")