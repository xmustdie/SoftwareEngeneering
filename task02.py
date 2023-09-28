results = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1,
           30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
three_best = sorted(results, reverse=False)[:3]
print(f"Три лучшие результата - {three_best}")
three_worse = sorted(results, reverse=True)[:3]
print(f"Три худшие результата - {three_worse}")
more_than_ten = [x for x in results if x >= 10]
print(f"Все результаты начиная с 10 - {more_than_ten}")
