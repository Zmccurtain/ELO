import math
import numpy as np

import Roster


def ELO(Won, Lost, first=False):
    fullRoster = Roster.oRoster("c")
    roster = {}
    for name in fullRoster:
        roster[name] = fullRoster[name][0]
    if first:
        Roster.Edit("l", fullRoster)
    winTotal = 0
    for i in Won:
        if i in roster:
            winTotal += roster[i]
        else:
            winTotal += 1000
    winAverage = winTotal / 5

    loseTotal = 0
    for i in Lost:
        if i in roster:
            loseTotal += roster[i]
        else:
            loseTotal += 1000
    loseAverage = loseTotal / 5

    difference = loseAverage - winAverage
    for i in Won:
        if i in roster:
            roster[i] += f(difference)
    for i in Lost:
        if i in roster:
            roster[i] -= f(difference)
    for name in roster:
        fullRoster[name] = [roster[name], fullRoster[name][1]]
    Roster.Edit("c", fullRoster)

def f(x):
    #return (math.log(abs(x)+1) *20 + 30) - (math.log(( (abs(x)-x) /2)+1)*24 - 20)
    return (x**3)/400000000 + x**2/100000 + x/10 + 200