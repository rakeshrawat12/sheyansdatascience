#count odd and even in given digit
# write your code here


a=int(input())
a=abs(a)

a=str(a)

counteven=0
countOdd=0

for i in a:

    if (int(i))%2==0:

        counteven=counteven+1

    else:
        countOdd=countOdd+1

print(f'Even: {counteven}')
print(f'Odd: {countOdd}')