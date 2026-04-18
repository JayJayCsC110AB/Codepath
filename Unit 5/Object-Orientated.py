class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
        
    def call_dog(self):
        print(f"Here {self.name}!")
    
    def command_trick(self, trick):
        print(f"{self.name}, {trick}!")

my_dog = Dog("Rosco", "Chihauhau", "Jasem")
#my_dog.call_dog()
my_dog.command_trick("roll over") 

"""
Calling class with print statements
my_dog = Dog("Rosco", "Chihauhau", "Jasem")
print(my_dog.name)

"""