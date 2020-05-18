import re

n = int(input())

for i in range(n):
    l=input()
    y=re.findall(r'(?<!^)(#[0-9a-f]{6}|#[0-9a-f]{3})\b',l,flags=re.I)
    for i in y:
        print(i)

