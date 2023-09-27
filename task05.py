string = 'hello'
counter = 0
values = [0, 2, 4, 6, 8, 10]
while counter != 10:
    memory = string
    if counter in values:
        string = string + ' world'
    print(string)
    counter += 1
    string = memory
memory = ' world'
print(string + memory)
