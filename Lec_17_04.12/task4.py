#OOП --- инкапсуляция, наследование, полиморфизм

# Инкапсуляция - способ хранения свойств объекта. Все свойства объекта обязаны быть собраны в единую сущность.

class Film:
    def __init__(self, title, actors, rating, duration):
        self.title = title
        self.actors = actors 
        self.rating = rating
        self.duration = duration


f = Film("LOTR", ["Boromir", "Frodo"], 10.0, 154)


# Наследование - способ переноса свойств от одного объекта к другому. 

class Figure:
    tree = "kek"
    def __init__(self, color, material):
        self.color = color + "lyqweasd"
        self.material = "[" +material +"]"

class Rectangle(Figure):
    def __init__(self,length, width, color, material):
        super().__init__(color, material)
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)



class Circle(Figure):
    def __init__(self, R, color, material):
        super().__init__(color, material)
        self.R = R
    
    def perimeter(self):
        return 2 * 3.14 * self.R

f = Figure("green", "iron")
r = Rectangle(10,20, "black", "wood")
print(f.color, f.material, f.tree)
print(r.color, r.material, r.tree)
print("Perimeter of rectangle: ",r.perimeter())

c = Circle(10, "yellow", "glass")
print("Perimeter of circle: ", c.perimeter())


# Полиморфизм - способ проявления свойств объектов.
