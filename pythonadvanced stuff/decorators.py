
# # def changecase(func):
    
# #     def innerfunc():
        
# #         return func().upper()
        
# #     return innerfunc
    
    
# # @changecase    
# # def myhello():
    
# #     return "hello budy"

# # def changecase(func):

# #     def innerfunc(*args, **kwargs):

# #         return func(*args, **kwargs).upper()

# #     return innerfunc
    
    
    


# # print(myhello())



# import time

# def timer(func):

#     def wrapper(*args,**kwargs):
         

#         start=time.time()
#         result=func(*args,**kwargs)
#         end=time.time()
#         print(f"{func.__name__} run in {end-start}  time")
#         return result
#     return wrapper


# @timer
# def example_function(n):
#     time.sleep(n)


# example_function(2)



#toll booth

def debug(func):

    def wrapper(*args,**kwargs):
       args_value=', '.join(str(arg) for arg in args)
       print(args_value+"helo args v")

       kwargs_value=', '.join(f"{k}={v}"for k,v in kwargs.items())

       print(kwargs_value+ "and hellke_v")

       print(f"calling:{func.__name__} with args {args_value} and kargs {kwargs_value}")


       return func(*args,**kwargs)


        

    return wrapper




@debug
def greet(name,greeting="hello"):


    print(f"{greeting}, {name}")


greet("chai")






