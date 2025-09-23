import re

def get_initials(name):
    words = name.split()
    initials = ""
    for word in words:
        if word:
            initials += word[0].upper()
    return initials

name = str(input('ФИО: '))
name = re.sub(r'\s+', ' ', name).strip()
print(f'Инициалы: {get_initials(name)}.')
print(f'Длина: {len(name)}')
