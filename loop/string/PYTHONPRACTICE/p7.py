#count upper case and lower case letter
n = input()

countlower = 0
countupper = 0

for s in n:
    if s.islower():
        countlower += 1
    elif s.isupper():
        countupper += 1

print("Uppercase:", countupper)
print("Lowercase:", countlower)