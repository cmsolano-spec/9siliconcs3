class Plants:
  
  def __init__(self, name, color, height, waterstatus):
    self.name = value1
    self.color = value2
    self.__private_height = value3
    self.__private_waterstatus = false
    
  def waterplant(self):
    self.__private_waterstatus = true
    
  def grow(self, amount):
    return self.__private_height + amount

  def displayinfo(self):
    print(f"The name of the plant is {self.name}")
    
  def needswater(self):
    if self.__private_waterstatus is False:
      print("The plant needs to be watered")
    
Basil = Plants("Basil", color="Green", __private_height=12)
Cactus = Plants("Cactus", color="Light Green", __private_height=3)
