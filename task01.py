import time


def performance(func):
    def wrapper(*args, **kwarg):
        start = time.time()
        result = func(*args, **kwarg)
        print(f"\nВремя выполнения функции {func.__name__} - {(time.time() - start)} мс\n")
        return result
    return wrapper


@performance
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')


if __name__ == '__main__':
    fibonacci()
