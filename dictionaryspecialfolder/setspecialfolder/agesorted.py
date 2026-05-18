
name=["marry","john","ema"]

height=[180,165,170]
l=[]


newdict=dict(zip(name,height))
print(newdict)
print(50*"--")
print(sorted(newdict.items(),key=lambda x: x[1],reverse=True))



for d in range(len(height)):
    l.append(height[d])
    
print(sorted(l))

print(sorted(dict(zip(name,height))))