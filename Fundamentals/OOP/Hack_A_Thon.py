base_speed=.05
class Aliens:
    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
    def attack( self , cowboys ):
        cowboys.health -= self.strength
        if 
        return self

class Cowboys:
    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
    def attack ( self , aliens ):
        aliens.health -= self.strength
        return self

Marvin = Aliens("Marvin the martian")
Clint = Cowboys("Clint Eastwood")

