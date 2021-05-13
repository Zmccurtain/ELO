import numpy as np
import Roster
import math
import random


def legal(genotype):
    if len(set(genotype)) != 10:
        return False
    return True


class Evolutionary():
    def __init__(self, pop, mprob, rprob, geneSize, fitnessFunction, sampleSize):
        self.pop = np.zeros((pop, geneSize))
        self.mutatProb = mprob
        self.recomProb = rprob
        self.geneSize = geneSize
        self.fitnessFunction = fitnessFunction
        self.sampleSize = sampleSize

        self.populate()

    def populate(self):
        for i in range(len(self.pop)):
            while True:
                new = np.random.randint(self.sampleSize, size=10)
                if legal(new):
                    for j in range(self.geneSize):
                        self.pop[i][j] = new[j]
                    break
        return

    def step(self):
        a = np.random.randint(len(self.pop))
        b = np.random.randint(len(self.pop))
        while (a == b):
            b = np.random.randint(len(self.pop))
        if self.fitnessFunction(self.pop[a]) < self.fitnessFunction(self.pop[b]):
            winner = a
            loser = b
        else:
            winner = b
            loser = a
        while True:
            if np.array_equal(self.pop[loser], self.pop[winner]):
                break
            new = (self.pop[loser]).copy()
            for i in range(self.geneSize):
                if np.random.random() < self.recomProb:
                    new[i] = self.pop[winner][i]
            if legal(new):
                for j in range(self.geneSize):
                    self.pop[loser][j] = new[j]
                break

        while True:
            new = (self.pop[loser]).copy()
            for i in range(self.geneSize):
                if np.random.random() < self.mutatProb:
                    new[i] = np.random.randint(self.sampleSize)
            if legal(new):
                for j in range(self.geneSize):
                    self.pop[loser][j] = new[j]
                break

    def best(self):
        best = 10000000
        for i in self.pop:
            fitness = self.fitnessFunction(i)
            if fitness < best:
                best = fitness
        return best

    def getBest(self):
        best = 10000000
        genotype = []
        for i in self.pop:
            fitness = self.fitnessFunction(i)
            if fitness < best:
                best = fitness
                genotype = i
        return best, genotype
    def run(self, duration):
        for i in range(duration):
            self.step()





def balanceTeams(sample):
    roster = Roster.oRoster("c")

    def fit(genotype):
        roster = Roster.oRoster("c")
        Atotal = 0
        Btotal = 0

        Ahappiness = 0
        Bhappiness = 0

        totalHappiness = 0

        for i in range(10):
            index = roster[sample[int(genotype[i])]][1].index(i % 5)
            if i < 5:
                Atotal += roster[sample[int(genotype[i])]][0]
                Ahappiness += 5 - index
            else:
                Btotal += roster[sample[int(genotype[i])]][0]
                Bhappiness += 5 - index

            if index >= 3:
                totalHappiness -= 1000
            else:
                totalHappiness += 5 - roster[sample[int(genotype[i])]][1].index(i % 5)

        weightedTotalHappiness = totalHappiness
        totalDifference = abs(Atotal - Btotal)

        weightedOutput = totalDifference - weightedTotalHappiness

        return weightedOutput

    def ratingFit(genotype):
        roster = Roster.oRoster("c")
        Atotal = 0
        Btotal = 0
        for i in range(10):
            if i < 5:
                Atotal += roster[sample[int(genotype[i])]][0]
            else:
                Btotal += roster[sample[int(genotype[i])]][0]
        totalDifference = abs(Atotal - Btotal)
        return totalDifference

    pop = 40
    mprob = 0.1
    rprob = 0.5
    geneSize = 10
    sampleSize = len(sample)
    fitness = fit
    duration = 1000

    best = np.zeros(duration)
    balance = Evolutionary(pop, mprob, rprob, geneSize, fitness, sampleSize)

    balance.run(duration)

    best, genotype = balance.getBest()
    first = []
    second = []
    for i in range(geneSize):
        if i < 5:
            first.append(sample[int(genotype[i])])
        else:
            second.append(sample[int(genotype[i])])
    return first,second


