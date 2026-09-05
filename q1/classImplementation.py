class Plants:
  
  def __init__(self, name, color, height, waterstatus):
    self.name = name
    self.color = color
    self._height = height
    self._waterstatus = waterstatus
    
  def waterplant(self):
    self.__waterstatus = True
    
  def grow(self, amount):
    return self._height + amount

  def displayinfo(self):
    print(f"The name of the plant is {self.name}")
    
  def needswater(self):
    if self._waterstatus is False:
      print("The plant needs to be watered")
    
basil = Plants("Basil", "Green",12, False )
cactus = Plants("Cactus", "Light Green",3, False )

print("--- BEFORE ---")
print(f"Basil's Information: \n Name: {basil.name} \n Color: {basil.color} \n Height: {basil._height} \n Water Status: {basil._waterstatus} \n")
print(f"Cactus's Information: \n Name: {cactus.name} \n Color: {cactus.color} \n Height: {cactus._height} \n Water Status: {cactus._waterstatus} \n")

print("--- AFTER ---")
print(f"Basil's Information: \n Name: {basil.name} \n Color: {basil.color} \n Height: {basil.grow(2)} \n Water Status: {basil._waterstatus} \n")
print(f"Cactus's Information: \n Name: {cactus.name} \n Color: {cactus.color} \n Height: {cactus._height} \n Water Status: {cactus._waterstatus} ")
