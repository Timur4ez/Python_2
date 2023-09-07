# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.


# num = int(input("Введите целое число: "))

# hex_string = hex(num)

# print("Шестнадцатеричное представление числа:", hex_string)


num = int(input("Введите целое число: "))

if num == 0:
    hex_string = "0"
else:
    hex_chars = "0123456789ABCDEF"
    hex_string = ""

    if num < 0:
        num = -num
        hex_string = "-"

    while num > 0:
        remainder = num % 16
        hex_string = hex_chars[remainder] + hex_string
        num //= 16

print("Шестнадцатеричное представление числа:", hex_string)