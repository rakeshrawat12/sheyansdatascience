class CarFactory:

    a="BMW"
    print(a)

    def messaage(a):

        print(f"hello{a}")


bmw=CarFactory()

CarFactory.messaage("Bmw")

bmw.messaage("hello")


# class Factory:
#     a = "hello I am an attribute"
#     def hello(s):
#         print("hello I am a method")

# obj = Factory() #obj becomes an object who can access anythin inside the class till now
# obj2 = Factory()

# print(obj.a)
# obj2.hello()




