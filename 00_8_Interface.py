from abc import ABC,abstractmethod
class Animal(ABC):
    def __init__(self,l):
        self.legs=l
        self.baby=''

    @abstractmethod
    def legs_info(self,count):
        pass
    @abstractmethod
    def baby_info(self,count):
        pass

class Dog(Animal):
    def __init__(self):
        self.legs_present=4
        self.baby='puppies'
    
    def legs_info(self,count):
        self.legs_present += count
        return self.legs_present
    def baby_info(self,count):
        pass

d=Dog()
print(d.legs_info(1))
