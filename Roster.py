#Some of this code existed previously, but has been overhauled 
#massively to the point where it is basically new code.
import re


def Edit(target, new):
    if target == "c":
        x = open("Current.txt", "w")
    if target == "l":
        x = open("Last.txt", "w")
    for i in new:
        roles = "["
        for role in new[i][1]:
            roles += str(role) + ","
        roles = roles[:-1]+"]"
        x.write("{}:{}:{}\n".format(i, new[i][0], roles))
    x.close()
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
        line = line.strip()
        try:
            i,j,z = line.split(":")
        except:
            print(line.split(":"))
        roles = []
        for role in re.sub("(\[|\])","",z).split(","):
            roles.append(int(role))
        roster[i] = [float(j), roles]
        
    return roster

def Reset():
    roster = oRoster("d")
    Edit("c", roster)
    Edit("l", roster)