import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

def create_gameboard():
    board = [[" "," "," "], #1st row
             [" "," "," "], #2nd row
             [" "," "," "]] #3rd row

current_player = "x"

def handle_click(row,column):
    global current_player
    #checks if the selected button value is empty
    if board[row][column] == " ":
        board[row][column] = current_player


    buttons = [] 
    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(window, text = " ", width = 15, height = 6, command = lambda:handle_click(i,j))
            button.grid(row = i, column = j)
            row.append(button)
        buttons.append(row)


create_gameboard()

window.mainloop()
    