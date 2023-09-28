# Тема 8. Основы объектно-ориентированного программирования
Отчет по Теме #8 выполнил(а):
- Дуркин Андрей Викторович
- ЗПИЭ-20-1

| Задание | Лаб_раб | Сам_раб |
| ------ |---------|---------|
| Задание 1 | -       | +       |
| Задание 2 | -       | +       |
| Задание 3 | -       | +       |
| Задание 4 | -       | +       |
| Задание 5 | -       | +       |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Самостоятельная  работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
class AbstractPhone:
    def __init__(self, year):
        self.year = year


phone = AbstractPhone(1984)
print(phone)
print(phone.year)

```
### Результат.
![Результат задания 1](./pics/task_1.png)

## Выводы

В данной работе я создал класс, являющийся основой объектно-ориентированных языков, и создал экземпляр данного класса

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```

### Результат.
![Результат задания 2](./pics/task_2.png)

## Выводы
в данной работе я расширил класс из 1 работы добавив атрибуты и методы класса.

## Самостоятельная работа №3 
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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

```

### Результат.
![Результат задания 3](./pics/task_3.png)

## Выводы
в данной задаче я создал дочерний класс от класса AbstractPhone 
  
## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли. 

```python
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


```

### Результат.
![Результат задания 4](./pics/task_4.png)

## Выводы

В данной работе я реализовал инкапсуляцию для существующих классов, то есть скрыл детали реализации от внешнего пользователя

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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


class User:
    def __init__(self, name):
        self.name = name

    def calling(self, number, phone):
        phone.dialing(number)
        print(f"{self.name} calling by {number}")


wireless_phone = WirelessPhone(1984, 10)
old_phone = AbstractPhone(1926)
user = User('John')
user.calling(123123123, wireless_phone)
user.calling(123123123, old_phone)
```

### Результат.
![Результат задания 5](./pics/task_5.png)


## Выводы

В данной работе успешно реализовали принцип ООП полиморфизм 

## Общие выводы по теме
- В данной теме мы познакомились с реализацией принципов ООП таких, как: инкапсуляция, полиморфизм, наследование. Познакомились с областями видимости переменных классов и их методов, создали экземпляры классов и передали их в качестве аргументов в методы другого класса 


