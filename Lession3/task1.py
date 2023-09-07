# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов. 
# Пример: [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

input_list = [1, 2, 3, 1, 2, 4, 5, 5, 5, 4, 0, 21, 21]
dupl_list = []

for num in input_list:
    if input_list.count(num) > 1 and num not in dupl_list:
        dupl_list.append(num)

print(dupl_list)