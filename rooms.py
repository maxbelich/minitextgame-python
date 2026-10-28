class Room:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def describe(self):
    print(self.description)

hallway = Room(name= "hallway", description = "You are in a hallway with a old wooden closet in front of you. The Door behind you is locked. You see a living room to the left and a kitchen to right.")
kitchen = Room(name= "kitchen", description = "You are in the kitchen. There is a fridge and a pantry.")
living_room = Room(name= "living room", description = "You are in the living room. There is a sofa and a TV.")