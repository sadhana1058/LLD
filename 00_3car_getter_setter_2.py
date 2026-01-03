class car:
    def __init__(self,brand,model):
        self._brand = brand
        self._model = model
        self._speed = 0
    #method 1 
    @property
    def banana(self):
        return self._brand
    
    @banana.setter
    def banana(self,b):
        if not b:
            raise ValueError('Brand name cannot be empty string')
        else:
            self._brand = b
    
    # #method 2
    # def set_brand(self, brand):
    #     if not brand:
    #         raise ValueError('Brand name cannot be empty string')
    #     else:
    #         self._brand = brand
    
    def accelerate(self,increment):
        self._speed += increment

    def display_status(self):
        print("------Car------")
        print('model : ',self._model)
        print('brand : ',self._brand)
        print('speed : ',self._speed ,"km/h")
        print("---------------")
objcar =car('Suzuki','Omni')
objcar.accelerate(20)
objcar.display_status()
objcar.banana = 'SuZuKi'
objcar.display_status()