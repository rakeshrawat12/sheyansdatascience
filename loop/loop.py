def even(lst1, lst2):

    li = []
    print(min(len(lst1), len(lst2)))

    for i in range(min(len(lst1), len(lst2))):

        s = lst1[i] + lst2[i]

        li.append(s)

    return li


result = even([1,2,3,4], [5,6,7])

print(result)