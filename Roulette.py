from random import randrange
from Graphics import *

def thetablebasics():

# Defines coordinates and strings in order to set up window.
    x1 = 80
    x2 = 700
    x3 = 180
    y1 = 220
    y2 = 80
    y3 = 500
    win = GraphWin("Roulette-Lite", 1000, 800)
    win.setBackground("Black")
    board = Rectangle(Point(80,500),Point(700,80))
    board.setFill("green")
    board.draw(win)
    Rx1 = [0,0,80,0,80,80]
    Rx2 = [1000,705,700,80,700,700]
    Ry1 = [0,0,500,150,500,80,]
    Ry2 = [550,550,80,450,550,20]
    RC = ["white","saddlebrown","green","green","green","green",]
    index1 = 0

# Index Loops that displays the table and its various parts
    for i in range(6):
        xtrarecs = Rectangle(Point(Rx1[index1],Ry1[index1]),Point(Rx2[index1],Ry2[index1]))
        xtrarecs.setFill(RC[index1])
        xtrarecs.draw(win)
        index1 += 1
    for x in range(2):
        hline = Line(Point(x1,y1),Point(x2,y1))
        hline.setFill("white")
        hline.draw(win)
        y1 += 150
    for x in range(5):
        vline = Line(Point(x3, y3), Point(x3, y2))
        vline.setFill("white")
        vline.draw(win)
        x3 += 105

# Hardcoded / looped lines to separate specific rectangles
    vline2 = Line(Point(0,300),Point(80,300))
    vline2.setFill("white")
    vline2.draw(win)
    vline3 = Line(Point(390,20),Point(390,80))
    vline3.setFill("white")
    vline3.draw(win)
    x4 = 285
    for x in range(2):
        vline4 = Line(Point(x4,500),Point(x4,550))
        vline4.setFill("white")
        vline4.draw(win)
        x4 += 210
    vline5 = Line(Point(390,500),Point(390,550))
    vline5.setFill("white")
    vline5.draw(win)

    return win

def wheelstill():
    #This just makes sure that there is a wheel at all times
    wheelstill = Image(Point(850,300), "wheelstill.gif")
    wheelstill.draw(win)

    return win

def sceneAssests():
    # Lists that will be used in order to index loop board details onto the window
    nx = [130, 130, 130, 230, 230, 230, 330, 330, 330, 440, 440, 440, 545, 545, 545, 650, 650, 650,230,545,180,600,335,442,40,40]
    ny = [430, 300, 150, 430, 300, 150, 430, 300, 150, 430, 300, 150, 430, 300, 150, 430, 300, 150,50,50,525,525,525,525,230,375]
    color = ["red","black","red","black","red","black","red","black","red","red","black","red","black","red","black",
             "red","black","red","white","white","white","white","black","red","black","black"]
    numberstr = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18",
                 "1-9","10-18","EVEN","ODD","BLACK","RED","00","0"]
    index = 0

    #index loop for displaying every number and text on the board
    for i in range(26):
        numbers = Text(Point(nx[index],ny[index]),numberstr[index])
        numbers.setFill(color[index])
        numbers.draw(win)
        index += 1

    # Sets up more lists for corners to index loop off of
    cx = [180, 180, 285, 285, 390, 390, 495, 495, 600, 600]
    cy = [220, 370, 220, 370, 220, 370, 220, 370, 220, 370]
    ctext = ["C1","C2","C3","C4","C5","C6","C7","C8","C9","C10"]
    index = 0

    # Index loop that picks off from the lists above and displays corner choices onto the window
    for i in range(10):
        cornors = Circle(Point(cx[index], cy[index]), 20)
        cornors.setFill("purple")
        cornors.draw(win)
        Ctext = Text(Point(cx[index], cy[index]),ctext[index])
        Ctext.setFill("black")
        Ctext.draw(win)
        index += 1

    # Establishes more shapes onto window
    box = Rectangle(Point(900,450), Point(800,500))
    box.setFill("blue")
    box.draw(win)


    #Establishes many variables for the code to index off of
    Ptext = ["You can pick a corner here","Here you can pick a number or number range",
             "Here you can pick either BLACK or RED","Here you can pick either EVEN or ODD",
             "Spin!","How to play: Simply input the amount of money\n   you wish to bet (in whole dollars)"
             " hit bet! then spin!",
             "Welcome to Roulette-Lite!","Left box for location right box for amount\nif you want, leave left box(es) blank \n "
            "if don't want to bet at all. Additionally, if you \n don't want to bet place a 0 on each right box.","Bet","Bet","Bet","Bet"]
    Px = [450,800,800,450,850,170,170,150,450,450,795,795]
    Py = [600,600,700,700,475,650,600,720,665,765,665,765]
    Pcolor = ["white","white","white","white","black","white","white","white","black","black","black","black"]
    index = 0

    #hard-coded index loop
    for i in range(12):
        Playtext = Text(Point(Px[index],Py[index]), Ptext[index])
        Playtext.setFill(Pcolor[index])
        Playtext.draw(win)
        index += 1

    Betbox = Rectangle(Point(575, 720), Point(650, 770))
    Betbox.setFill("White")
    Betbox.draw(win)
    bets = Text(Point(614, 745), "BET!")
    bets.setFill("gold")
    bets.draw(win)

    return win

def userInputsAssests():

    blackBox1 = Rectangle(Point(300,565), Point(550,585))
    blackBox1.setFill("black")
    blackBox1.draw(win)

    blackBox2 = Rectangle(Point(650,665), Point(900,685))
    blackBox2.setFill("black")
    blackBox2.draw(win)

    blackBox3 = Rectangle(Point(350, 665), Point(510,685))
    blackBox3.setFill("black")
    blackBox3.draw(win)

    blackBox4 = Rectangle(Point(630,565),Point(980,585))
    blackBox4.setFill("black")
    blackBox4.draw(win)

    blackBox5 = Rectangle(Point(518,645), Point(703,665))
    blackBox5.setFill("black")
    blackBox5.draw(win)

    # Entry boxes for the player to type in are displayed

    global cornorloc, cornoramt, colorloc, coloramt, EoOloc, EoOamt, numsloc, numsamt
    cornorloc = Entry(Point(410,630),5)
    cornorloc.draw(win)
    cornoramt = Entry(Point(490, 630), 5)
    cornoramt.draw(win)
    EoOloc = Entry(Point(410, 730), 5)
    EoOloc.draw(win)
    EoOamt = Entry(Point(490, 730), 5)
    EoOamt.draw(win)
    numsloc = Entry(Point(760, 630), 5)
    numsloc.draw(win)
    numsamt = Entry(Point(830, 630), 5)
    numsamt.draw(win)
    colorloc = Entry(Point(760, 730), 5)
    colorloc.draw(win)
    coloramt = Entry(Point(830, 730), 5)
    coloramt.draw(win)



    return win

def getChoice():
    # Sets up placeholding variables in order to be replaced later on in the function
    check = 0
    mousepoint = win.getMouse()
    Mousex = mousepoint.getX()
    Mousey = mousepoint.getY()
    corner_location = color_location = EvenorOdd_location = number_location = ""
    corner_amount = color_amount = EvenorOdd_Amount = number_amount = 0


    # Sets up the mouse collision for storing betting amount and where the player wants to bet
    if Mousex < 650 and Mousey > 720 and Mousex > 575 and Mousey < 770:
        check += 1

    # Stores both the players input for how much they want to bet and where they place their bet(s).
    if check >= 1:
        corner_location = str(cornorloc.getText())
        corner_amount = int(cornoramt.getText())
        color_location = str(colorloc.getText())
        color_amount = int(coloramt.getText())
        EvenorOdd_location = str(EoOloc.getText())
        EvenorOdd_Amount = int(EoOamt.getText())
        number_location = str(numsloc.getText())
        number_amount = int(numsamt.getText())

    return corner_location, corner_amount, color_location, color_amount, EvenorOdd_location, EvenorOdd_Amount, number_location, number_amount

def inputValidation(corner_location, corner_amount, color_location, color_amount, evenorOdd_location, evenorOdd_amount, number_location, number_amount):
    number_valid = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
                    "16", "17", "18", "0", "00", "1-9", "10-18", "placeholder1"]
    evenorOdd_valid = ["", "EVEN", "Even", "even", "ODD", "Odd", "odd", "placeholder2"]
    color_valid = ["", "RED", "Red", "red", "BLACK", "Black", "black", "placeholder3"]
    corner_LocValid = ["", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "placeholder4"]
    index = valid = 0
    while number_location != number_valid[index]:
        if number_location == number_valid[index]:
            validNumberSig = Text(Point(790, 580), "VALID # OR # RANGE INPUT")
            validNumberSig.setFill("limegreen")
            validNumberSig.draw(win)
            valid += 1
            break
        elif index == 23:
            Invalidtext = Text(Point(790, 580), "INVALID NUMBER OR NUMBER RANGE")
            Invalidtext.setFill("red")
            Invalidtext.draw(win)
            break
        index+=1
    index = 0
    while evenorOdd_location != evenorOdd_valid[index]:
        if evenorOdd_location == evenorOdd_valid[index]:
            validEoOSig = Text(Point(450, 680), "VALID INPUT")
            validEoOSig.setFill("limegreen")
            validEoOSig.draw(win)
            valid += 1
            break
        elif index == 7:
            Invalidtext = Text(Point(450, 680), "INVALID INPUT")
            Invalidtext.setFill("red")
            Invalidtext.draw(win)
            break
        index+=1
    index = 0
    while color_location != color_valid[index]:
        if color_location == color_valid[index]:
            validColorSig = Text(Point(790, 680), "VALID COLOR INPUT")
            validColorSig.setFill("limegreen")
            validColorSig.draw(win)
            valid += 1
            break
        elif index == 7:
            Invalidtext = Text(Point(790, 680), "INVALID COLOR INPUT")
            Invalidtext.setFill("red")
            Invalidtext.draw(win)
            break
        index+=1
    index = 0
    while corner_location != corner_LocValid:
        if corner_location == corner_LocValid[index]:
            validCornerSig = Text(Point(450, 580), "VALID CORNER INPUT")
            validCornerSig.setFill("limegreen")
            validCornerSig.draw(win)
            valid += 1
            break
        elif index == 11:
            Invalidtext = Text(Point(450, 580), "INVALID CORNER INPUT")
            Invalidtext.setFill("red")
            Invalidtext.draw(win)
            break
        index+=1


    if int(corner_amount) + int(color_amount) + int(evenorOdd_amount) + int(number_amount) > int(user.money):
        validText = Text(Point(610,655),"LOWER BET AMOUNT(S)")
        validText.setFill("red")
        validText.draw(win)

    elif int(corner_amount) + int(color_amount) + int(evenorOdd_amount) + int(number_amount) < int(user.money):
        valid += 1

    if valid == 5:
        Validtext = Text(Point(614,655),"Lookin good!")
        Validtext.setFill("limegreen")
        Validtext.draw(win)

    elif valid != 5:
        time.sleep(3)
        userInputsAssests()
        corner_location, corner_amount, color_location, color_amount, evenorOdd_location, evenorOdd_amount, number_location, number_amount = getChoice()
        inputValidation(corner_location, corner_amount, color_location, color_amount, evenorOdd_location,
                        evenorOdd_amount, number_location, number_amount)

    return win

class player:
    # Sets up blueprint for player class
    def __init__(self, name, money):
        self.name = name
        self.money = money

    # Sets up display money
    def displaymoney(self):
        if self.money > 0:
            print(self.money)

    def displayname(self):
        if self.name > 0:
            print(self.name)

def wheelspin():
    # Sets up the amount of slots where the ball can roll into
    wheelpoints = ["0","00","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]

    # Collects the mouse data when wheelspin() is triggered
    mousepoint = win.getMouse()
    Mousex = mousepoint.getX()
    Mousey = mousepoint.getY()


    # Sets up detection for the spin button in order to spin the wheel
    if Mousex < 900 and Mousey > 450 and Mousex > 800 and Mousey < 500:
        spin = randrange(0,19)
        spinnum = wheelpoints[spin]
        cycle = 0
    # Sets up an animation cycle with sprites
        while cycle < 3:
            wheelspin = Image(Point(850, 300), "Spinningwheel.gif")
            wheelspin.draw(win)
            time.sleep(0.2)
            wheelspin = Image(Point(850, 300), "Wheelcycle1.gif")
            wheelspin.draw(win)
            time.sleep(0.2)
            wheelspin = Image(Point(850, 300), "Wheelcycle2.gif")
            wheelspin.draw(win)
            time.sleep(0.2)
            wheelspin = Image(Point(850, 300), "Wheelcycle3.gif")
            wheelspin.draw(win)
            cycle += 0.6

    # Displays the wheel spin roll onto window and right above the wheel
        time.sleep(1)
        numdisplay = Text(Point(850,150),spinnum)
        numdisplay.setFill("purple")
        numdisplay.draw(win)
        time.sleep(2.5)
        numdisplay.undraw()

        return spinnum

def cornerBet(spinnum, corner_location, corner_amount):

    if corner_location == '' or str(spinnum) == "00" or str(spinnum) == "0":
        corner_amount = 0
        return corner_amount

    else:
        EoO = int(corner_location[1]) % 2

    index1 = 1
    index2 = 0
    index3 = 2
    oddList = [1,3,5,7,9]
    evenList = [2,4,6,8,10]
    if EoO == 1:
        while int(corner_location[1]) != oddList[index2]:
            index3 += 1
            index2 += 1
            index1 += 1
        topLeft = int(corner_location[1]) + index3
        bottomLeft = int(corner_location[1]) + index1
        topRight = topLeft + 3
        bottomRight = bottomLeft + 3


    else:
        while int(corner_location[1]) != evenList[index2]:
            index1 -= 1
            index2 += 1
        topLeft = int(corner_location[1]) + index2
        bottomLeft = int(corner_location[1]) - index1
        topRight = topLeft + 3
        bottomRight = bottomLeft + 3

    if int(spinnum) == topLeft or int(spinnum) == topRight or int(spinnum) == bottomLeft or int(spinnum) == bottomRight:
        corner_amount = corner_amount * 8
        return corner_amount
    else:
        corner_amount = 0
        return corner_amount

def eoOBet(spinnum, evenorOdd_location, evenorOdd_amount):
    index = 0
    eoOlist = ["EVEN", "Even", "even","ODD", "Odd", "odd"]

    if evenorOdd_location == '' or str(spinnum) == "00" or str(spinnum) == "0":
        evenorOdd_amount = 0
        return evenorOdd_amount

    while evenorOdd_location != eoOlist[index]:
        index+=1

    if index >= 0 and index < 4:
        if (int(spinnum) % 2) == 0:
            evenorOdd_amount *= 2
            return evenorOdd_amount
        else:
            evenorOdd_amount = 0
            return evenorOdd_amount
    else:
        if (int(spinnum) % 2) == 1:
            evenorOdd_amount *= 2
            return evenorOdd_amount
        else:
            evenorOdd_amount = 0
            return evenorOdd_amount

def numbersBet(spinnum, number_location, number_amount):
    index = index2 = 0
    if number_location == '':
        number_amount = 0
        return number_amount
    numList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
               "16", "17", "18", "0", "00", "1-9", "10-18"]

    while number_location != numList[index]:
        index += 1
    while str(spinnum) != numList[index2]:
        index2 += 1

    if index == index2:
        number_amount *= 35
        return number_amount

    elif number_location == "1-9":
        if (index2 - 9) < 0:
            number_amount *= 2
            return number_amount
        else:
            number_amount = 0
            return number_amount

    elif number_location == "10-18":
        if (index2 - 9) >= 0:
            number_amount *= 2
            return number_amount
        else:
            number_amount = 0
            return number_amount
    else:
        numbers_amount = 0
        return numbers_amount

def colorsBet(spinnum, color_location, color_amount):
    index = 0
    orderedColorList = ["1","3","5","7","9","10","12","14","16","18","2","4","6","8","11","13","15","17"]
    colorList = ["RED", "Red", "red", "BLACK", "Black", "black"]
    if color_location == '' or str(spinnum) == "00" or str(spinnum) == "0":
        color_amount = 0
        return color_amount

    while color_location != colorList[index]:
        index += 1
    translate = orderedColorList.index(str(spinnum))
    if index < 3:
        if translate < 10:
            color_amount *= 2
            return color_amount
        else:
            color_amount = 0
            return color_amount
    else:
        if translate > 9:
            color_amount *= 2
            return color_amount
        else:
            color_amount = 0
            return color_amount

def readFile():
    #reads the input file by using a loop
    inFile = open("Input-Users.txt", "r")
    fileString = inFile.readline()
    lineSplit = fileString.split()
    name = (lineSplit[0])
    money = (lineSplit[1])
    user = player(str(name), int(money))
    return user

def modifyFile(user):

    # Sets the name of the outfile
    outputFile = open("Output-Users.txt", "w")
    outputFile.write("{} {}".format(user.name, user.money))

if __name__=='__main__':
    # defines which turn it is among the players
    user = readFile()
    win = thetablebasics()
    wheeldetails = wheelstill()
    sceneAssests = sceneAssests()
    userInput = userInputsAssests()
    corner_location, corner_amount, color_location, color_amount, evenorOdd_location, evenorOdd_amount, number_location, number_amount = getChoice()
    inputValidation(corner_location, corner_amount, color_location, color_amount, evenorOdd_location, evenorOdd_amount, number_location, number_amount)
    user.money = user.money - (corner_amount + evenorOdd_amount + number_amount + color_amount)
    spinnum = wheelspin()
    corner_amount = cornerBet(spinnum, corner_location, corner_amount)
    evenorOdd_amount = eoOBet(spinnum, evenorOdd_location, evenorOdd_amount)
    number_amount = numbersBet(spinnum, number_location, number_amount)
    color_amount = colorsBet(spinnum, color_location, color_amount)
    user.money = user.money + corner_amount + evenorOdd_amount + number_amount + color_amount
    modifyFile(user)
    win.getMouse()
    win.close()
