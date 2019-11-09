class Auto:
    def __init__(self, mark="Audi", max_speed=300, power=300, rate=5, lvl=4, price=10_000_000):
        self.mark = mark
        self.max_speed = max_speed
        self.power = power
        self.rate = rate
        self.lvl = lvl
        self.price = price 

    def efficency(self):
        return self.price * self.lvl / self.rate 

    def max_distance(self):
        return  self.max_speed/(2 * self.price)

bmw = Auto("BMW", 320, 440, 4.9, 3.5, 4_500_000)
stock = Auto()
print("BMW: ", bmw.efficency(), "%", bmw.max_distance(), "km")
print("Audi: ", stock.efficency(), "%", stock.max_distance(), "km")