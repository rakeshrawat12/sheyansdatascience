
def changecase(func):
    
    def innerfunc():
        
        return func().upper()
        
    return innerfunc
    
    
@changecase    
def myhello():
    
    return "hello budy"
    
    
    


print(myhello())