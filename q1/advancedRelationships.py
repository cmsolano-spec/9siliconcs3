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

class Sunflower(Plants): 

  def __init__(self, name, color, height, waterstartus, number):
    super().__init__(value)
    self.number = number 
    
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
