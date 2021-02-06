def Edit(new):
    x = open("Current.txt", "w")
    for i in new:
        x.write(i + ":" + str(new[i])+"\n")
    x.close()
    print(oRoster())
def oRoster():
    x = open("Current.txt", "r")
    lines = x.readlines()
    roster = {}
    for line in lines:
        i,j = line.split(":")
        roster[i] = float(j.split("\n")[0])
    return roster