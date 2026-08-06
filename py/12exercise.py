# #Create a simple game character class with health, attack and heal methods
# class Kirito: 
#     def __init__(self, health, attack, heal_amount):
#         self.health = health
#         self.attack = attack
#         self.heal_amount = heal_amount

#     def attack_target (self, target):
#         target.health -= self.attack
#         return f"{target} took {self.attack} damage!"

#     def heal(self):
#         self.health += self.heal_amount
#         return f"Healed {self.heal_amount} hp!"

# kirito = Kirito(100, 15, 10)
# enemy = Kirito(80, 10 ,5 )
    
class Kirito:
    def __init__(self, name, health, attack, heal_amount):
        self.name = name
        self.health = health
        self.attack = attack
        self.heal_amount = heal_amount

    def attack_target(self, target):
        target.health -= self.attack
        return f"{self.name} attacks {target.name} for {self.attack} damage"

    def heal(self):
        self.health += self.heal_amount
        return f"{self.name} heals for {self.heal_amount} health"

kirito = Kirito("Kirito", 100, 15, 10)
enemy = Kirito("Enemy", 80, 12, 8)

print(kirito.attack_target(enemy))
print(enemy.health)
print(kirito.heal())
print(kirito.health)