from graphics.rectfunctions import *
from graphics.cirfunctions import *
from graphics.Dgraphics.spherefunctions import *
from graphics.Dgraphics.cuboidfunctions import *
l= int(input("enter length:"))
b= int(input("enter breadth:"))
print("Rectangle Area =", RectArea(l, b))
print("Rectangle Perimeter =",RectPerimeter(l, b))
r = int(input("enter radius of circle:"))
print("Circle Area =", CircArea(r))
print("Circle Perimetetr =", CircPerimeter(r))
r = int(input("enter radius of sphere:"))
print("Sphere Area =", SpArea(r))
print("Sphere Volume =", SpPerimeter(r))
l = int(input("enter cuboid length:"))
b = int(input("enter cuboid breadth:"))
h = int(input("enter cuboid height:"))
print("Cuboid Area =", CubArea(l, b, h))
print("Cuboid Perimetetr =", CubPerimeter(l, b, h))
