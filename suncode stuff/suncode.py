from graphics import*
import random

def main():
    win = GraphWin("Landscape", 1200, 730)
    win.setBackground("lightskyblue") #sky

#sun
    sun = Circle(Point(1200, 0), 120) 
    sun.draw(win)
    sun.setFill("gold")
    sun.setOutline("gold")
    
#sun rays
    ray1 = Line(Point(1200,0), Point(1050, 150)) 
    ray1.draw(win)
    ray1.setOutline("gold")
    ray1.setWidth(15)
    ray2 = Line(Point(1200,0), Point(1185, 200))
    ray2.draw(win)
    ray2.setOutline("gold")
    ray2.setWidth(15)
    ray3 = Line(Point(1200,0), Point(1000, 15)) 
    ray3.draw(win)
    ray3. setOutline("gold")
    ray3.setWidth(15)
    
#pathway
    pathway = Line(Point(0,730), Point(1200,730))
    pathway.draw(win)
    pathway.setOutline("grey")
    pathway.setWidth(500)
    
#stalks
    stalk1 = Line(Point(800, 500), Point(800, 700))
    stalk1.draw(win)
    stalk1.setOutline("green")
    stalk1.setWidth(20)
main()
