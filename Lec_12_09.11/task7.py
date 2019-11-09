class Vacancy:
    def __init__(self, title="BackedDeveloper", company="", city="Moscow", cs="", sal = 100000, rs =[""], nrs = 0, ms = 150000):
        self.title = title
        self.company = company 
        self.city = city 
        self.closed_station = cs
        self.salary = sal
        self.req_skills = rs 
        self.nums_rs = nrs
        self.middle_salary = ms 

    def time_on_way(self):
        # len(closed_station) * 100 / (len(city))
        return len(self.closed_station)*100/ len(self.city)

    def efficency(self):
        # (middle_salary - salary) / middle_salary * 100
        return (self.middle_salary - self.salary) / self.middle_salary * 100

    #def yes_or_no(self):
        # efficency*time_on_way / 999999 > 150 : YES
        # NO
        

vac_1 = Vacancy()
vac_2 = Vacancy("FD", "Yandex", "SPB", "Prohorovka", 250_000, ["JS", "Vue"], 2, 180_000)

print("Vac1: ", vac_1.efficency(), vac_1.time_on_way())
print("Vac2: ", vac_2.efficency(), vac_2.time_on_way())