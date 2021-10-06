from random import randrange
import time
from Graphics import *

def thetablebasics():

# Defines coordinates and strings in order to set up window.
    x1 = 80
    x2 = 700
    x3 = 180
    y1 = 220
    y2 = 80
    y3 = 500
    win = GraphWin("Oneshot-Roulette", 1000, 800)
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

def boarddetails1():
    # Lists that will be used in order to index loop board details onto the window
    nx = [130, 130, 130, 230, 230, 230, 330, 330, 330, 440, 440, 440, 545, 545, 545, 650, 650, 650,230,545,180,600,335,442,40,40]
    ny = [430, 300, 150, 430, 300, 150, 430, 300, 150, 430, 300, 150, 430, 300, 150, 430, 300, 150,50,50,525,525,525,525,230,375]
    color = ["red","black","red","black","red","black","red","black","red","red","black","red","black","red","black","red","black","red","white","white","white","white","black","red","black","black"]
    numberstr = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","1-9","10-18","EVEN","ODD","BLACK","RED","00","0"]
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
    index2 = 0

    # Index loop that picks off from the lists above and displays corner choices onto the window
    for i in range(10):
        cornors = Circle(Point(cx[index2], cy[index2]), 20)
        cornors.setFill("purple")
        cornors.draw(win)
        Ctext = Text(Point(cx[index2], cy[index2]),ctext[index2])
        Ctext.setFill("black")
        Ctext.draw(win)
        index2 += 1

    return win

def playertext():

    # Establishes more shapes onto window
    box = Rectangle(Point(900,450), Point(800,500))
    box.setFill("white")
    box.draw(win)

    # Creates bet box
    Betbox = Rectangle(Point(575,720),Point(650,770))
    Betbox.setFill("White")
    Betbox.draw(win)
    bets = Text(Point(614,745),"BET!")
    bets.setFill("gold")
    bets.draw(win)

    #Establishes many variables for the code to index off of
    Ptext = ["You can pick a corner here","Here you can pick a number or number range","Here you can pick either BLACK or RED","Here you can pick either EVEN or ODD","Spin!","How to play: Simply input the amount of money\nyou wish to bet (in whole dollars) and hit spin!\nkeep in mind, you only have one shot per turn!","Welcome to Oneshot-Roulette!","Left box for location right box for amount\nif you like, you can also use x if \ndon't want to bet at all.","Bet","Bet","Bet","Bet"]
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

    # Entry boxes for the player to type in are displayed
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

    return cornorloc,cornoramt,colorloc,coloramt,EoOloc,EoOamt,numsloc,numsamt

###### START OF PLAYER CLASS ######
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
###### END OF PLAYER CLASS ######

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
            cycle +=0.6

    # Displays the wheel spin roll onto window and right above the wheel
        time.sleep(1)
        numdisplay = Text(Point(850,150),spinnum)
        numdisplay.setFill("purple")
        numdisplay.draw(win)
        time.sleep(2.5)
        numdisplay.undraw()

        return str(spinnum)

def getChoice(cornorloc,cornoramt,colorloc,coloramt,EoOloc,EoOamt,numsloc,numsamt):
        # Sets up placeholding variables in order to be replaced later on in the function
        check = 0
        mousepoint = win.getMouse()
        Mousex = mousepoint.getX()
        Mousey = mousepoint.getY()
        corner_location = "placeholder"
        color_location = "placeholder"
        corner_amount = 0
        EvenorOdd_location = "placeholder"
        color_amount = 0
        EvenorOdd_Amount = 0
        number_location = "placeholder"
        number_amount = 0

        # Sets up the mouse collision for storing betting amount and where the player wants to bet
        if Mousex < 650 and Mousey > 720 and Mousex > 575 and Mousey < 770:
            check += 1

        # Stores both the players input for how much they want to bet and where they place their bet(s).
        if check >= 1:
            corner_location = str(cornorloc.getText())
            corner_amount = (cornoramt.getText())
            color_location = str(colorloc.getText())
            color_amount = (coloramt.getText())
            EvenorOdd_location = str(EoOloc.getText())
            EvenorOdd_Amount = (EoOamt.getText())
            number_location = str(numsloc.getText())
            number_amount = (numsamt.getText())

        return corner_location, corner_amount, color_location, color_amount, EvenorOdd_location, EvenorOdd_Amount, number_location, number_amount

def validlocationcheck(corner_location, color_location, EvenorOdd_location, number_location):
    # Establishes variable line in which the code later will index from
    q,w,e,r,passing,passing_y_index,passing_x_index,gy,gx,cornerlocvalid, color_valid, EvenorOdd_valid, number_valid, index1, index2, index3, index4, strike = 1,1,1,1,0,0,0,[580,680,680,580],[450,790,450,790],["x","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","+-=_+~"],["x","RED","Red","red","BLACK","Black","black","+-=_+~","+-=_+~","+-=_+~"],["x","EVEN","Even","even","ODD","Odd","odd","+-=_+~","+-=_+~"],["placeholder","x","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","0","00","1-9","10-18","+-=_+~"],0,0,0,0,0

    # Creates a never ending loop in which is only stopped when all four location values are good
    while strike < 8:

        if passing == 1:
            greenlight = Text(Point(gx[passing_x_index], gy[passing_y_index]), "O")
            greenlight.setFill("lightgreen")
            greenlight.draw(win)

        # Displays error message if there isn't a correct input using operator index loop
        if corner_location == cornerlocvalid[index1]:
            for i in range(q):
                q,passing, passing_x_index, passing_y_index = 0, 1, 0, 0
                strike += 2


        # Displays error message if there isn't a correct input using operator index loop
        if corner_location != cornerlocvalid[index1]:
            index1 += 1
            if index1 == 11:
                strike = 1
            if strike == 1:
                Invalidtext = Text(Point(450, 580), "INVALID CORNER INPUT")
                Invalidtext.setFill("red")
                Invalidtext.draw(win)

        # Displays error message if there isn't a correct input using operator index loop
        if color_location == color_valid[index2]:
            for i in range(w):
                w,passing, passing_x_index, passing_y_index = 0, 1, 1, 1
                strike += 2

        # Displays error message if there isn't a correct input using operator index loop
        if color_location != color_valid[index2]:
            index2 += 1
            if index2 == 9:
                strike = 1
            if strike == 1:
                Invalidtext = Text(Point(790, 680), "INVALID COLOR INPUT")
                Invalidtext.setFill("red")
                Invalidtext.draw(win)

        # Displays error message if there isn't a correct input using operator index loop
        if EvenorOdd_location == EvenorOdd_valid[index3]:
            for i in range(r):
                r,passing, passing_x_index, passing_y_index = 0, 1, 2, 2
                strike += 2

        # Displays error message if there isn't a correct input using operator index loop
        if EvenorOdd_location != EvenorOdd_valid[index3]:
            index3 += 1
            if index3 == 9:
                strike = 1
            if strike == 1:
                Invalidtext = Text(Point(450, 680), "INVALID INPUT")
                Invalidtext.setFill("red")
                Invalidtext.draw(win)

        # Displays error message if there isn't a correct input using operator index loop
        if number_location == number_valid[index4]:
            for i in range(e):
                e,passing, passing_x_index, passing_y_index = 0, 1, 3, 3
                strike += 2

        # Displays error message if there isn't a correct input using operator index loop
        if number_location != number_valid[index4]:
            index4 += 1
            if index4 == 23:
                strike = 1
            if strike == 1:
                Invalidtext = Text(Point(785, 580), "INVALID NUMBER OR NUMBER RANGE")
                Invalidtext.setFill("red")
                Invalidtext.draw(win)

    return win

def validamountcheckone(one,corner_amount, color_amount, EvenorOdd_Amount, number_amount):
    # lays out the two variables needed in order to make sure that the player inputs the correct amounts
    strike,onemoney = 0,int(one.money)

    # Makes a check on all inputs for betting amounts and makes sure that it doesn't go over the limit
    while strike == 0:
        # Checks corner betting amount if the player decides to skip
        if corner_amount == "x":
            corner_amount = 0
        if corner_amount != "x":
            if int(corner_amount) >= int(onemoney):
                break
        # Checks color betting amount if the player decides to skip
        if color_amount == "x":
            color_amount = 0
        if color_amount != "x":
            if int(color_amount) >= int(onemoney):
                break
        # Checks Even or Odd betting amount if the player decides to skip
        if EvenorOdd_Amount == "x":
            EvenorOdd_Amount = 0
        if EvenorOdd_Amount != "x":
            if int(EvenorOdd_Amount) >= int(onemoney):
                break
        # Checks single number and number range betting amount if the player decides to skip
        if number_amount == "x":
            number_amount = 0
        if number_amount != "x":
            if int(number_amount) >= int(onemoney):
                break
        # Adds up every betting amount to make sure that it doesn't go over the amount of money the player has
        amount_total = int(corner_amount) + int(color_amount) + int(EvenorOdd_Amount) + int(number_amount)

        # Triggers a variable change if the betting amounts go over the amount of money the player has
        if int(amount_total) > int(onemoney):
            strike = 1

        # Displays an error message if strike, which is the error variable, is set at  1
        if strike == 1:
            Invalidtext = Text(Point(605, 650), "NOT ENOUGH MONEY")
            Invalidtext.setFill("red")
            Invalidtext.draw(win)


        # Allows the player to go on if strike is set to 0
        if int(amount_total) < int(onemoney):
            break

        return win

def validamountchecktwo(two,corner_amount, color_amount, EvenorOdd_Amount, number_amount):
    # lays out the two variables needed in order to make sure that the player inputs the correct amounts
    strike, twomoney = 0, int(two.money)

    # Makes a check on all inputs for betting amounts and makes sure that it doesn't go over the limit
    while strike == 0:
        # Checks corner betting amount if the player decides to skip
        if corner_amount == "x":
            corner_amount = 0
        if corner_amount != "x":
            if int(corner_amount) >= int(twomoney):
                break
        # Checks color betting amount if the player decides to skip
        if color_amount == "x":
            color_amount = 0
        if color_amount != "x":
            if int(color_amount) >= int(twomoney):
                break
        # Checks Even or Odd betting amount if the player decides to skip
        if EvenorOdd_Amount == "x":
            EvenorOdd_Amount = 0
        if EvenorOdd_Amount != "x":
            if int(EvenorOdd_Amount) >= int(twomoney):
                break
        # Checks single number and number range betting amount if the player decides to skip
        if number_amount == "x":
            number_amount = 0
        if number_amount != "x":
            if int(number_amount) >= int(twomoney):
                break
        # Adds up every betting amount to make sure that it doesn't go over the amount of money the player has
        amount_total = int(corner_amount) + int(color_amount) + int(EvenorOdd_Amount) + int(number_amount)

        # Triggers a variable change if the betting amounts go over the amount of money the player has
        if int(amount_total) > int(twomoney):
            strike = 1

        # Displays an error message if strike, which is the error variable, is set at  1
        if strike == 1:
            Invalidtext = Text(Point(605, 650), "NOT ENOUGH MONEY")
            Invalidtext.setFill("red")
            Invalidtext.draw(win)

        # Allows the player to go on if strike is set to 0
        if int(amount_total) < int(twomoney):
            break

        return win

def validamountcheckthree(three,corner_amount, color_amount, EvenorOdd_Amount, number_amount):
    # lays out the two variables needed in order to make sure that the player inputs the correct amounts
    strike, threemoney = 0, int(three.money)

    # Makes a check on all inputs for betting amounts and makes sure that it doesn't go over the limit
    while strike == 0:
        # Checks corner betting amount if the player decides to skip
        if corner_amount == str("x"):
            corner_amount = 0
        if corner_amount != str("x"):
            if int(corner_amount) >= int(threemoney):
                break
        # Checks color betting amount if the player decides to skip
        if color_amount == str("x"):
            color_amount = 0
        if color_amount != str("x"):
            if int(color_amount) >= int(threemoney):
                break
        # Checks Even or Odd betting amount if the player decides to skip
        if EvenorOdd_Amount == str("x"):
            EvenorOdd_Amount = 0

        if EvenorOdd_Amount != str("x"):
            if int(EvenorOdd_Amount) >= int(threemoney):
                break
        # Checks single number and number range betting amount if the player decides to skip
        if number_amount == str("x"):
            number_amount = 0

        if number_amount != str("x"):
            if int(number_amount) >= int(threemoney):
                break
        # Adds up every betting amount to make sure that it doesn't go over the amount of money the player has
        amount_total = int(corner_amount) + int(color_amount) + int(EvenorOdd_Amount) + int(number_amount)

        # Triggers a variable change if the betting amounts go over the amount of money the player has
        if int(amount_total) > int(threemoney):
            strike = 1

        # Displays an error message if strike, which is the error variable, is set at  1
        if strike == 1:
            Invalidtext = Text(Point(605, 650), "NOT ENOUGH MONEY")
            Invalidtext.setFill("red")
            Invalidtext.draw(win)

        # Allows the player to go on if strike is set to 0
        if int(amount_total) < int(threemoney):
            break
        return win

def readfile():
    #makes list of player and its player limit
    one,two,three,index, playerlimit = 0,0,0,0,0
    #reads the input file by using a loop
    infile = open("Input-Users.txt", "r")
    for line in infile:
        lineList = line.split()
        name = (lineList[0])
        money = (lineList[1])
        index += 1

        #stores data by using conditionals within loop
        if index == 1:
            one = player(name, money)
        if index == 2:
            two = player(name, money)
        if index == 3:
            three = player(name, money)
        playerlimit = index
    return one,two,three,playerlimit

def modifyfile(playerlimit,one,two,three):

    # Sets the name of the outfile
    outputFileName = open("Output-Users.txt", "w")

    # Will modify outfile based on how many players there are
    if playerlimit == 1:
        print(one.name," ",one.money, file=outputFileName)
    if playerlimit == 2:
        print(one.name, " ", one.money, file=outputFileName)
        print(two.name, " ", two.money, file=outputFileName)
    if playerlimit == 3:
        print(one.name, " ", one.money, file=outputFileName)
        print(two.name, " ", two.money, file=outputFileName)
        print(three.name, " ", three.money, file=outputFileName)

def cornors(spinnum, corner_amount):
    # Establishes variable line in which the code later will index from
    numberlist, dex, row1, row2, row3, index1, index2, index3, check, rowonesubtractright, row, rowlist, skip, rowonesubtractleft, rowtwosubtractlowleft, rowtwosubtractlowright, rowtwosubtracthighleft, rowtwosubtracthighright, rowthreesubtractleft, rowthreesubtractright = ["place","1","4","7","10","13","16","2","5","8","11","14","17","3","6","9","12","15","18","0","00"],0,["1","4","7","10","13","16"],["2","5","8","11","14","17"],["3","6","9","12","15","18"],0,0,0,1,[-1,0,1,2,3,4],0,1,0,[1,2,3,4,5,6],[2,3,4,5,6,7],[0,1,2,3,4,5],[2,4,5,6,7,8],[1,2,3,4,5,6],[3,5,6,7,8,9],[2,3,4,5,6,7]

    # Will check if corner input for location is x or not
    if corner_location != str("x"):

        # Will index loop until the roll matches with
        while spinnum != numberlist[dex]:
            dex += 1
        if dex >= 0 and dex < 7:
            row = 1
        if dex >= 7 and dex < 13:
            row = 2
        if dex >= 13 and dex < 19:
            row = 3
        if dex >= 19 or dex >= 20:
            skip = 1

        # Checks for the horizontal row to narrow down location for surrounding corners
        if skip == 0:
            if row == 1:
                while check == 0:
                    if spinnum == row1[index1]:
                        check = 1
                    if spinnum != row1[index1]:
                        index1 += 1
                # Identifies the surrounding corners the roll touches
                rowoneleftcorner = (int(spinnum) - rowonesubtractright[index1])
                rowonerightcorner = (int(spinnum) - rowonesubtractleft[index1])

                #filters out corners that don't exist
                if rowoneleftcorner == 0:
                    rowlist = [rowonerightcorner]
                if rowoneleftcorner != 0:
                    rowlist = [rowoneleftcorner, rowonerightcorner,"placeholder"]

        # Checks for the horizontal row to narrow down location for surrounding corners
            if row == 2:
                while check == 0:
                    if spinnum == row2[index2]:
                        check = 1
                    if spinnum != row2[index2]:
                        index2 += 1

                # Identifies the surrounding corners the roll touches
                rowtwolowleftcornor = (int(spinnum) - rowtwosubtractlowleft[index2])
                rowtwolowrightcornor = (int(spinnum) - rowtwosubtractlowright[index2])
                rowtwohighleftcornor = (int(spinnum) - rowtwosubtracthighleft[index2])
                rowtwohighrightcornor = (int(spinnum) - rowtwosubtracthighright[index2])
                rowlist = [rowtwolowleftcornor, rowtwolowrightcornor, rowtwohighleftcornor, rowtwohighrightcornor,"placeholder"]

        # Checks for the horizontal row to narrow down location for surrounding corners
            if row == 3:
                while check == 0:
                    if spinnum == row3[index3]:
                        check = 1
                    if spinnum != row3[index3]:
                        index3 += 1

                # Identifies the surrounding corners the roll touches
                rowthreeleftcornor = (int(spinnum) - rowthreesubtractleft[index3])
                rowthreerightcornor = (int(spinnum) - rowthreesubtractright[index3])
                rowlist = [rowthreeleftcornor, rowthreerightcornor,"placeholder"]

        # if skip is triggered, player auto-loses money
        if skip == 1:
            corner_amount = corner_amount * -1
            rowlist = ["x"]

    return rowlist, corner_amount

def cornercheck(rowlist,corner_amount,corner_location):

    # Establishes variable list to index from
    spotlist, correspondant, condition, checked, cornerspots = ["C1", "C2", "C3", "C4", "C5", "C6", "C7","C8","C9","C10"],"placeholder",0,0,[1,2,3,4,5,6,7,8,9,10]

    # Auto lose mechanic
    if rowlist != ["x"]:

        # Creates a non-ending loop until player input matches list
        while condition == 0:
            if corner_location != spotlist[checked]:
                checked += 1

            # with checked being defined, the non-ending loop breaks

            if corner_location == spotlist[checked]:
                condition = 1

            # Correspondant becomes an int version of the player corner
            correspondant = cornerspots[checked]

        # defines indexing variables
        ind = 0
        limit = int(len(rowlist))

        # defines a while loop in order to compare player input with the corners the roll touches
        while correspondant != rowlist[ind]:
            ind += 1
            if ind == limit:
                corner_amount = corner_amount * -1
                break
        print(correspondant)
        #modifies money accourdingly
        if correspondant == rowlist[ind]:
            corner_amount = corner_amount * 8
        else:
            corner_amount = corner_amount * -1

    return corner_amount

def moneychange(spinnum, color_location, color_amount, EvenorOdd_location, EvenorOdd_Amount, number_location, number_amount):
    # Sets up many variables used in order to keep track of index loops to modify money
    RedorBlackchoicelist, RedandBlacklist, EvenorOddlist, condition, ranges, colorroll, EoOchoice, EoO, number_range, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, rednumbers, blacknumbers, onetonine, tentoeighteen,index,index2,index3,index4 = ["placeholder","RED","Red","red","BLACK","Black","black"],["placeholder","1", "3", "5", "7", "9", "10", "12", "14", "16", "18", "2", "4", "6", "8", "11", "13", "15", "17", "0", "00"],["placeholder","EVEN","Even","even","ODD","Odd","odd"],0,0,"not-red",3,(int(spinnum)%2),0,["2","3","5","6","x"],["1", "2", "4", "5","x"],["5","6","8","9","x"],["4", "5", "7", "8","x"],["8","9","11","12","x"],["7","8","10","11","x"],["11", "12", "14", "15","x"],["10", "11", "12", "14","x"],["14", "15", "17", "18","x"],["12", "14", "16", "17","x"],["1","3","5","7","9","10","12","14","16","18",".."],["0","00","2","4","6","8","11","13","15","17",".."],["1","2","3","4","5","6","7","8","9","guh"],["10","11","12","13","14","15","16","17","18","Hung"],0,0,0,0


    # Modifies the betting amount for Even and Odd based around whether or not the number rolled from the wheel has a remainder of 1 or 0 when divided by 2
    if EvenorOdd_location != "x":
        while EvenorOdd_location != EvenorOddlist[condition]:
            condition += 1
        if condition > 3:
            EoOchoice = 1
        if condition < 4:
            EoOchoice = 0
        if EoOchoice == EoO:
            EvenorOdd_Amount = EvenorOdd_Amount * 2
        if EoOchoice != EoO:
            EvenorOdd_Amount = EvenorOdd_Amount * -1

    # Detects if the player input a number range based on str value
    if number_location == "1-9":
        ranges = 1
        if number_location == "10-18":
            ranges = 2

    # Modifies the amount bet on numbers based around the ball meeting the range or not
    if ranges == 1:
        if int(spinnum) < 10:
            number_amount = number_amount * 2
        if number_location != int(spinnum):
            number_amount = number_amount * -1
    if ranges == 2:
        if int(spinnum) >= 10:
            number_amount = number_amount * 2
        if number_location != int(spinnum):
            number_amount = number_amount * -1

    # Modifies the amount bet on a single number and is based around whether the roll lands on that single number
    if number_location == spinnum:
        number_amount = number_amount * 35
    if number_location != spinnum:
        number_amount = number_amount * -1

    # Will skip if player inputed "x"
    if color_location != "x":

        # Modifies the amount bet on whether the roll is either the color red or black by determining the index's value
        while spinnum != RedandBlacklist[index]:
            index += 1
        if index < 11:
            colorroll = "red"
        if index > 10:
            colorroll = "black"
        while color_location != RedorBlackchoicelist[index2]:
            index2 += 1
        if index2 > 3:
            color_location = "black"
        if index2 < 4:
            color_location = "red"
        if color_location == colorroll:
            color_amount = color_amount * 2
        if color_location != colorroll:
            color_amount = color_amount * -1

    return color_amount, EvenorOdd_Amount, number_amount

def closebox(turn):

    # draws up the progression button for the next turn and the quit button that will modify outfile
    close = Rectangle(Point(950,2),Point(998,50))
    close.setFill("red")
    close.draw(win)
    ex = Text(Point(974,26),"X")
    ex.setFill("white")
    ex.draw(win)
    next_turn = Rectangle(Point(900,2),Point(950,50))
    next_turn.setFill("green")
    next_turn.draw(win)
    go = Text(Point(925,26),"GO")
    go.setFill("white")
    go.draw(win)

    # Establishes collision for the boxes
    mousepoint = win.getMouse()
    Mousex = mousepoint.getX()
    Mousey = mousepoint.getY()
    # Adds effect to collision such as not doing anything and let the loop continue or stop the main loop and modify outfile
    if Mousex < 998 and Mousey > 2 and Mousex > 950 and Mousey < 50:
        turn = -1
    if Mousex < 950 and Mousey > 2 and Mousex > 900 and Mousey < 50:
        pass
    return win, turn

def moneychangeone(one,corner_amount, color_amount, EvenorOdd_Amount, number_amount):

    # concatenate class value from str to int
    onemoney = int(one.money)

    # if still possible, convert "x" values to int(0)
    if corner_amount == str("x"):
        corner_amount = 0
    if color_amount == str("x"):
        color_amount = 0
    if EvenorOdd_Amount == str("x"):
        EvenorOdd_Amount = 0
    if number_amount == str("x"):
        number_amount = 0

    # adds all values together into amount_total
    amount_total = int(corner_amount) + int(color_amount) + int(EvenorOdd_Amount) + int(number_amount)

    # changes the variable that replicates class value
    onemoney = onemoney + amount_total

    # changes class value
    one.money = str(onemoney)

    print(one.money)
    return one.money

def moneychangetwo(two,corner_amount, color_amount, EvenorOdd_Amount, number_amount):
    # concatenate class value from str to int
    twomoney = int(two.money)

    # if still possible, convert "x" values to int(0)
    if corner_amount == str("x"):
        corner_amount = 0
    if color_amount == str("x"):
        color_amount = 0
    if EvenorOdd_Amount == str("x"):
        EvenorOdd_Amount = 0
    if number_amount == str("x"):
        number_amount = 0

    # adds all values together into amount_total
    amount_total = int(corner_amount) + int(color_amount) + int(EvenorOdd_Amount) + int(number_amount)

    # changes the variable that replicates class value
    twomoney = twomoney + amount_total

    # changes class value
    two.money = int(twomoney)

    print(two.money)
    return two.money

def moneychangethree(three,corner_amount, color_amount, EvenorOdd_Amount, number_amount):
    # concatenate class value from str to int
    threemoney = int(three.money)

    # if still possible, convert "x" values to int(0)
    if corner_amount == str("x"):
        corner_amount = 0
    if color_amount == str("x"):
        color_amount = 0
    if EvenorOdd_Amount == str("x"):
        EvenorOdd_Amount = 0
    if number_amount == str("x"):
        number_amount = 0

    # adds all values together into amount_total
    amount_total = int(corner_amount) + int(color_amount) + int(EvenorOdd_Amount) + int(number_amount)

    # changes the variable that replicates class value
    threemoney = threemoney + amount_total

    # changes class value
    three.money = int(threemoney)

    print(three.money)
    return three.money

if __name__=='__main__':
    # defines which turn it is among the players
    turn = 0
    one, two, three, playerlimit = readfile()
    win = thetablebasics()
    wheeldetails = wheelstill()
    boarddetails = boarddetails1()
    while turn > -1:
        info = playertext()
        turn += 1
        # For each cycle or turn, these three lines will reset, and store input data for the players turn
        cornorloc, cornoramt, colorloc, coloramt, EoOloc, EoOamt, numsloc, numsamt = info
        gettingchoice = getChoice(cornorloc,cornoramt,colorloc,coloramt,EoOloc,EoOamt,numsloc,numsamt)
        corner_location, corner_amount, color_location, color_amount, EvenorOdd_location, EvenorOdd_Amount, number_location, number_amount = gettingchoice

        spinnum = wheelspin()
        # Defends against invalid inputs
        location_validation = validlocationcheck(corner_location, color_location, EvenorOdd_location, number_location)

    # Depending on the turn, each player will go through the same money modifying process
        if turn == 1:
            validamountcheckone(one, corner_amount, color_amount, EvenorOdd_Amount, number_amount)
            validcheck = validamountcheckone(one, corner_amount, color_amount, EvenorOdd_Amount, number_amount)
            if corner_location != str("x"):
                cornerspotting = cornors(spinnum, corner_amount)
                rowlist = cornerspotting
                cornercheck(rowlist, corner_amount, corner_location)
            modifymoney = moneychange(spinnum, color_location, color_amount, EvenorOdd_location, EvenorOdd_Amount, number_location,number_amount)
            moneychangeone(one,corner_amount, color_amount, EvenorOdd_Amount, number_amount)
            closeup = closebox(turn)
        if turn == 2:
            validamountchecktwo(two, corner_amount, color_amount, EvenorOdd_Amount, number_amount)
            validation = validlocationcheck(corner_location, color_location, EvenorOdd_location, number_location)
            validcheck = validamountchecktwo(two, corner_amount, color_amount, EvenorOdd_Amount, number_amount)
            if corner_location != str("x"):
                cornerspotting = cornors(spinnum, corner_amount)
                rowlist = cornerspotting
                cornercheck(rowlist, corner_amount, corner_location)
            moneychange(spinnum, color_location, color_amount, EvenorOdd_location, EvenorOdd_Amount, number_location,number_amount)
            moneychangetwo(two, corner_amount, color_amount, EvenorOdd_Amount, number_amount)
            closeup = closebox(turn)
        if turn == 3:
            validamountcheckthree(three, corner_amount, color_amount, EvenorOdd_Amount, number_amount)
            validation = validlocationcheck(corner_location, color_location, EvenorOdd_location, number_location)
            validcheck = validamountcheckthree(three, corner_amount, color_amount, EvenorOdd_Amount, number_amount)
            if corner_location != str("x"):
                cornerspotting = cornors(spinnum, corner_amount)
                rowlist = cornerspotting
                cornercheck(rowlist, corner_amount, corner_location)
            moneychange(spinnum, color_location, color_amount, EvenorOdd_location, EvenorOdd_Amount, number_location, number_amount)
            moneychangethree(three, corner_amount, color_amount, EvenorOdd_Amount, number_amount)
            closeup = closebox(turn)

        # creates loop at the player-limit in order to keep the game going until a player quits
        if turn == playerlimit:
            turn = 0

    # modifies the outfile with modified money
    modifyfile(playerlimit,one,two,three)