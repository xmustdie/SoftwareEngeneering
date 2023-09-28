class Tomato:
    states = {'Отсутствует': 0, 'Цветение': 1, 'Зеленый': 2, 'Красный': 3}

    def __init__(self, _index):
        # protected field
        self._index = _index
        # protected field
        self._state = self.states['Отсутствует']

    def grow(self):
        if self._state < 3:
            self._state += 1

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, amount):
        self.tomatoes = [Tomato(index) for index in range(1, amount + 1)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        # public field
        self.name = name
        # protected field
        self._plant = plant

    def work(self):
        print('Ухаживаем за помидорным кустом')
        self._plant.grow_all()

    def harvest(self):
        if len(self._plant.tomatoes) == 0:
            print("Отсутствует доступный куст с помидорами")
            return
        if self._plant.all_are_ripe():
            print('Урожай собран!')
            self._plant.give_away_all()
        else:
            print('Помидоры еще не дозрели')

    @staticmethod
    def knowledge_base():
        print('Справка по садоводству:')
        print('1. Не забывайте регулярно поливать и подкармливать растения')
        print('2. Определите правильное расстояние между растениями, чтобы они не мешали друг другу в росте')
        print('3. Удалите поврежденные листья и плоды, чтобы предотвратить распространение болезней\n')


# Вызов справки по садоводству
Gardener.knowledge_base()

# Создание объектов классов TomatoBush и Gardener
bush = TomatoBush(7)
gardener = Gardener('Juan Pablo Montoya', bush)

# Уход за кустом с помидорами
gardener.work()
gardener.work()

# Попытка сбора урожая
gardener.harvest()

# Сбор урожая после дозревания всех томатов
gardener.work()
gardener.harvest()
gardener.harvest()
