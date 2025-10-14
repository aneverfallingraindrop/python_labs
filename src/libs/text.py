from re import *
from collections import Counter

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    res_string = text.replace('\\t', " ").replace('\\r', " ").replace('\\f', " ")
    if casefold:
        res_string = text.casefold()
    if yo2e:
        res_string = res_string.replace('ё', 'е')
        res_string = res_string.replace('Ё', 'Е')

    words = res_string.split()
    res_string = ''
    for i in words:
        res_string += i + " "
    res_string = res_string.strip()
    return res_string

def tokenize(text: str) -> list[str]:
    return findall(r'\w+(?:-\w+)*', text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    return(dict(Counter(tokens)))

def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    return sorted(Counter(freq).items())[0:n]

stroka = (["a","b","a","c","b","a"])
print(top_n(stroka, n=2))