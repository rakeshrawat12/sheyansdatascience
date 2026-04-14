def reverse(s:str):


    return s[::-1]




print(reverse("hello"))





def looplogic(st:str):

    res=""
    for s in st:

        res=s+res

    return ((res,))

print(looplogic("newjourney"))



def looplogic2(st:str):

    res=""

    for i in range(len(st),-1,-1):


        res+=i


print(looplogic("deeplearning"))



def Twopintertechnique(st: str):

    def reverse_string(sto: str):

        # string ko list me convert
        sto = list(sto)

        left = 0
        right = len(sto) - 1

        while left < right:
            # swap
            sto[left], sto[right] = sto[right], sto[left]

            # pointers move
            left += 1
            right -= 1

        return "".join(sto)

    return reverse_string(st)   # ✅ yaha argument pass kiya


print(Twopintertechnique("datanayst"))





