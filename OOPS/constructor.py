#constructor this is magic method that ivoked automatically whenver creating class

class Factory:

    def __init__(self,material,zipp,quantity):
        self.material=material
        self.zip=zipp
        self.quantity=quantity

    def Show_Details(self):

        
        return f"{self.material}and{self.zip}or{self.quantity}"


rebbok=Factory("leather",4,4)


adidas=Factory("nylon",5,5)

print(rebbok.material)
print(adidas.material)

print(adidas.Show_Details())



        