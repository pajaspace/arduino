from easygui import *
import easygui
image = "anemometr.gif"
msg = "Vitejte v programu anemometr"
choices = ["Yes - strasne moc chci merit ", "No", "No opinion"]
reply = buttonbox(msg, image=image, choices=choices, title="Toz vitajte...")
hod = 0  # osetreni startu , hod = 0
message = "What does she say?"
title = ""
if boolbox(message, title, ["She loves me", "She loves me not"]):
  print ('Flowers')
else: print ('Picu')
