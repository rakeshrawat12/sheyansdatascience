#print palidrome number in given range

a, b = map(int, input().split())


for i in range(a, b+1):
    s = str(i)

    if s == s[::-1]:
        print(i, end=" ")