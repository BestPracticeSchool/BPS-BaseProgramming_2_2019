class Event:
    # Class Atributes
    example = "example"
    isNotFree = True 

    #INIT == Instance Attributes
    def __init__(self, title, name, year, city, time, price):
        self.title = title 
        self.name = name 
        self.year = year
        self.city = city 
        self.time = time 
        self.price = price 

class Kek:
    pass 


a = Event("Maxidrom", "Rammstein", 2020, "Moscow", "20:00", "1500")

print(type(a)) 
print(type("kek"))

print(a.city, a.name, a.example, a.isNotFree)

k1 = Kek()
k2 = Kek() 
print(k1,  k2)