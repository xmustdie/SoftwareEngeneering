class AbstractPhone:
    def __init__(self, year):
        self.year = year

    def ring(self):
        print(f"dong dong to {self.year}")

    def dialing(self, number):
        print(f"Hello-Central, plz connect to number {number}")


class WirelessPhone(AbstractPhone):
    def __init__(self, year, charge_reserve):
        super().__init__(year)
        self._charge_reserve = charge_reserve

    def charging(self, charge):
        self._charge_reserve += charge
        print(f"Charge reserve is {self._charge_reserve}")

    def __discharge(self):
        self._charge_reserve -= 1

    def ring(self):
        self.__discharge()
        print("Beep beep")

    def dialing(self, number):
        self.__discharge()
        print(f"Dialing {number}...")


phone = WirelessPhone(1984, 10)
phone.dialing(825513132435)
phone.ring()
phone.charging(3)
