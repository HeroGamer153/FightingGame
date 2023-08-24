''' 
---abilities of the game---
each player has 100hp and 20 energy
punch - 5hp to the opponent, 5 energy
kick - 10hp to the opponent, 10 energy
block - blocks attack, gain 5 energy

---instructions for the game---
Once the characters, health and energy points, and the buttons have been drawn,
the user will click one of the buttons to do an action. Text will display of what
happened and the health/energy points for both characters will be updated at the 
top. The user continues pressing buttons and doing actions until one of the
characters reaches 0hp.

'''

#---import statements---
from turtle import *
import turtle as trtl
import tkinter as tk
import random as rand


#---setup & configuration---
#Lines 27-96 were written by my partner
# color list
buttonColors = ["red", "orange", "green", "blue", "violet", "gray"]

# hit points display
hp = trtl.Turtle()
hp.hideturtle()
hp.speed(0)
hp.color("red")

userHP = 100 # hit points of the user
opponentHP = 100 # hit points of the opponent

# energy display
energy = trtl.Turtle()
energy.hideturtle()
energy.speed(0)
energy.color("turquoise")

userEnergy = 20 # energy of the user
opponentEnergy = 20 # energy of the opponent

# user character
userRightHand = trtl.Turtle() # separate Turtle for the user's right hand (does the movement when punching)
userRightHand.pensize(10)
userRightHand.hideturtle()
userRightHand.speed(0)

userRightLeg = trtl.Turtle() # separate Turtle for the user's right leg (does the movement when kicking)
userRightLeg.pensize(10)
userRightLeg.hideturtle()
userRightLeg.speed(0)

# opponent character
opponentLeftHand = trtl.Turtle() # separate Turtle for the opponent's right hand (does the movement when punching)
opponentLeftHand.pensize(10)
opponentLeftHand.hideturtle()
opponentLeftHand.speed(0)

opponentLeftLeg = trtl.Turtle() # separate Turtle for the opponent's right leg (does the movement when kicking)
opponentLeftLeg.pensize(10)
opponentLeftLeg.hideturtle()
opponentLeftLeg.speed(0)

# both characters for drawing bodies
character = trtl.Turtle() # Turtle for drawing the rest of the user character
character.pensize(10)
character.hideturtle()
character.speed(0)

# button for the user to punch the opponent
punch = trtl.Turtle()
punch.hideturtle()
punch.speed(0)

# button for the user to kick the opponent
kick = trtl.Turtle()
kick.hideturtle()
kick.speed(0)

# button for the user to defend
defend = trtl.Turtle()
defend.hideturtle()
defend.speed(0)

# button for the user to gain energy
energyButton = trtl.Turtle()
energyButton.hideturtle()
energyButton.speed(0)

# default variable for the font throughout the game
fontSetup = ("Comic Sans MS", 15, "bold") 

# write text user 
textUser = trtl.Turtle()
textUser.hideturtle()
textUser.speed(0)

# write text opponent
textOpp = trtl.Turtle()
textOpp.hideturtle()
textOpp.speed(0)

# write text defend 
textDefend = trtl.Turtle()
textDefend.hideturtle()
textDefend.speed(0)

#Lines 117-269 was written by my partner
#---functions---

# write/rewrite HP levels
def writeHP():
  hp.clear()
  fontSetup = ("Comic Sans MS", 20, "bold")
  
  # user HP levels
  hp.penup()
  hp.goto(-350, 300)
  hp.pendown()

  hp.write(str(userHP), font=fontSetup)

  # opponent HP levels
  hp.penup()
  hp.goto(330, 300)
  hp.pendown()

  hp.write(str(opponentHP), font=fontSetup)

# write/rewrite energy levels
def writeEnergy():
  energy.clear()
  fontSetup = ("Comic Sans MS", 20, "bold")

  # user energy levels
  energy.penup()
  energy.goto(-275, 300)  
  energy.pendown()

  energy.write(str(userEnergy), font=fontSetup)

  # opponent energy levels
  energy.penup()
  energy.goto(275, 300)
  energy.pendown()

  energy.write(str(opponentEnergy), font=fontSetup)

# draw character without active limbs based on boolean parameter (true: user, false: opponent)
def drawCharacter(char):
  # choosing where the body would be based on the parameter
  if (char):
    bodyPosition = -150
    mirrorFactor = 0
  else: 
    bodyPosition = 150
    mirrorFactor = 300
  
  character.setheading(0)
  character.penup()
  character.goto(bodyPosition, 100)
  character.pendown()

  # draw character head
  character.begin_fill()
  character.circle(50)
  character.end_fill()

  # draw character body
  character.penup()
  character.goto(bodyPosition, 100)
  character.right(90)
  character.pendown()
  character.forward(150)

  # draw character still limbs
  character.penup()
  character.right(30 + mirrorFactor)
  character.pendown()
  character.forward(100)
  character.left(180)
  character.forward(100)
  character.left(30 + mirrorFactor)
  character.forward(85)
  character.left(135 + mirrorFactor * 3.9)
  character.forward(75)

# draw/redraw user character's active limbs
def drawUserActiveLimbs():
  userRightHand.clear()
  userRightLeg.clear()

  # draw user right hand
  userRightHand.penup()
  userRightHand.goto(-150, 35)
  userRightHand.right(45)
  userRightHand.pendown()
  userRightHand.forward(75)

  # draw user right leg
  userRightLeg.penup()
  userRightLeg.goto(-150, -50)
  userRightLeg.pendown()
  userRightLeg.right(60)
  userRightLeg.forward(100)

# draw/redraw opponent character's active limbs
def drawOpponentActiveLimbs():
  opponentLeftHand.clear()
  opponentLeftLeg.clear()

  # draw oppo3nent right hand
  opponentLeftHand.penup()
  opponentLeftHand.goto(150, 35)
  opponentLeftHand.right(135)
  opponentLeftHand.pendown()
  opponentLeftHand.forward(75)

  # draw opponent right leg
  opponentLeftLeg.penup()
  opponentLeftLeg.goto(150, -50)
  opponentLeftLeg.pendown()
  opponentLeftLeg.right(120)
  opponentLeftLeg.forward(100)

# draw button based on input of the turtle and coordinates for where the button will be
xcorList = [-200, -67.5] # list of x-coordinates for the buttons
text = ["Punch", "Kick", "Defend", "Energize"] # list of the texts used for the buttons
buttons = [punch, kick, defend, energyButton] # list of the button turtles
buttonIndex = 0
def drawButton(leftRight):
  index = 0
  global buttonIndex
  a = 1
  b = 0
  
  # change direction of drawing the buttons based on the boolean parameter
  if leftRight:
    a = -1
    b = 40

  while (index < len(xcorList)):
    # create turtle from buttons list
    turtle = buttons[buttonIndex]

    # setup and configure turtle
    turtle.hideturtle()
    turtle.penup()
    turtle.turtlesize(5)
    turtle.color("black")
    turtle.shape("square")

    # write the text
    turtle.goto((xcorList[index] - 20) * a - b, -195)
    turtle.write(text[buttonIndex], font = fontSetup)

    # draw the button
    turtle.color(buttonColors.pop(rand.randint(0, len(buttonColors)-1)))
    turtle.goto(xcorList[index] * a, -250)
    turtle.showturtle()

    index += 1
    buttonIndex += 1

def writeText(display, location):
    if(location == 1):
        textUser.clear()
        fontSetup = ("Comic Sans MS", 15, "bold")

        textUser.penup()
        textUser.goto(-200, 300)  
        textUser.pendown()

        textUser.write(display, font=fontSetup)
    elif(location == 2):
        textOpp.clear()
        fontSetup = ("Comic Sans MS", 15, "bold")

        textOpp.penup()
        textOpp.goto(-200, 275)  
        textOpp.pendown()

        textOpp.write(display, font=fontSetup)
    elif(location == 3):
        textDefend.clear()
        fontSetup = ("Comic Sans MS", 15, "bold")

        textDefend.penup()
        textDefend.goto(-200, 250)  
        textDefend.pendown()

        textDefend.write(display, font=fontSetup)


#Lines 306-315 was written by my partner
# write the final text once the game ends
def writeFinalText(display):
  finalText = trtl.Turtle()
  finalText.hideturtle()
  finalText.clear()

  finalText.penup()
  finalText.goto(-200, 225)
  finalText.pendown()

  finalText.write(display, font=fontSetup)
    
# user moves 
# punch opponent function
def punchOpponent():
    global opponentHP
    global userEnergy
    if(userEnergy >= 5):
        opponentHP -= 5
        userEnergy -= 5
        textDefend.clear()
        writeText("You punched your opponent!", 1)
    else:
        textDefend.clear()
        writeText("You don't have enough energy", 1)

# kick opponent function
def kickOpponent():
    global opponentHP
    global userEnergy
    if(userEnergy >= 10):
        opponentHP -= 10
        userEnergy -= 10
        textDefend.clear()
        writeText("You kicked your opponent!", 1)
    else:
        textDefend.clear()
        writeText("You don't have enough energy", 1)

# energize user function
def energizeUser():
    global userEnergy
    if(userEnergy <= 15):
        userEnergy += 5
        textDefend.clear()
        writeText("You energized and gained 5 energy!", 1)
    else:
        textDefend.clear()
        writeText("You reached your max energy", 1)

# opponent moves 
def punchUser():
    global userHP
    global opponentEnergy
    if(opponentEnergy >= 5):
        userHP -= 5
        opponentEnergy -= 5
        textDefend.clear()
        writeText("The opponent punched you!", 2)
    else:
        textDefend.clear()
        writeText("Your opponent didn't have enough energy", 2)

# kick user function
def kickUser():
    global userHP
    global opponentEnergy
    if(opponentEnergy >= 10):
        userHP -= 10
        opponentEnergy -= 10
        textDefend.clear()
        writeText("The opponent kicked you!", 2)
    else:
        textDefend.clear()
        writeText("Your opponent didn't have enough energy", 2)

# defend opponent function
def defendOpponent():
    global opponentEnergy
    opponentEnergy += 0

# energize opponent function
def energizeOpponent():
    global opponentEnergy
    if(opponentEnergy <= 15):
        opponentEnergy += 5
        textDefend.clear()
        writeText("Your opponent energized and gained 5 energy!", 2)
    else:
        textDefend.clear()
        writeText("The opponent has max energy", 2)

# function for when the punch button is clicked
response = ""
def punchClick(x,y):
    global response 
    response = "Punch"

# function for when the kick button is clicked
def kickClick(x,y):
    global response 
    response = "Kick"

# function for when the defend button is clicked
def defendClick(x,y):
    global response 
    response = "Defend"

# function for when the energize button is clicked
def energizeClick(x,y):
    global response 
    response = "Energize"
    

#---events---
#Lines 422-430 were written by my partner
# begin the game
writeHP()
writeEnergy()
drawCharacter(True)
drawUserActiveLimbs()
drawCharacter(False)
drawOpponentActiveLimbs()
  
drawButton(False)
drawButton(True)

# continue the game 
opponentMoves = [punchUser, kickUser, defendOpponent, energizeOpponent]

while(userHP > 0 and opponentHP > 0):
    
    defendStatusOpponent = False
    defendStatusUser = False
    
    punch.onclick(punchClick)
    kick.onclick(kickClick)
    defend.onclick(defendClick)
    energyButton.onclick(energizeClick)

    opponentMove = rand.randint(0,3)
    if(opponentMove == 2):
        defendStatusOpponent = True

    if(response.lower() == "punch" and defendStatusOpponent == False):
        punchOpponent()
    elif(response.lower() == "punch" and defendStatusOpponent == True):
        if (userEnergy >= 5):
            writeText("Your attack was defended against!", 3)
            userEnergy -= 5
        else:
            writeText("You don't have enough energy and your opponent defended", 3)
    elif(response.lower() == "kick" and defendStatusOpponent == False):
        kickOpponent()
    elif(response.lower() == "kick" and defendStatusOpponent == True):
        if (userEnergy >= 10):
            userEnergy -= 10
            writeText("Your attack was defended against!", 3)
        else:
            writeText("You don't have enough energy and your opponent defended", 3)
    elif(response.lower() == "defend"):
        defendStatusUser = True
    elif(response.lower() == "energize"):
        energizeUser()
        
    if(defendStatusUser == True):
        if(opponentMove == 0 and opponentEnergy >= 5):
            opponentEnergy -= 5
        elif(opponentMove == 1 and opponentEnergy >=10):
            opponentEnergy -= 10
        textUser.clear()
        textOpp.clear()
        writeText("You defended your opponents attack and gained 5 energy!", 3)
    elif(response != ""):
        opponentMoves[opponentMove]()
    
    if(response != ""):
        writeHP()
        writeEnergy()
    response = ""
    
# end the game when user or opponent has 0 health points 
textOpp.clear()
textUser.clear()
textDefend.clear()
if(userHP <= 0):
  writeFinalText("Sorry, you have lost :(")
elif(opponentHP <= 0):
  writeFinalText("Congratulations, you defeated your opponent!")

# keep the game going until the user exits out
wn = trtl.Screen()
wn.listen()
wn.mainloop()