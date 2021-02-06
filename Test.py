def testELO(roster):
    
    Won = ["10slayer", "CyborgSteve", "AmericanHussar", "Cade", "Daniel"]
    Lost = ["ColinJH", "aijinxed","chibikitty" , "GentileBanan",  "Imperialpayload"]


    
    base = []
    for i in roster:
        base.append(i)
    for i in range(5):
        current = base[random.randint(0, len(base)-1)]
        Won[i] =  current
        base.remove(current)
    for i in range(5):
        current = base[random.randint(0, len(base)-1)]
        Lost[i] =  current
        base.remove(current)
    roster = WeightELO(Won,Lost,roster)
    return roster
 
def WeightELO(Win, Lose, roster):
    winTotal = 0
    for i in Win:
        winTotal += roster[i]
    winAverage = winTotal/5
    
    
    
    loseTotal = 0
    for i in Lose:
        loseTotal += roster[i]
    loseAverage = loseTotal/5
    
    if winAverage < loseAverage:
        Greater = Lose
        Lower = Win
        x = winAverage
        winAverage = loseAverage
        loseAverage = x
    else:
        Greater = Win
        Lower = Lose
    difference = winAverage - loseAverage
    Gprob = math.log(difference+1)/math.log(2001)
    Lprob = 1 - Gprob
    choice = random.choices([Greater,Lower], weights = [Gprob, Lprob], k = 1)
    if choice[0] == Greater:
        return ELO(Greater, Lower,roster)
    else:
        return ELO(Lower,Greater,roster)
def Distribution(roster):
    n = 2000
    change = []
    for i in range (n):
        new = testELO(roster.copy())
        for j in roster:
            if new[j] != roster[j]:
                change.append(new[j] - roster[j])
        roster = new.copy()
    
    fig, (ax1, hist) = plt.subplots(2)
    ax1.plot(change, "ro")
    hist.hist(change)
    plt.show()
def Change(roster):
    n = 2000
    change = []
    new = roster.copy()
    for i in range (n):
        testELO(new)
    for i in roster:
        change.append(roster[i]-new[i])
    
    fig, (ax1, hist) = plt.subplots(2)
    ax1.plot(change, "ro")
    hist.hist(change)
    plt.show()
def Individual(roster):
    n = 2000
    change = []
    new = roster.copy()
    for i in range (n):
        testELO(new)
    for i in roster:
        change.append(roster[i]-new[i])
    names = []
    for i in roster:
        names.append(i)
    plt.figure(figsize=(30, 3))
    plt.bar(names, change)
    plt.show()