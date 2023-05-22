print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
name=input('What is your name?\n')
print(f'Are you ready for this , {name} ?')
opt=input('yes or no?')
if opt=='yes':
  mode=input('copter or bike or boat')


  if mode==copter:
    next=input('Drop or Keep Flying')
    if next==Drop:
      then=input('stairs or lion')
      if then=='stairs':
        print('You loose!')
      else:
        print('You loose!')
    else:
       print('You loose!')

  elif mode=='bike':
    next=input('truck or house')
    if next=='truck':
      print('You ran into a truck,you loose!')
    else:
      print('You ran into a truck,you loose!')

  elif mode=='boat':
    next==input('swim or stay in the boat')
    if next==swim:
      then=input('open door or stay outside')
      if then=='open door':
        print('You found the treasure, you win!')
      else:
        print('You loose')
    else:
      print('The boat ran out of Energy,you are dead,you loose')

else:
  print('You are a coward, you loose!')
