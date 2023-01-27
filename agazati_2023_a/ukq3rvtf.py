class gombak:
    def __init__(self, sor):
        daraboltSor=sor.split("@")
        self.gombaneve = daraboltSor[0]
        self.nemzetseg = daraboltSor[1]
        self.evszak=daraboltSor[2]

    def __str__(self):
        return "Gombaneve {}, Nemzetség {}, Évszak {}.".format(self.gombaneve, self.nemzetseg, self.evszak)