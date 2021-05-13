import pytesseract
import cv2
import PIL
import re
import Roster

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
class MatchData:
    def __init__(self,filename, first=False):
        self.won = []
        self.lose = []
        self.first = first
        im = PIL.Image.open(filename)
        width, height = im.size
        result = im.crop(((80/1037)*width, (10/625)*height, (230/1037)*width, (75/625)*height))
        team1 = im.crop(((100 / 1037) * width, (175 / 625) * height, (300 / 1037) * width, (350 / 625) * height))
        team2 = im.crop(((100 / 1037) * width, (375 / 625) * height, (300 / 1037) * width, height))
        bareFileName = filename.split("/")[-1].replace(".png", "")

        result = result.resize(newSize(result.size), PIL.Image.LANCZOS)
        team1 = team1.resize(newSize(team1.size), PIL.Image.LANCZOS)
        team2 = team2.resize(newSize(team2.size), PIL.Image.LANCZOS)

        team1.save("Matches/TempData/{}Team1.png".format(bareFileName))
        team2.save("Matches/TempData/{}Team2.png".format(bareFileName))
        result.save("Matches/TempData/{}Result.png".format(bareFileName))

        resultData = cv2.imread("Matches/TempData/{}Result.png".format(bareFileName))
        team1Data = cv2.imread("Matches/TempData/{}Team1.png".format(bareFileName))
        team2Data = cv2.imread("Matches/TempData/{}Team2.png".format(bareFileName))

        resultText = pytesseract.image_to_string(resultData)

        if resultText.__contains__("VICTORY"):
            self.winText = pytesseract.image_to_string(team1Data).split("\n")
            self.loseText = pytesseract.image_to_string(team2Data).split("\n")
        else:
            self.loseText = pytesseract.image_to_string(team1Data).split("\n")
            self.winText = pytesseract.image_to_string(team2Data).split("\n")

        self.clean()
        addHistory(self.won, self.lose, self.first)
    def clean(self):
        for i in range(len(self.winText)):
            self.winText[i] = self.winText[i].strip()
        for i in range(len(self.loseText)):
            self.loseText[i] = self.loseText[i].strip()

        self.winText = list(filter(lambda x : x != "", self.winText))
        self.loseText = list(filter(lambda x : x != "", self.loseText))

        for i in range(len(self.winText)):
            self.winText[i] = re.sub('[^A-Za-z0-9]+', '', self.winText[i])
        for i in range(len(self.loseText)):
            self.loseText[i] = re.sub('[^A-Za-z0-9]+', '', self.loseText[i])


        roster = Roster.oRoster("d")
        for i in self.winText:
            if i in roster.keys():
                self.won.append(i)
            elif i.lower() == "inpgami":
                self.won.append("Inugami")
        for i in self.loseText:
            if roster.__contains__(i):
                self.lose.append(i)
            elif i.lower() == "inpgami":
                self.lose.append("Inugami")
        print(self.winText)
        print(self.loseText)
    def __str__(self):
        return "Won: \n{}\nLose: \n{}".format(self.won, self.lose)


def addHistory(won, lost, first=False):
    with open("Matches.txt", "a") as file:
        file.write("\n")
        if first:
            file.write("\n")
        file.write("ELO(Won = {}, Lost = {}, first = {})".format(won,lost, first))

def newSize(size):
    return (size[0]*2, size[1]*2)

if __name__ == "__main__":
    MatchData("Matches/4.png", True)
