import turtle
window = turtle.Screen()
window.bgcolor("lightpink")
steve = turtle.Turtle()
steve.color("green")
str_sides = input("How many sides do you want on your shape?") # takes input 
sides = int(str_sides)										   # changes input string to integer
print(sides)
for i in range (sides):
	steve.forward(50)
	steve.right(360/sides)
#steve.left(50)
#steve.right(50)
