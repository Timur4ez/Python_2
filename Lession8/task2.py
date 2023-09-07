# Напишите функцию, которая сереализует содержимое текущей директории в json-файл. В файле должен храниться список словарей, словарь описывает 
# элемент внутри директории: имя, расширение, тип. Если элемент - директория, то только тип и имя. Пример результата для папки, где лежит файл 
# test.txt и директория directory_test:

import os
import json

def serialize_directory_content(directory):
    if not os.path.exists(directory):
        print("Указанная директория не существует.")
        return
    
    content_list = []
    
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        
        item_info = {
            'name': item,
        }
        
        if os.path.isfile(item_path):
            item_info['type'] = 'file'
            item_info['extension'] = os.path.splitext(item)[1]
        elif os.path.isdir(item_path):
            item_info['type'] = 'directory'
        
        content_list.append(item_info)
    
    return content_list

directory_path = "/путь/к/директории"
serialized_content = serialize_directory_content(directory_path)


output_path = "directory_content.json"
with open(output_path, 'w') as json_file:
    json.dump(serialized_content, json_file, indent=4)

print(f"Содержимое директории сохранено в файл: {output_path}")