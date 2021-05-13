if __name__ == "__main__":
    import Roster
    Roster.reset()
    with open("matches.txt") as x:
        for line in x:
            line.strip()
            if line != "":
                eval(line)