# s1="abbccdd"

# s2="abbccdd"

# if len(s1)==len(s2):


#     d={}
#     for i in s1:



#         if i in d.keys():


#             d[i]+=1

#         else:

#             d[i]=1
#     for ss in s2:

#         if  ss in d.keys():
#             d[ss]-=1

#         else:
#             print("extra element found")
#     for checkxxero in d:
#         if d[checkxxero]!=0:

#             print("sorry your elemet are not same")

#     else:
#         print('your string are same')


# else:

#     print("your length is not same=sorry")


s1 = "abbccdd"
s2 = "abbccdd"

if len(s1) == len(s2):

    d = {}

    # count from s1
    for i in s1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    # subtract using s2
    for ss in s2:
        if ss in d:
            d[ss] -= 1   # ✅ fix
        else:
            print("extra element found")
            break

    # check all zero
    for val in d.values():
        if val != 0:
            print("sorry your elements are not same")
            break
    else:
        print("your strings are same")

else:
    print("length not same")








    











for s in s1:
    
