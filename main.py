from rooms import hallway, kitchen, living_room

def clean_command(command):
  return command.strip().lower()

playing = True
current_room = hallway
has_key = False
music_box_played = False
turned_tv_on = False
search_sofa = False
inventory = []
has_apple = True

print("""
THE HOUSE IN THE RAIN

You step into an old house to escape the rain.
The front door clicks shut behind you. The handle will not turn.
Somewhere inside, a floorboard creaks.
A note on a dusty table reads: "The spare key is still in the house. Look carefully."

Find the key and unlock the front door.
Type 'help' to see the commands, or 'look around' to explore.
""")

while playing:
  print("")
  command = input("What do you want to do?\n")

  cleaned_command = clean_command(command)

  if cleaned_command == "look around":
    current_room.describe()
  
  elif cleaned_command == "inventory":
    print(f"Your Inventory:{inventory}")
  
  elif cleaned_command == "help":
    if not "apple" in inventory:
      print("Commandlist:\n  look around\n  inventory\n  go living room\n  go kitchen\n  go hallway\n  search sofa\n  search tv\n  search closet\n  open door\n  search pantry\n  search fridge\n\n  help\n  quit")
    elif "apple" in inventory:
      print("Commandlist:\n  look around\n  inventory\n  go living room\n  go kitchen\n  go hallway\n  search sofa\n  search tv\n  search closet\n  open door\n  search pantry\n  search fridge\n  eat apple\n\n  help\n  quit")
  
  elif cleaned_command == "open door":
    if current_room is hallway and not has_key:
      print("The door is locked. You need a key to open it.")
    elif current_room is hallway and has_key:
      print("""You opened the door and escaped!
You step back into the rain, the key still warm in your hand.
Behind you, someone chuckles.

“Leaving already?”

You turn, but the hallway is empty.
The door closes softly. This time, you hear no lock.""")
      playing = False
    else:
      print("There is no exit door here.")

  elif cleaned_command == "search pantry":
    if current_room is kitchen and has_key == False:
      print("You found a shiny key in the pantry!")
      has_key = True
      inventory.append("Key")
    elif current_room is kitchen and has_key == True:
      print("Just some conserves in here.")
    else:
      print("There is no pantry in here.")

  elif cleaned_command == "search fridge":
    if not "apple" in inventory and current_room is kitchen and has_apple == True:
      has_apple = False
      print("You found a apple in the fridge. You put it in your bag")
      inventory.append("apple")
    elif current_room is kitchen and has_apple == False:
      print("The fridge is empty.")
    else:
      print("There is no fridge in here.")

  elif cleaned_command == "eat apple":
    if "apple" in inventory:
      inventory.remove("apple")
      print("It was sweet and fresh...how?...if nobody is in that house?")
    elif not "apple" in inventory:
      print("There is no apple in your bag.")

  elif cleaned_command == "search sofa":
    if current_room == living_room and search_sofa == False:
      search_sofa = True
      print("Between the cushions, you find a crumpled note: “The house enjoys having visitors.”")
    elif current_room == living_room and search_sofa == True:
      print("Just crumbles and dust.")
    else:
      print("There is no sofa in here.")

  elif cleaned_command == "search tv":
      if current_room == living_room and turned_tv_on == False:
        turned_tv_on = True
        print("You find a remote with no batteries. You press a button anyway. The screen flashes: ”THANK YOU FOR VISITING.”")
      elif current_room == living_room and turned_tv_on == True:
        print("Nothing happens.")
      else:
        print("There is no TV in here.")

  elif cleaned_command == "search closet":
      if current_room == hallway and music_box_played == False:
        music_box_played = True
        print("A tiny music box plays three notes. Then you hear a quiet giggle.")
      elif current_room == hallway and music_box_played == True:
        print("You open the music box again. This time, it remains silent.")
      else:
        print("There is no closet in here.")

  elif cleaned_command == "go hallway":
    current_room = hallway
    current_room.describe()
  elif cleaned_command == "go kitchen":
    current_room = kitchen
    current_room.describe()
  elif cleaned_command == "go living room":
    current_room = living_room
    current_room.describe()
  
  elif cleaned_command == "quit":
    playing = False
    print("You have quit the game. Goodbye!")
  
  else:
    print("Unknown command. Try 'look around' or 'open door'.")

