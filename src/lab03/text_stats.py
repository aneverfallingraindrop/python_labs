import sys, os
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)
from src.libs.text import *
s = input()
tokens = tokenize(normalize(s, casefold=True, yo2e=True))
freq = count_freq(tokens)
print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(freq)}")
top = top_n(freq, 5)
print('Топ-5:')
print("______________________")
leng = 0
for r, t in top:
    leng = max(leng, len(r))
print(f"Слово{" " * leng}| Частота")
print("----------------------")
for x, y in top:
    print(f"{x}{" " * (leng - len(x) + 1)}| {y}") 