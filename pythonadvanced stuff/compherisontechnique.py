'''
list comprehension is a concise way to create lists in python. It
 allows you to generate a new list by applying an expression to each item in an iterable, 
 while optionally filtering items using a condition.


'''
#syntax [append for item in iterable if condition]

#list comp

evenlis=[x for x in range(1,20) if x%2==0 and x<10]

print(evenlis)


#set comp

evenset={x for x in range(1,20) if x%2==0 }

print(type(evenset))

#dict comp


squareofdictkey={x:x**2 for x in range(1,40) }
print(squareofdictkey)

