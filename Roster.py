def Edit(target, new):
    if target == "c":
        x = open("Current.txt", "w")
    if target == "l":
        x = open("Last.txt", "w")
    for i in new:
        x.write(i + ":" + str(new[i])+"\n")
    x.close()
    if target=="c":
        print(oRoster("c"))
def oRoster(target):
    if target == "c":
    
        x = open("Current.txt", "r")
    elif target == "d":
        x = open("Default.txt", "r")
    elif target =="l":
        x = open("Last.txt", "r")
    lines = x.readlines()
    roster = {}
    for line in lines:
        i,j = line.split(":")
        roster[i] = float(j.split("\n")[0])
    return roster

def Reset():
    roster = oRoster("d")
    Edit("c", roster)
    Edit("l", roster)