# 1.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


# a = float(input("Сторона a: "))
# b = float(input("Сторона b: "))
# c = float(input("Сторона c: "))

# if a + b > c and a + c > b and b + c > a:

#     if a != b and b != c and a != c:
#         print("Треугольник - разносторонний.")
#     elif a == b and b == c:
#         print("Треугольник - равносторонний.")
#     else:
#         print("Треугольник - равнобедренный.")
# else:
#     print("Треугольник с такими сторонами не существует.")


# 2. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является 
# простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# number = int(input("Введите число: "))


# if number < 0 or number > 100000:
#     print("Число должно быть положительным и не превышать 100 тысяч.")
# else:
#     if number < 2:
#         print("Число не является ни простым, ни составным.")
#     else:
#         is_prime = True
#         for i in range(2, int(number**0.5) + 1):
#             if number % i == 0:
#                 is_prime = False
#                 break
        
#         if is_prime:
#             print("Число является простым.")
#         else:
#             print("Число является составным.")