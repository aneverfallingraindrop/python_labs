from re import *

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

# print(f'"ПрИвЕт\nМИр\t" -> {normalize("ПрИвЕт\nМИр\t", casefold = True, yo2e= True)}')
# print(f'"ёжик, Ёлка" -> {normalize("ёжик, Ёлка", casefold= True, yo2e=True)}')
# print(f'"Hello\r\nWorld" -> {normalize("Hello\r\nWorld", casefold=True)}')
# print(f'"  двойные   пробелы  " -> {normalize("  двойные   пробелы  ")}')

def tokenize(text: str) -> list[str]:
    return findall(r'\w+(?:-\w+)*', text)

# print(f'"привет мир" -> {tokenize("привет мир")}')
# print(f'"hello,world!!!" -> {tokenize("hello,world!!!")}')
# print(f'"по-настоящему круто" -> {tokenize("по-настоящему круто")}')
# print(f'"2025 год" -> {tokenize("2025 год")}')
# print(f'"emoji 😀 не слово" -> {tokenize("emoji 😀 не слово")}')

def count_freq(data):
    new_data = []
    new_data = set(data)
    dict = {}
    for i in new_data:
        col = data.count(i)
        dict[i] = col
    return dict

def top_n(dict, n_top):
    text = []
    for key, value in dict.items():
        text.append((key, value))
    ans = text.sort()
    ans = sorted(text, key = lambda x: (x[1]), reverse=True)
    res = []
    if n_top > len(dict):
        for i in range(len(dict)):
            res.append(ans[i])
    else:
        for i in range(n_top):
            res.append(ans[i])
    return res

# print(f'tokens ["a","b","a","c","b","a"] -> {count_freq(["a","b","a","c","b","a"])}')
# print(f'tokens ["a","b","a","c","b","a"] -> {top_n(count_freq(["a","b","a","c","b","a"]), 2)}')
# print(f'tokens ["bb","aa","bb","aa","cc"] -> {count_freq(["bb","aa","bb","aa","cc"])}')
# print(f'tokens ["bb","aa","bb","aa","cc"] -> {top_n(count_freq(["bb","aa","bb","aa","cc"]), 2)}')