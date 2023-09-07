# - Нахождение корней квадратного уравнения
# - Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

# 1
import math

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    

# 2
import csv
import random

def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for _ in range(num_rows):
            row = [random.random() for _ in range(3)]
            csv_writer.writerow(row)

# 3
def quadratic_roots_decorator(func):
    def wrapper(*args):
        roots = []
        for row in args:
            a, b, c = row
            roots.append(func(a, b, c))
        return roots
    return wrapper

# 4
import json
import functools

def cache_decorator(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        arg_key = json.dumps(args)
        
        if arg_key in cache:
            return cache[arg_key]
        
        result = func(*args)
        cache[arg_key] = result
        
        with open('cache.json', 'w') as cache_file:
            json.dump(cache, cache_file, indent=4)
        
        return result

    return wrapper

# использование всех компонентов


generate_csv('data.csv', 100)

@quadratic_roots_decorator
@cache_decorator
def find_roots(a, b, c):
    return quadratic_roots(a, b, c)


with open('data.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    data = [list(map(float, row)) for row in csv_reader]

result = find_roots(*data)

print(result)