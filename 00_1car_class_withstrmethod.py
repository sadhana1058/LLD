class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.speed = 0
    def __str__(self):
        res =f"{self.brand} car of {self.model} model with speed {self.speed} km/hr. "
        return res
    
    def accelerate(self,increment):
        self.speed += increment

    def display_status(self):
        print("------Car------")
        print('model : ',self.model)
        print('brand : ',self.brand)
        print('speed : ',self.speed ,"km/h")
        print("---------------")
objcar =car('Suzuki','Omni')
objcar.accelerate(20)
objcar.display_status()
print(objcar)
## __str__ is for custom string representation of an object