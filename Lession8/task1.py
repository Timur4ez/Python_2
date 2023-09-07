# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.

import os
import json
import pickle

def convert_json_to_pickle(directory):
    if not os.path.exists(directory):
        print("Указанная директория не существует.")
        return
    
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            json_path = os.path.join(directory, filename)
            pickle_path = os.path.splitext(json_path)[0] + '.pickle'
            
            try:
                with open(json_path, 'r') as json_file:
                    json_content = json.load(json_file)
                
                with open(pickle_path, 'wb') as pickle_file:
                    pickle.dump(json_content, pickle_file)
                    
                print(f"Файл {filename} успешно сконвертирован в {pickle_path}")
            except Exception as e:
                print(f"Ошибка при конвертации файла {filename}: {e}")

# Укажите путь к директории, в которой нужно произвести конвертацию
directory_path = "/путь/к/директории"
convert_json_to_pickle(directory_path)