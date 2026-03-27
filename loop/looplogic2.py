#print prime number in range
# write your code here
# a,b = map(int(input()))
# b = int(input())
a, b = map(int, input().split())

found = False   # prime mila ya nahi

for i in range(a, b+1):
    if i > 1:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            print(i, end=" ")
            found = True

if not found:
    print("No Prime Numbers")
