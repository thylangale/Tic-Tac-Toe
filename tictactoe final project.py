# Thy-Lan Gale
# tlg326
# CS-UY 1114
# Final project - Tic Tac Toe

import turtle
import time
import random

the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]

def draw_board(board):
    turtle.setup(650,650) #sets the height and width of the turtle frame
    turtle.clear()
    turtle.penup()
    turtle.home() #resets turtle to origin every time

    for i in range(100,-200,-200): #draws horizontal lines for board
        turtle.color("black")
        turtle.penup()
        turtle.setx(-300)
        turtle.sety(i)
        turtle.pendown()
        turtle.forward(600)
    turtle.right(90) #turns the turtle to draw straight down

    for j in range(100,-200,-200): #draws vertical lines for board
        turtle.color("black")
        turtle.penup()
        turtle.setx(j)
        turtle.sety(300)
        turtle.pendown()
        turtle.forward(600)

    for k in range(9): #checks all places on the board
        turtle.penup()
        if board[k] == "O": #if human moved here, draws O
            turtle.color("blue")
            turtle.setheading(270)
            x_coord_O = 200 * (k % 3) - 300
            y_coord_O = 200 + (k // 3) * -200
            turtle.goto(x_coord_O, y_coord_O)
            turtle.pendown()
            turtle.circle(100)
        elif board[k] == "X": #if comp moved here, draws X
            turtle.color("red")
            x_coord_X1 = -300 + (k % 3) * 200
            x_coord_X2 = -100 + (k % 3) * 200
            y_coord_X = 300 + (k // 3) * -200
            turtle.goto(x_coord_X1, y_coord_X)
            turtle.pendown()
            turtle.setheading(-45)
            turtle.forward(282.84)
            turtle.penup()
            turtle.goto(x_coord_X2, y_coord_X)
            turtle.pendown()
            turtle.setheading(-135)
            turtle.forward(282.84)        
    turtle.update()
   
    
def do_user_move(board, x, y): 
    print("user clicked at "+str(x)+","+str(y))
    for i in range(9): #checks every area to see if the user can move here
        x_bound = -300 + (i % 3) * 200
        y_bound = 300 + (i // 3) * -200
        if check_game_over(board) == True:
            break
        elif board[i] == "_" and x > x_bound and x < x_bound + 200 and y < y_bound and y > y_bound - 200:
            board[i] = "O"
            return True
    return False
       

def check_game_over(board):
    lst_of_wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]] #all possible wins
    turtle.color("green")
    turtle.penup()
    turtle.home()
    for win_combo in lst_of_wins:
        if board[win_combo[0]] == board[win_combo[1]] == board[win_combo[2]] and board[win_combo[0]] != "_":
            if board[win_combo[0]] == "O": #human won
                time.sleep(0.5)
                turtle.clear()
                turtle.write("Congratulations! You won!", align = "center", font = ("Arial", 20, "bold"))
                for i in range(len(board)):
                    if board[i] != "_":
                        board[i] = "_"
                time.sleep(1)
                draw_board(board)
            else: #computer won
                time.sleep(0.5)
                turtle.clear()
                turtle.write("Sorry! You lost.", align = "center", font = ("Arial", 20, "bold"))
                for i in range(len(board)):
                    if board[i] != "_":
                        board[i] = "_"
                time.sleep(1)
                draw_board(board)
            return True

    count = 0
    for k in range(9): #checks to see if board is full
        if board[k] != '_':
            count += 1
        if count == 9: #all spaces are filled
            time.sleep(0.5)
            turtle.clear()
            turtle.write("There is no winner.", align = "center", font = ("Arial", 20, "bold"))
            for i in range(len(board)):
                if board[i] != "_":
                    board[i] = "_"
            time.sleep(1)
            draw_board(board)
            return True
    
    return False

def do_computer_move(board):
    lst_of_wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]] #all possible wins

    for win_combo in lst_of_wins:
        if board[win_combo[0]] == board[win_combo[1]] == "X" or board[win_combo[0]] == board[win_combo[2]] == "X" \
           or board[win_combo[1]] == board[win_combo[2]] == "X": #computer can win
            for i in range(3):
                if board[win_combo[i]] == "_":
                    board[win_combo[i]] = "X"
                    return
        
    for win_combo in lst_of_wins: #not in the same loop as above so that computer prioritizes winning first
        if board[win_combo[0]] == board[win_combo[1]] == "O" or board[win_combo[0]] == board[win_combo[2]] == "O" \
           or board[win_combo[1]] == board[win_combo[2]] == "O": #computer can block 
            for j in range(3):
                if board[win_combo[j]] == "_":
                    board[win_combo[j]] = "X"
                    return
       
    #random computer move
    comp_position = random.randint(0,8)
    compMove = False
    while not compMove:
        if board[comp_position] == "_":
            board[comp_position] = "X"
            compMove = True
            return
        else:
            comp_position = random.randint(0,8)
            
def clickhandler(x, y):
    if do_user_move(the_board,x,y): #if user moves
        draw_board(the_board) #draws the board
        if not check_game_over(the_board): #if the game is not over
            do_computer_move(the_board) #the computer's move
            draw_board(the_board) #board is updated
            check_game_over(the_board)#check to see if the game is over
    #if game is not over, then the user moves again

def main():
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()

main()
