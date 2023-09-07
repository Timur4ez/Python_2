# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и 
# произведение* дробей. Для проверки своего кода используйте модуль fractions.

fraction1_str = input("Введите первую дробь в формате a/b: ")
fraction2_str = input("Введите вторую дробь в формате a/b: ")

numerator1, denominator1 = map(int, fraction1_str.split("/"))

numerator2, denominator2 = map(int, fraction2_str.split("/"))

sum_numerator = numerator1 * denominator2 + numerator2 * denominator1
sum_denominator = denominator1 * denominator2

product_numerator = numerator1 * numerator2
product_denominator = denominator1 * denominator2

print("Сумма дробей:", sum_numerator, "/", sum_denominator)
print("Произведение дробей:", product_numerator, "/", product_denominator)


# from fractions import Fraction

# fraction1_str = input("Введите первую дробь в формате a/b: ")
# fraction2_str = input("Введите вторую дробь в формате a/b: ")

# # Разбираем первую дробь с помощью Fraction
# fraction1 = Fraction(fraction1_str)

# # Разбираем вторую дробь с помощью Fraction
# fraction2 = Fraction(fraction2_str)

# # Вычисляем сумму дробей
# sum_fraction = fraction1 + fraction2

# # Вычисляем произведение дробей
# product_fraction = fraction1 * fraction2

# print("Сумма дробей:", sum_fraction)
# print("Произведение дробей:", product_fraction)