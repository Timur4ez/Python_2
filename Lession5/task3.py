# Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator():
    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    
    n = 0
    while True:
        yield fibonacci(n)
        n += 1

fib_gen = fibonacci_generator()

fibonacci_numbers = [next(fib_gen) for _ in range(10)]
print(fibonacci_numbers) 