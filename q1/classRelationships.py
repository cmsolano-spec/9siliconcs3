class Plants:
  
  def __init__(self, name, color, height, waterstatus):
    self.name = name
    self.color = color
    self._height = height
    self._waterstatus = waterstatus
    
  def _waterplant(self):
    self._waterstatus = True
    
  def _grow(self, amount):
    return self._height + amount

  def displayinfo(self):
    print(f"The name of the plant is {self.name}")
    print(f"The color of the plant is {self.color}")
    print(f"The height of the plant is {self._height}")
    print(f"The water status of the plant is {self._waterstatus}")
    
  def _needswater(self):
    if self._waterstatus is False:
      print("The plant needs to be watered")

class Garden:
  
  def __init__(self, name, space, cleanliness_status):
    self.name = name
    self.space = space
    self._cleanliness_status = cleanliness_status
    self.inventory = []
    
  def addplant(self, plant: Plants):
    self.inventory.append(plant)

  def removeplant(self, plant: Plants):
    self.inventory.remove(plant)
    
  def cleangarden(self):
    self._cleanliness_status = True

  def displayinfo(self):
    print(f"The name of the garden is {self.name}")
    print(f"The space of the plant is {self.space}")
    print(f"The cleanliness status of the plant is {self._cleanliness_status}")
    if not self.inventory:
      print("Related object(s): None")
    else:
      print("Related object(s):")
      for plant in self.inventory:
        print(f"- {plant.name}")


print("--- BEFORE RELATIONSHIP ---\n")
my_garden = Garden("Claire", 15, False)
basil = Plants("Basil", "Green", 12, False)
cactus = Plants("Cactus", "Light Green", 3, False)


print(f"Garden: {my_garden.name}")
for plant in my_garden.inventory:
    print(plant.name)
print("Plants in inventory: None")

print('basil = Plants("Basil", "Green",12, False)')
print('cactus = Plants("Cactus", "Light Green",3, False)\n')

print("--- BUILDING RELATIONSHIP ---\n")
print("Adding basil to my garden")
print("Adding cactus to my garden\n")
my_garden.addplant(basil)
my_garden.addplant(cactus)

print("--- AFTER RELATIONSHIP ---\n")
print(f"Garden: {my_garden.name}")
for plant in my_garden.inventory:
  print(f"Plants in store: {plant.name}")
