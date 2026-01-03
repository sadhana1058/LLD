class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        self.speed = 0
    
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