letters = input().split()
a, b, c = integers.split()
a = int(a)
b = int(b)
C = int(c)

if a > b:
    a, b = b, a
if c < b:
    c, b = b, c
if a > b:
    a, b = b, a
print(f"{a}, {b}, {c}")