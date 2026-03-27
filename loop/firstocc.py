def FirstOccurrence(lst: list, key: int):
    i = 0
    j = len(lst) - 1
    ans = -1  # default agar element nahi mile

    while i <= j:
        mid = (i + j) // 2

        if lst[mid] == key:
            ans = mid
            j = mid - 1  # left side check karo pehla occurrence ke liye
        elif key > lst[mid]:
            i = mid + 1
        else:
            j = mid - 1

    if ans != -1:
        return f"First occurrence of element is at index {ans}"
    else:
        return "Element not found"

print(FirstOccurrence([1,2,2,2,3,4,5], 2))




        

