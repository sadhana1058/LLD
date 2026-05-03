from enum import Enum

class TrafficLight(Enum):
    RED = 30
    YELLOW = 5
    GREEN = 25
    
    

    def next(self):
        _TrafficTransitions={
        TrafficLight.RED: TrafficLight.GREEN,
        TrafficLight.GREEN: TrafficLight.YELLOW,
        TrafficLight.YELLOW: TrafficLight.RED
    }
        
        return _TrafficTransitions[self]

    def display(self):
        print(f"{self.name} light is on for {self.value} seconds.")


current_light = TrafficLight.RED
for _ in range(6):
    current_light.display()
    current_light = current_light.next()