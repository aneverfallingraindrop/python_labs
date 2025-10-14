from libs.text import *

text = input()
text = normalize(text, casefold=True, yo2e=True)
tokens = tokenize(text)
words_total = len(tokens)
unique_words = len(set(tokens))
top_5 = top_n(tokens, 5)

print(words_total)
print(unique_words)
print(top_5)