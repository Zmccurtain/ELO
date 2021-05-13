from PIL import ImageFont, ImageDraw, Image
import tkinter as tk
import Roster


def Borderless(week):
    Crimson = (169, 5, 51)
    lightCrimson = (237, 23, 76)
    darkCrimson = (119, 13, 41)
    Midnight = (0, 91, 148)
    DarkMidnight = (0, 57, 99)

    img = Image.new('RGB', (1000, 1000), color=DarkMidnight)
    draw = ImageDraw.Draw(img)

    draw.rectangle([(100, 100), (900, 200)], Crimson, "black")

    dic = Roster.oRoster("c")
    ldic = Roster.oRoster("l")
    for name in dic:
        dic[name] = dic[name][0]
        ldic[name] = ldic[name][0]
    font = ImageFont.truetype("JuraBook.ttf", 25)
    roster = []
    last = []

    for i in dic:
        roster.append([i, dic[i]])
        last.append(ldic[i])
    coords = []
    for i in range(50, 750, 50):
        coords.append([(100, 200 + (i - 50)), (500, 200 + i)])
    for i in range(50, 750, 50):
        coords.append([(500, 200 + (i - 50)), (900, 200 + i)])

    for i in range(len(coords)):
        if i % 2 != 0:
            draw.rectangle(coords[i], "white", "black")


        else:
            draw.rectangle(coords[i], (173, 167, 164), "black")

        if i < len(roster):
            draw.text(xy=(coords[i][0][0], coords[i][0][1] + 15),
                      text=("  " + roster[i][0] + ": " + str(int(roster[i][1]))), font=font, fill="black")
            dif = roster[i][1] - last[i]
            if dif < 0:

                downArrow(draw, coords[i][0][0] + 300, coords[i][0][1] + 20)
                draw.text((coords[i][0][0] + 325, coords[i][0][1] + 15), str(int(dif)), fill="red", font=font)
            elif dif > 0:
                upArrow(draw, coords[i][0][0] + 300, coords[i][0][1] + 20)
                draw.text((coords[i][0][0] + 325, coords[i][0][1] + 15), "+" + str(int(dif)), fill="green", font=font)

    header = ImageFont.truetype("GILBI___.ttf", 60)
    draw.text((415, 120), "Week " + str(week), font=header, fill="black")

    img.save("Weeks/" + "Week" + str(week) + ".png")
def upArrow(draw, x, y):
    draw.rectangle([(x-5*.75, y-5*.75), (x+5*.75, y+25*.75)], "green")
    draw.regular_polygon(bounding_circle=(x, y-5*.75, 15*.75), n_sides=3, fill="green")
def downArrow(draw,x,y):
    draw.rectangle([(x-5*.75, y-15*.75), (x+5*.75, y+15*.75)], "red")
    draw.regular_polygon(bounding_circle=(x, y+15*.75, 15*.75), n_sides=3, fill="red",rotation=180)

if __name__ == "__main__":
    Borderless(9)