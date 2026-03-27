def  Sorted_list(lst:list):

    for i in range(len(lst)-1):

        if lst[i]<lst[i+1]:

            continue
        else:
            print("array is not sorted")
            
            return
    print("array is sorted")

Sorted_list([1,2,3,4,0])


# def Sorted_list(lst: list):
#     for i in range(len(lst)-1):
#         if lst[i] < lst[i+1]:
#             continue
#         else:
#             print("array is not sorted")
#             return   # 🔥 yaha exit kar diya
    
#     print("array is sorted")


# Sorted_list([1,2,3,4,0])


#left rotation


def LeftRotation(lst:list):

    firstelemnt=lst[0]

    for s in range(1,len(lst)):

        lst[s-1]=lst[s]
    lst[len(lst)-1]=firstelemnt

    print(lst)

LeftRotation([1,2,3,4])
    

    


# li=[1,2]

# print(len(li))
# print(li[len(li)-1])



#reverse list


# li=[1,2,3,4,5]

# print(li[::-1])

# b=[]


# for i in range(len(li)-1,-1,-1):

#     b.append(li[i])


# print(b)


#reverse list without using extra space

def Rev(lst:list):


    left = 0
    right = len(lst) - 1

    while left<right:


        lst[left], lst[right] = lst[right], lst[left]

        left+=1
        right-=1
    print(lst)
Rev([1,2,3,4,5])


