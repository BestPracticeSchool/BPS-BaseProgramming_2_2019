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
    
    def full_info(self):
        return "Info: \ntitle --- {} \nname --- {}".format(self.title, self.name)


a = Event("Maxidrom", "Rammstein", 2020, "Moscow", "20:00", "1500")

print(a.full_info())
#print(b.full_info())
