# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int, премия str с 
# указанием процентов вида “10.25%”. В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
# Сумма рассчитывается как ставка умноженная на процент премии

name_list = ['Sergio', 'Keks', 'Mitya']
salary_list = [1123, 2002, 3234]
extra_list = ['10.25%', '15%', '20%']

result_dict = {name: salary * float(extra.strip('%')) / 100 for name, salary, extra in zip(name_list, salary_list, extra_list)}

print(result_dict)