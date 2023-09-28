class AbstractPhone:
    def __init__(self, year):
        self.year = year

    def ring(self):
        print(f"dong dong to {self.year}")

    def dialing(self):
        print(f"calling someone from {self.year}")


phone = AbstractPhone(1984)
phone.dialing()
phone.ring()
