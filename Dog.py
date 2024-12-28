class Doge:
    def __init__(self, name, breed, height, fav_food):  
        self.name = name
        self.breed = breed
        self.height = height
        self.fav_food = fav_food

BullDog = Doge('Winston', 'Bull dog', 'Thirty One Centimeters', 'chicken')
print(BullDog.name)
print(BullDog.breed)
print(BullDog.height)
print(BullDog.fav_food)
