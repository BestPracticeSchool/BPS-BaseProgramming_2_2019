class Film:
    title = "LOTR"
    heroes = ["Boromir", "Legolas", "Froddo"]
    studio = "Paramount"
    url = "www.my_host.com/1235451234"
    cash = 92_000_000


LOTR = Film()
print(LOTR.studio, LOTR.cash, LOTR.heroes)

HULK = Film()
HULK.title = "Hulk"
HULK.studio = "Marvel"
HULK.cash = 45_000_000
HULK.heroes = ["Hulk", "Bruce Banner"]
print(HULK.studio, HULK.cash, HULK.heroes)