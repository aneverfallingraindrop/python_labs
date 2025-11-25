import sys
import os
from pathlib import Path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, project_root)
from io_txt_csv import write_csv
from src.libs import text
path_in = "././data/lab04/input.txt"
path_a = "././data/lab04/a.txt"
path_b = "././data/lab04/b.txt"
# path_file = input() # - allows free file path input
if not Path(path_in).exists():
    raise FileNotFoundError

with open(path_in, mode="r", newline='', encoding='utf-8') as f:
    string = f.read()
    top = 5
    txt = text.top_n(text.count_freq(text.tokenize(text.normalize(string, casefold=True, yo2e=True))), 5)
    words = []
    for item in txt:
        words.append(item)
    write_csv(words, "././data/lab04/report", ("word", "count"))
    print(f"Всего слов: {len(string.split())}")
    print(f"Уникальных слов: {len(txt)}")
    print('Топ-5:')
    print("______________________") 
    max_len = 5
    for r, t in txt: 
        max_len = max(max_len, len(r))
    print(f"Слово{" " * (max_len - 4)}| Частота")
    print("----------------------")
    for x, y in txt:
        print(f"{x}{" " * (max_len - len(x) + 1)}| {y}")

