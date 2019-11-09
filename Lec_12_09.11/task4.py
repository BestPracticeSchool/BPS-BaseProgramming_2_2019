class Film:
    def __init__(self, my_title, my_heroes, my_studio, my_url, my_cash):
        self.title = my_title
        self.heroes = my_heroes
        self.studio = my_studio
        self.url = my_url
        self.cash = my_cash
    


#LOTR = Film()
#print(LOTR.studio, LOTR.cash, LOTR.heroes)


HP1 = Film("Harry Potter", ["Hermoina", "Rhone"], "Paramount", "www.my_host.com/111223344", 125_000_000)
print(HP1.studio, HP1.heroes, HP1.cash)
HP2 = Film("Harry Potter2", ["Hermoina", "Rhone", "Hagrid"], "Paramount", "www.my_host.com/11122214", 200_000_000)
print(HP2.studio, HP2.heroes, HP2.cash)
HP3 = Film("Harry Potter3", ["Hermoina", "Rhone", "Doumbledore"], "Paramount", "www.my_host.com/145233344", 300_000_000)
print(HP3.studio, HP3.heroes, HP3.cash)
# CLASS - инструкция создания объектов
# АТРИБУТ - переменная, определенная внутри класса
# МЕТОД - функция, определенная внутри класса

