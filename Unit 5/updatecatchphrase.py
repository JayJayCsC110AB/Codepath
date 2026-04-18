import re
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
    
    def greet_player(self, player_name):
         return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    
    def set_catchphrase(self, new_catchphrase):
            specialchar = "!@#$%^&*()_+}][\\;',./|:<>?"

            # Check length
            if len(new_catchphrase) >= 20:
                print("Invalid catchphrase")
                return

            for i in new_catchphrase:
                if i in specialchar:
                    print("Invalid catchphrase")
                    return
            # If valid
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated!")
    
    def add_item(self, item_name):
        valid_items = [
            "acoustic guitar",
            "ironwood kitchenette",
            "rattan armchair",
            "kotatsu",
            "cacao tree"
        ]

        if item_name in valid_items:
            self.furniture.append(item_name)
    def print_inventory(self):
        if not self.furniture:
          return "Inventory empty"
        
        # Count each unique item using .get()
        item_counts = {}
        for item in self.furniture:
            item_counts[item] = item_counts.get(item, 0) + 1
        list = []
        for item, count in item_counts.items():
            list.append(f"{item}: {count}")
        output = ", ".join(list)
        return output
    

        
apollo = Villager("Bones" , "Eagle", "ruff it up")
print(apollo.greet_player("Villager"))
apollo.set_catchphrase("Everyday is great")
print(apollo.catchphrase)



alice = Villager("Alice", "Koala", "guvnor")
"""
print(alice.furniture)

alice.add_item("acoustic guitar")
print(alice.furniture)

alice.add_item("cacao tree")
print(alice.furniture)

alice.add_item("nintendo switch")
print(alice.furniture)
"""
  # Inventory empty

print(alice.print_inventory())

alice.furniture = ["acoustic guitar", "ironwood kitchenette", "kotatsu", "kotatsu"]
print(alice.print_inventory())  #


"""
print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 
"""


"""
understand: Make a class called catchphrase and call a player using an method called greet players
i- class objects and methods
o- returning the method greet_player
c- None
edgecase: 
In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.

Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".

Example Usage:

print(bones.greet_player("Samia"))
Example Output:

Bones: Hey there, Samia! How's it going, ruff it up!
"""