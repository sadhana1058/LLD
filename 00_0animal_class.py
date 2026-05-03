class Animal:
    def __init__(self,name,age,species):
        self.name = name
        self.age = age
        self.species = species
    
    def get_details(self):
        return f"{self.name} is a {self.age} year old {self.species}"
    
    def turned_one_year_older(self):
        self.age += 1
    
Animal1 = Animal("Buddy", 5, "Dog")
Animal2 = Animal("Mittens", 3, "Cat")
print(Animal1.get_details())
print(Animal2.get_details())
Animal1.turned_one_year_older()
print(Animal1.get_details())
