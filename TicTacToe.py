# CS 100 2018F
# Tic-Tac-Toe, Oct 23, 2018

from random import *
              
def drawingBoard(t, size):
    t.penup()
    t.width(5)
    t.forward(size/3)
    t.right(90)
    t.pendown()
    t.forward(size)
    t.penup()
    t.left(90)
    t.forward(size/3)
    t.left(90)
    t.pendown()
    t.forward(size)
    t.penup()
    t.home()
    t.right(90)
    t.forward(size/3)
    t.left(90)
    t.pendown()
    t.forward(size)
    t.penup()
    t.right(90)
    t.forward(size/3)
    t.right(90)
    t.pendown()
    t.forward(size)
    t.penup()
    t.home()

def drawX(t):
    t.width(10)
    t.color('red')
    t.right(45)
    t.forward(40)
    t.pendown()
    t.forward(45)
    t.penup()
    t.right(135)
    t.forward(30)
    t.right(135)
    t.pendown()
    t.forward(45)
    t.penup()
    t.home()

def drawO(t):
    t.width(10)
    t.color('blue')
    t.forward(45)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.pendown()
    t.circle(25)
    t.penup()
    t.home()

def drawWin(t, pos, color):
    if pos == 'straight1':
        t.goto(0, -50)
        t.width(5)
        t.pendown()
        t.forward(300)
        t.penup()

    elif pos == 'straight2':
        t.goto(0, -150)
        t.width(5)
        t.pendown()
        t.forward(300)
        t.penup()

    elif pos == 'straight3':
        t.goto(0, -250)
        t.width(5)
        t.pendown()
        t.forward(300)
        t.penup()

    elif pos == 'down1':
        t.goto(50, 0)
        t.width(5)
        t.right(90)
        t.pendown()
        t.forward(300)
        t.penup()

    elif pos == 'down2':
        t.goto(150, 0)
        t.width(5)
        t.right(90)
        t.pendown()
        t.forward(300)
        t.penup()

    elif pos == 'down3':
        t.goto(250, 0)
        t.width(5)
        t.right(90)
        t.pendown()
        t.forward(300)
        t.penup()
        
    elif pos == 'diagR':
        t.goto(0, 0)
        t.width(5)
        t.right(45)
        t.pendown()
        t.forward(400)
        t.penup()

    else:
        t.goto(300, 0)
        t.width(5)
        t.right(135)
        t.pendown()
        t.forward(400)
        t.penup()
        
def turns(t, loc):
    taken = []
    moves1 = []
    moves2  = []
    gameOver = False
    while gameOver == False:
        player1 = input("Player-1, where would you like to place the X? ")
        while player1 not in loc or player1 in taken:
            print("You either entered an invalid position or one "
                 + "that is already taken.")
            player1 = input("Where would you like to place the X? ")
        taken += [player1]
        moves1 += [player1]
        gameOver = player1Move(player1, t, gameOver, moves1)
        if gameOver == True:
            break
        if len(taken) == len(loc):
            break
        print("Computer's turn..")
        player2 = computerTurn(loc)
        while player2 not in loc or player2 in taken:
            player2 = computerTurn(loc)
        taken += [player2]
        moves2 += [player2]
        gameOver = player2Move(player2, t, gameOver, moves2)

def computerTurn(boxLoc):
    boxLoc = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    x = sample(boxLoc, 1)
    return x[0]

def player1Move(player1, t, gameOver, moves):
    if player1 == 'A1':
        t.goto(0, 0)
        drawX(t)

    elif player1 == 'A2':
        t.goto(100, 0)
        drawX(t)

    elif player1 == 'A3':
        t.goto(200, 0)
        drawX(t)

    elif player1 == 'B1':
        t.goto(0, -100)
        drawX(t)

    elif player1 == 'B2':
        t.goto(100, -100)
        drawX(t)

    elif player1 == 'B3':
        t.goto(200, -100)
        drawX(t)

    elif player1 == 'C1':
        t.goto(0, -200)
        drawX(t)

    elif player1 == 'C2':
        t.goto(100, -200)
        drawX(t)

    else:
        t.goto(200, -200)
        drawX(t)

    if ('A1' in moves and 'A2' in moves and 'A3' in moves):
        drawWin(t, 'straight1', 'red')
        return True

    elif ('B1' in moves and 'B2' in moves and 'B3' in moves):
        drawWin(t, 'straight2', 'red')
        return True

    elif ('C1' in moves and 'C2' in moves and 'C3' in moves):
        drawWin(t, 'straight3', 'red')
        return True

    elif ('A1' in moves and 'B1' in moves and 'C1' in moves):
        drawWin(t, 'down1', 'red')
        return True

    elif ('A2' in moves and 'B2' in moves and 'C2' in moves):
        drawWin(t, 'down2', 'red')
        return True

    elif ('A3' in moves and 'B3' in moves and 'C3' in moves):
        drawWin(t, 'down3', 'red')
        return True

    elif ('A1' in moves and 'B2' in moves and 'C3' in moves):
        drawWin(t, 'diagR', 'red')
        return True

    elif ('A3' in moves and 'B2' in moves and 'C1' in moves):
        drawWin(t, 'diagL', 'red')
        return True

    else:
        return False

def player2Move(player2, t, gameOver, moves):
    if player2 == 'A1':
        t.goto(0, 0)
        drawO(t)

    elif player2 == 'A2':
        t.goto(100, 0)
        drawO(t)

    elif player2 == 'A3':
        t.goto(200, 0)
        drawO(t)

    elif player2 == 'B1':
        t.goto(0, -100)
        drawO(t)

    elif player2 == 'B2':
        t.goto(100, -100)
        drawO(t)

    elif player2 == 'B3':
        t.goto(200, -100)
        drawO(t)

    elif player2 == 'C1':
        t.goto(0, -200)
        drawO(t)

    elif player2 == 'C2':
        t.goto(100, -200)
        drawO(t)

    else:
        t.goto(200, -200)
        drawO(t)

    if ('A1' in moves and 'A2' in moves and 'A3' in moves):
        drawWin(t, 'straight1', 'blue')
        return True

    elif ('B1' in moves and 'B2' in moves and 'B3' in moves):
        drawWin(t, 'straight2', 'blue')
        return True

    elif ('C1' in moves and 'C2' in moves and 'C3' in moves):
        drawWin(t, 'straight3', 'blue')
        return True

    elif ('A1' in moves and 'B1' in moves and 'C1' in moves):
        drawWin(t, 'down1', 'blue')
        return True

    elif ('A2' in moves and 'B2' in moves and 'C2' in moves):
        drawWin(t, 'down2', 'blue')
        return True

    elif ('A3' in moves and 'B3' in moves and 'C3' in moves):
        drawWin(t, 'down3', 'blue')
        return True

    elif ('A1' in moves and 'B2' in moves and 'C3' in moves):
        drawWin(t, 'diagR', 'blue')
        return True

    elif ('A3' in moves and 'B2' in moves and 'C1' in moves):
        drawWin(t, 'diagL', 'blue')
        return True

    else:
        return False

def letsPlay(t, loc):
    drawingBoard(turt, 300)
    turns(t, loc)
 
import turtle

turt = turtle.Turtle()
screen = turtle.Screen()
boxLoc = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
letsPlay(turt, boxLoc)
