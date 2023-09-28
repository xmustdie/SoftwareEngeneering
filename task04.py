class AbstractPhone:
    def __init__(self, year):
        self.year = year

    def ring(self):
        print(f"dong dong to {self.year}")

    def call_someone(self):
        print(f"calling someone from {self.year}")


class WirelessPhone(AbstractPhone):
    def __init__(self, year, charge_reserve):
        super().__init__(year)
        self.__charge_reserve = charge_reserve

    def charging(self, charge):
        self.__charge_reserve += charge
        print(f"Charge reserve is {self.__charge_reserve}")

    def __discharge(self):
        self.__charge_reserve -= 1

    def ring(self):
        self.__discharge()
        print("Beep beep")

    def call_someone(self):
        self.__discharge()
        print("Calling to another person")


phone = WirelessPhone(1984, 10)
phone.call_someone()
phone.ring()
phone.charging(2)
