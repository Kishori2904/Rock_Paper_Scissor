from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from random import randint

win = tk.Tk()
win.title("Rock Paper Scissor")
win.geometry("780x330")
win.resizable(False,False)
win.config(background="black")

rock_img = ImageTk.PhotoImage(Image.open("rock2.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper2.png"))
scissors_img = ImageTk.PhotoImage(Image.open("scissors2.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock1.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper1.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors1.png"))

user_label = Label(win,image=scissors_img,bg="black")
comp_label = Label(win,image=scissors_img_comp,bg="black")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

playerScore = Label(win,text=0,font=100,bg="black",fg="yellow")
compScore = Label(win,text=0,font=100,bg="black",fg="yellow")
compScore.grid(row=3, column=0)
playerScore.grid(row=3, column=4)

user_indicator = Label(win,font=50,text="User",bg="black",fg="yellow")
comp_indicator = Label(win,font=50,text="Computer",bg="black",fg="yellow")
user_indicator.grid(row=0, column=4)
comp_indicator.grid(row=0, column=0)

# Message
msg = Label(win, font=50,bg="black",fg="yellow",text="You Lose !!")
msg.grid(row=7, column=2)

def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)
def updateCompScore():
    score = int(compScore["text"])
    score += 1
    compScore["text"] = str(score)

def checkWin(player,computer):
    if player == computer:
        updateMessage("It's a tie !!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You lose !!")
            updateCompScore()
        else:
            updateMessage("You Win !!")
            updateUserScore()
    elif player == "paper":
        if computer == "scissors":
            updateMessage("You lose !!")
            updateCompScore()
        else:
            updateMessage("You Win !!")
            updateUserScore()
    elif player == "scissors":
        if computer == "rock":
            updateMessage("You lose !!")
            updateCompScore()
        else:
            updateMessage("You Win !!")
            updateUserScore()

    else:
        pass

# Update Choice
choices = ["rock","paper","scissors"]
def updateChoice(x):

# for computer 
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissors_img_comp)
# for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x =="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissors_img)

    checkWin(x,compChoice)

# Buttons
rock  = Button(win,width=20,height=2,text="ROCK",bg="yellow",fg="black",command = lambda:updateChoice("rock")).grid(row=5, column=1)
paper  = Button(win,width=20,height=2,text="PAPER",bg="red",fg="white",command = lambda:updateChoice("paper")).grid(row=5, column=2)
scissors  = Button(win,width=20,height=2,text="Scissors",bg="aqua",fg="black",command = lambda:updateChoice("scissors")).grid(row=5, column=3)
exit  = Button(win,width=10,height=1,text="exit",bg="grey",fg="black",command = win.quit).grid(row=8, column=4)

win.mainloop()

