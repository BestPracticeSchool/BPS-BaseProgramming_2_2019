import math as m

#Perimeter of Circle with radius = R
def len_circle(R = 1):
    return 2 * m.pi * R


#Area of Circle with radius = R
def area_circe(R = 1):
    return m.pi * R**2

#Area of Triangle with Heron's Forula
def heron_area(a = 1, b = 1, c = 1):
    p = (a + b + c) / 2
    s = (p/2 * (p/2 - a) * (p/2 - b) * (p/2 - c))**0.5 
    return s

def perim_triangle(a = 1, b = 1, c = 1):
    return a + b + c 

def circle_ratio(R = 1):
    return area_circe(R) / len_circle(R)

def triangle_ratio(a = 1, b = 2, c = 1):
    return heron_area(a,b,c) / perim_triangle(a,b,c)


#print("Ratio: ", circle_ratio(10))
#print("Ratio T: ", triangle_ratio(3,3,3))


