import Roster
import Balance
import ELO
import tkinter

class MakeTeams:
    def __init__(self):
        self.top = tkinter.Tk()
        self.top.geometry("1000x800")
        self.firstTime = True
        self.sample = []
        self.text = tkinter.StringVar()
        self.choosePlayers()

    def choosePlayers(self):
        for i in self.top.winfo_children():
            i.destroy()
        self.text.set("")
        roster = Roster.oRoster("c")
        players = sorted(list(roster.keys()))
        label = tkinter.Label(self.top, textvariable=self.text)

        frame = tkinter.Frame()
        for j in range(len(players)):
            player = players[j]

            def my_func(k=player):
                self.sample.append(k)
                self.text.set(str(self.sample))

            a = tkinter.Button(frame, text=player, command=my_func, width=15)
            a.grid(row=j // 7, column=j % 7)
        frame.pack(pady=20)
        label.pack(pady=50)

        button = tkinter.Button(self.top, text="Finish", command=self.BalanceTeams)
        button.pack(pady=30)
        self.top.mainloop()

    def getSample(self):
        return self.sample

    def BalanceTeams(self):
        for i in self.top.winfo_children():
            i.destroy()
        self.first = []
        self.second = []
        self.text.set("")
        self.label = tkinter.Label(self.top, textvariable=self.text)
        self.reroll()
        self.button = tkinter.Button(self.top, text="Reroll", command=self.reroll)

        self.label.pack(pady=20)
        self.button.pack()

        done = tkinter.Button(self.top, text="Finish", command=self.ChooseWinner)
        done.pack(pady=20)
        self.top.mainloop()
    def reroll(self):
        self.first, self.second = Balance.balanceTeams(self.sample)
        self.text.set(f"{self.first}\n{self.second}")
    def getTeams(self):
        return self.first, self.second
    def ChooseWinner(self):
        for i in self.top.winfo_children():
            i.destroy()
        label = tkinter.Label(self.top, text="Who Won?")
        self.winner = []
        self.loser = []
        self.team1 = str(self.first)
        self.team2 = str(self.second)

        button1 = tkinter.Button(self.top, text=self.team1, command=self.team1Win)
        button2 = tkinter.Button(self.top, text=self.team2, command=self.team2Win)
        label.pack(pady=20)
        button1.pack()
        button2.pack(pady=20)
        self.top.mainloop()

    def team1Win(self):
        self.winner = self.first
        self.loser = self.second
        self.is_done()

    def team2Win(self):
        self.winner = self.second
        self.loser = self.first
        self.is_done()

    def is_done(self):
        for i in self.top.winfo_children():
            i.destroy()
        label = tkinter.Label(self.top, text="Are You Done?")


        label.pack()

        frame = tkinter.Frame(self.top)
        yesButton = tkinter.Button(frame, text="Yes", command=self.yes)
        noButton = tkinter.Button(frame, text="No", command=self.no)

        yesButton.pack(side=tkinter.LEFT, padx=50)
        noButton.pack(side=tkinter.LEFT,padx=50)
        frame.pack(pady=20)

    def yes(self):

        self.addHistory()
        self.top.destroy()
    def no(self):
        self.addHistory()
        self.firstTime = False
        self.sample = []
        self.choosePlayers()

    def addHistory(self):
        with open("Matches.txt", "a") as file:
            file.write("\n")
            if self.first:
                file.write("\n")
            file.write("ELO(Won = {}, Lost = {}, first = {})".format(self.winner, self.loser, self.firstTime))

if __name__ == "__main__":
    MakeTeams()


