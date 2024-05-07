from turtle import *
from random import *
def findcoord(coord):
  coord = -87 + coord * 25
pencolor('black')
penup()
goto(-100, -100)
pendown()
for i in range(4):
  forward(200)
  left(90)
for i in range(4):
  forward(25)
  left(90)
  forward(200)
  right(90)
  forward(25)
  right(90)
  forward(200)
  left(90) 
left(90)
for i in range(4):
  forward(25)
  left(90)
  forward(200)
  right(90)
  forward(25)
  right(90)
  forward(200)
  left(90) 
wherex = int(input('Where? x (1-8) '))
wherey = int(input('Where? y (1-8) '))
wherex = wherex - 1
wherey = wherey - 1
wherex = findcoord(wherex)
wherey = findcoord(wherey)
listcoords = [wherex, wherey]

xbad = randrange(-87, 87, 25)
xbad1 = randrange(-87, 87, 25)
xbad2 = randrange(-87, 87, 25)
xbad3 = randrange(-87, 87, 25)
xbad4 = randrange(-87, 87, 25)
xbad5 = randrange(-87, 87, 25)
xbad6 = randrange(-87, 87, 25)
xbad7 = randrange(-87, 87, 25)
ybad = randrange(-87, 87, 25)
ybad1 = randrange(-87, 87, 25)
ybad2 = randrange(-87, 87, 25)
ybad3 = randrange(-87, 87, 25)
ybad4 = randrange(-87, 87, 25)
ybad5 = randrange(-87, 87, 25)
ybad6 = randrange(-87, 87, 25)
ybad7 = randrange(-87, 87, 25)
print(ybad6)
mine = (xbad,ybad)
mine7 = (xbad1,ybad7)
mine1 = (xbad2,ybad6)
mine2 = (xbad3,ybad5)
mine3 = (xbad4,ybad4)
mine4 = (xbad5,ybad3)
mine5 = (xbad6,ybad2)
mine6 = (xbad7,ybad1)
listmines = [mine,mine7,mine1,mine2,mine3,mine4,mine5,mine6]
print(listmines)
if listcoords in listmines:
  print('loser')
else:
  print('winner')