li = [x for x in range(0,5)]

print(li)

for l in li:
    try:
        if l // 0 == 0:   # yeh hamesha error dega
            print("hello")
    except Exception as err:
        print("zero division error")


        


    