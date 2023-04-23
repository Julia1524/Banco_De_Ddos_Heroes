from entities import Hero

class action:
    def __init__(self):
        self.listaHeroes = []

    def criarHero(self, name, power, weakness):
        hero = Hero.Hero(name,power, weakness)
        self.listaHeroes.append(hero)

    def adicionarHero(self, hero):
        self.listaHeroes.append(hero)

    def bdHero(self, var, name):
        for i in self.listaHeroes:
            if name == i.name:
                if var == "name":
                    return f'Name: {i.name}'
                elif var == "power":
                    return f'Powers: {i.powers}'
                elif var == "weakness":
                    return f'Weaknesses: {i.weakness}'
