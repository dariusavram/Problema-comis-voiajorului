import random
import matplotlib.pyplot as plt
import numpy as np



plt.style.use('_mpl-gallery')

class GeneticAlgorithm:
    def __init__(self, orase, sediu, populatie, cale_fisier):
        self.orase = orase
        self.sediu = sediu
        self.populatie = populatie
        self.matrice_distante = self.load_distances(cale_fisier)
        self.generatii = []

    def load_distances(self, cale_fisier):
        matrice = []
        with open(cale_fisier, 'r') as fisier:
            fisier.readline()
            for linie in fisier:
                matrice.append(list(map(int, linie.split())))
        return matrice

    def genereaza_populatie_initiala(self):
        populatie_initiala = []
        for _ in range(self.populatie):
            orase_shuffle = self.orase.copy()
            random.shuffle(orase_shuffle)
            populatie_initiala.append((orase_shuffle, self.calculeaza_fitness(orase_shuffle)))
        return populatie_initiala

    def calculeaza_fitness(self, ruta):
        suma = 0
        ruta_completa = [self.sediu] + ruta + [self.sediu]
        for i in range(len(ruta_completa) - 1):
            x = self.orase.index(ruta_completa[i]) if ruta_completa[i] != self.sediu else -1
            y = self.orase.index(ruta_completa[i + 1]) if ruta_completa[i + 1] != self.sediu else -1
            suma += self.matrice_distante[x][y]
        return suma

    def turnir(self, generatie, k=2):
        competitori = random.sample(generatie, k)
        return min(competitori, key=lambda x: x[1])[0]

    def incrucisare(self, parinte1, parinte2):
        punct1 = random.randint(1, len(parinte1) - 1)
        copil1 = parinte1[:punct1] + [x for x in parinte2 if x not in parinte1[:punct1]]
        copil2 = parinte2[:punct1] + [x for x in parinte1 if x not in parinte2[:punct1]]
        return copil1, copil2

    def mutatie(self, individ, sansa_mutatie):
        if random.randint(0, 100) < sansa_mutatie:
            pozitie1 = random.randint(0, len(individ) - 1)
            pozitie2 = random.randint(0, len(individ) - 1)
            while pozitie1 == pozitie2:
                pozitie2 = random.randint(0, len(individ) - 1)
            individ[pozitie1], individ[pozitie2] = individ[pozitie2], individ[pozitie1]

    def evolueaza_generatie(self, sansa_mutatie):
        sursa_generatie = sum(self.generatii, [])
        urmasi = []
        while len(urmasi) < self.populatie:
            parinte1 = self.turnir(sursa_generatie)
            parinte2 = self.turnir(sursa_generatie)
            copil1, copil2 = self.incrucisare(parinte1, parinte2)
            self.mutatie(copil1, sansa_mutatie)
            self.mutatie(copil2, sansa_mutatie)
            urmasi.append((copil1, self.calculeaza_fitness(copil1)))
            urmasi.append((copil2, self.calculeaza_fitness(copil2)))
        urmasi.sort(key=lambda x: x[1])
        return urmasi[:self.populatie]

    def ruleaza_generatii(self, numar_generatii, sansa_mutatie):
        generatie_curenta = self.genereaza_populatie_initiala()
        self.generatii.append(generatie_curenta)
        for i in range(numar_generatii):
        #    print(f"\nGenerația {i + 1}:")
            for individ, fitness in generatie_curenta:
                ruta_completa = [self.sediu] + individ + [self.sediu]
         #       print(f"Individ: {ruta_completa} | Fitness: {fitness}")

            generatie_curenta = self.evolueaza_generatie(sansa_mutatie)
            self.generatii.append(generatie_curenta)

            if len(self.generatii) > 3:
                self.generatii.pop(0)

        toate_generatiile = sum(self.generatii, [])
        cel_mai_bun = min(toate_generatiile, key=lambda x: x[1])
        ruta_completa = [self.sediu] + cel_mai_bun[0] + [self.sediu]
        print(f"\nCea mai bună soluție după {numar_generatii} generații:")
        print(f"Rută: {ruta_completa} | Fitness: {cel_mai_bun[1]}")


# Example usage
orase = ["București", "Cluj", "Timișoara", "Iași", "Constanța", "Craiova", "Brașov", "Galați", "Ploiești", "Oradea"]
sediu = "Baia Mare"
populatie = 200
cale_fisier = 'distante.txt'

algoritm = GeneticAlgorithm(orase, sediu, populatie, cale_fisier)

numar_generatii = 3000
sansa_mutatie = 5
algoritm.ruleaza_generatii(numar_generatii, sansa_mutatie)

