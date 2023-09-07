# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии

import re
import requests
from collections import Counter

url = "https://ru.wikipedia.org/wiki/Тестирование_программного_обеспечения"
response = requests.get(url)
text = response.text

cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
words = cleaned_text.split()
word_count = Counter(words)

top_words = word_count.most_common(10)
for word, count in top_words:
    print(f'Слово "{word}", {count} раз')