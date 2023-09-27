import random


def roll_dice():
    dice = random.randint(1, 6)
    print(f"Выпало - {dice}")
    if dice == 5 or dice == 6:
        print("Вы выиграли")
    elif dice == 1 or dice == 2:
        print("Вы проиграли")
    else:
        print("Переигрываем")
        roll_dice()


if __name__ == '__main__':
    roll_dice()
