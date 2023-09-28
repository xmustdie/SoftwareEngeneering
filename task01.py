class AbstractPhone:
    def __init__(self, year):
        self.year = year


phone = AbstractPhone(1984)
print(phone)
print(phone.year)
