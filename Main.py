import Roster
import RosterDisplay
import Balance
import ELO
import tkinter

class ChoosePlayers:
    def __init__(self):
        self.top = tkinter.Tk()
        self.top.geometry("1000x800")
        roster = Roster.oRoster("c")
        players = sorted(list(roster.keys()))
        self.sample = []
        text = tkinter.StringVar()
        text.set("")
        label = tkinter.Label(self.top, textvariable=text)

        frame = tkinter.Frame()
        for j in range(len(players)):
            player = players[j]

            def my_func(k=player):
                self.sample.append(k)
                text.set(str(self.sample))

            a = tkinter.Button(frame, text=player, command=my_func, width=15)
            a.grid(row=j // 7, column=j % 7)
        frame.pack()
        label.pack(pady=50)

        button = tkinter.Button(self.top, text="Finish", command=self.finish)
        button.pack(pady=30)
        self.top.mainloop()

    def finish(self):
        self.top.destroy()

    def getSample(self):
        return self.sample

class BalanceTeams:
    def __init__(self, sample):
        self.sample = sample
        self.top = tkinter.Tk()
        self.first = []
        self.second = []
        self.text = tkinter.StringVar()
        self.text.set("")
        self.label = tkinter.Label(self.top, textvariable = self.text)
        self.reroll()
        self.button = tkinter.Button(self.top, text="Reroll", command=self.reroll)

        self.label.pack()
        self.button.pack(pady=20)

        done = tkinter.Button(self.top, text="Finish", command=self.finish)
        done.pack(pady=20)
        self.top.mainloop()

    def finish(self):
        self.top.destroy()
    def reroll(self):
        self.first, self.second = Balance.balanceTeams(self.sample)
        self.text.set(f"{self.first}\n{self.second}")
    def getTeams(self):
        return self.first, self.second

class ChooseWinner:
    def __init__(self, first, second):
        self.first = first
        self.second = second
        self.winner = []
        self.loser=[]
        self.top = tkinter.Tk()
        self.team1 = str(first)
        self.team2 = str(second)

        button1 = tkinter.Button(self.top, text=self.team1, command=self.team1Win)
        button2 = tkinter.Button(self.top, text=self.team2, command=self.team2Win)

        button1.pack()
        button2.pack(pady=20)
        self.top.mainloop()
    def team1Win(self):
        self.winner = self.first
        self.loser = self.second
        self.top.destroy()
    def team2Win(self):
        self.winner = self.second
        self.loser = self.first
        self.top.destroy()
    def getResult(self):
        return self.winner, self.loser

if __name__ == "__main__":
    firstTime = True
    while True:
        choose = ChoosePlayers()
        sample = choose.getSample()

        balance = BalanceTeams(sample)
        first,second = balance.getTeams()

        chooseWinner = ChooseWinner(first,second)
        winner,loser = chooseWinner.getResult()

        def addHistory(won, lost, first):
            with open("Matches.txt", "a") as file:
                file.write("\n")
                if first:
                    file.write("\n")
                file.write("ELO(Won = {}, Lost = {}, first = {})".format(won, lost, first))


        addHistory(winner, loser, firstTime)
        done = input("Done? y/n\n")
        if done == "y":
            break
        firstTime = False

