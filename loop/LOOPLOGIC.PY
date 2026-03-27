#1 CALCULATE SUM OF DIGIT -->logic reaminder and divisor

def digit_sum(a: int):
    
    a = abs(a)   # negative handle
    
    total = 0    # yaha 0 se start hoga
    
    while a != 0:
        res = a % 10
        total = total + res
        a = a // 10
        10
    return total


b = int(input())
print(digit_sum(b))



#3 count 


