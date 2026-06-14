from abc import ABC,abstractmethod

class Bird(ABC):
    @abstractmethod
    def eat(self):
        pass
        # print(f"{self.__class__.__name__} is eating")

class FlyingBird(ABC):
    @abstractmethod
    def fly(self):
        pass

class Sparrow(FlyingBird,Bird):
    def fly(self):
        print(f"{self.__class__.__name__} is flying")
    def eat(self):
        print(f"{self.__class__.__name__} is eating")



class Penguin(Bird):
    def eat(self):
        print(f"{self.__class__.__name__} is eating")

def make_bird_fly(bird):
    bird.fly()  # Crashes for Penguin!
def make_bird_eat(bird):
    bird.eat()

make_bird_eat(Sparrow())
make_bird_fly(Sparrow())  # Works fine
make_bird_eat(Penguin())  # NotImplementedError!

# TODO: Split Bird into a Bird ABC (eat) and a FlyingBird ABC (fly).
# TODO: Sparrow implements FlyingBird, Penguin implements only Bird.