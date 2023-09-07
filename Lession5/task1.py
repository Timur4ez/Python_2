# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: 
# путь, имя файла, расширение файла.

import os

def parse_file_path(file_path):
    directory, file_with_extension = os.path.split(file_path)
    
    file_name, file_extension = os.path.splitext(file_with_extension)
    
    return directory, file_name, file_extension

file_path = "C:/Users/Acer/Desktop/seminar_5/test.txt"
result = parse_file_path(file_path)
print(result)