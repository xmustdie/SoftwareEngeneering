while True:
    article = input('Enter article of expenses: ')
    expenses = input('Enter expenses (sum): ')
    file = open('files/expenses.txt', 'a')
    file.write(article + '|' + expenses + '\n')
    file.close()
    proceed = input("Do u want enter another expenses y/n?")
    if proceed.lower() == 'n':
        break
