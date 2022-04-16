# ROCK-PAPER-SCISSORS GAME
# 2022-04-08

import random
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import ImageTk, Image
import os

version = 'version: beta_v1_2022-04-08'

global srcPath
srcPath = os.getcwd()

## WINDOWS / ROOTS
# main window
root=Tk()
root.title("ROCK-PAPER-SCISSORS GAME")
# root.iconbitmap(r'D:\Dokumenty\KURSY\PYTHON\projekty\rock-paper-scissors\img\backButtonImg — kopia.ico')
# root.geometry("1000x800")



    ## main-LABELS
    # time
timeLabel_font = tkFont.Font(slant='italic')
timeLabel = Label(root, text='time', font=timeLabel_font)
timeLabel.grid(row=0, column=0, sticky=W)

    # version
versionLabel_font = tkFont.Font(slant='italic')
versionLabel = Label(root, text=version, font=versionLabel_font)
versionLabel.grid(row=0, column=1, sticky=E)

    # title
title_font = tkFont.Font(family='Helvetica', size='32', weight='bold', slant='italic')
titleLabel = Label(root, text='ROCK-PAPER-SCISSORS\nGAME', padx=200, pady=20, font=title_font)
titleLabel.grid(row=1, columnspan=2, sticky=W+E)

    # player name
global player
player='undefined'
def show_player_label(player):
    player_label='Player name: {}'.format(player)
    name_font = tkFont.Font(slant='italic')
    global nameLabel
    nameLabel = Label(root, text=player_label, font=name_font)
    nameLabel.grid(row=2, column=0, sticky=W)
show_player_label(player)

    ## main-BUTTONS
def on_enter(e):
    e.widget['foreground'] = 'orange'

def on_leave(e):
    e.widget['foreground'] = 'black'

    # start button
def start():
    # start root
    startRoot = Toplevel()
    startRoot.title('ROCK-PAPER-SCISSORS GAME')

    def show_comp_choice():
        choices = ['rock', 'paper', 'scissors']
        compChoice = random.choice(choices)
        source = '''
global choosenCompImg
choosenCompImg = PhotoImage(file = srcPath+r'\img\{}_trans.png')
'''.format(compChoice)
        exec(source)
        compChoiceLabel.configure(image = choosenCompImg)
        compChoiceLabel.image = choosenCompImg
        compChoiceLabel.grid(row=0, column=1)

    def show_choice(imagePath):
        choosenImg = PhotoImage(file = imagePath)
        playerChoiceLabel.configure(image = choosenImg)
        playerChoiceLabel.image = choosenImg
        playerChoiceLabel.grid(row=1, column=1)
        show_comp_choice()

    ## start root - LABELS
    # computer choice
    compChoiceLabel = Label(startRoot)

    # player choice
    playerChoiceLabel = Label(startRoot)

    # communicator
    # counter-all
    # counter-wins
    # counter-percentage
    # counter-choices
    # counter-which choice wins most time

    ## start root - BUTTONS
    # rock button

    rockButtonImg = PhotoImage(file = srcPath+r'\img\rock_trans.png')
    rockButtonImg = rockButtonImg.subsample(1,1)
    rockButton = Button(startRoot, image=rockButtonImg, bd = 0,
                        command = lambda: show_choice(srcPath+r'\img\rock_trans.png'))
    rockButton.image = rockButtonImg
    rockButton.grid(row=3, column=0)

    # paper button
    paperButtonImg = PhotoImage(file = srcPath+r'\img\paper_trans.png')
    paperButtonImg = paperButtonImg.subsample(1,1)
    paperButton = Button(startRoot, image=paperButtonImg, bd = 0,
                        command = lambda: show_choice(srcPath+r'\img\paper_trans.png'))
    paperButton.image = paperButtonImg
    paperButton.grid(row=3, column=1)

    # scissors button
    def scissors():
        pass

    scissorsButtonImg = PhotoImage(file = srcPath+r'\img\scissors_trans.png')
    scissorsButtonImg = scissorsButtonImg.subsample(1,1)
    scissorsButton = Button(startRoot, image=scissorsButtonImg, bd = 0,
                            command = lambda: show_choice(srcPath+r'\img\scissors_trans.png'))
    scissorsButton.image = scissorsButtonImg
    scissorsButton.grid(row=3, column=2)

    # show more statistics
    # reset button
    # quit game button
    def exit_startRoot():
        startRoot.destroy()

    exit_font = tkFont.Font(size='15', weight='bold')
    exitButton = Button(startRoot, text='EXIT', font=exit_font, activeforeground='orange', relief=RIDGE, bd=0, 
                        command=exit_startRoot)
    exitButton.grid(row=4, column=0, ipadx=10, sticky=W)
    exitButton.bind('<Enter>', on_enter)
    exitButton.bind('<Leave>', on_leave)

start_font = tkFont.Font(size='30', weight='bold')
startButton = Button(root, text='START', font=start_font, activeforeground='orange', relief=RIDGE, bd=0, command=start)
startButton.grid(row=3, column=0, sticky=W)
startButton.bind('<Enter>', on_enter)
startButton.bind('<Leave>', on_leave)

    # change player button
global players
players = ['Patryk', 'Magda']

def change_player():
    chPlayerButton.configure(state=DISABLED)

        # frame - changing player frame
    chPlayerFrame=LabelFrame(root)
    chPlayerFrame.grid(row=3, rowspan=3, column=1, sticky=W)

        # entry - changing player frame
    chPlayerEntry = Entry(chPlayerFrame, width=50, fg='gray')
    chPlayerEntry.grid(row=1,column=1)
    defaultText = ' Type a player name or choose from list...'
    chPlayerEntry.insert(0, defaultText)

        # option menu - changing player frame
    def choice_from_list(clicked):
        chPlayerEntry.delete(0, END)
        chPlayerEntry.configure(state=NORMAL, fg='black')
        chPlayerEntry.insert(0, clicked)
        clicked2.set('')
    
    clicked2 = StringVar(value='')
    drop = OptionMenu(chPlayerFrame, clicked2, *players, command=choice_from_list)
    drop.grid(row=1, column=3, sticky=W+E)
    
        # clear button - changing player frame
    def clear():
        chPlayerEntry.delete(0, END)
    
    clearButtonImgPath = srcPath+r'\img\clearButtonImg.png'
    clearButtonImg = PhotoImage(file = clearButtonImgPath)
    clearButtonImgResized = clearButtonImg.subsample(1,1)

    clearButton = Button(chPlayerFrame, image=clearButtonImgResized, command=clear)
    clearButton.image = clearButtonImgResized
    clearButton.grid(row=1, column=2, sticky=W)

        # confirm button - changing player frame
    def confirm():
        newPlayerName = chPlayerEntry.get()
        if not newPlayerName in players and not newPlayerName == '' and not newPlayerName == defaultText:
            players.append(newPlayerName)
        if not newPlayerName == '' and not newPlayerName == defaultText:
            player = newPlayerName
            nameLabel.destroy()
            show_player_label(player)
        else:
            messagebox.showinfo('CONFIRM ERROR', defaultText)
            return
        
        chPlayerButton.configure(state=NORMAL)
        chPlayerFrame.destroy()

    confirmButtonImgPath = srcPath+r'\img\confirmButtonImg.png'
    confirmButtonImg = PhotoImage(file = confirmButtonImgPath)
    confirmButtonImgResized = confirmButtonImg.subsample(2, 2)
    
    confirmButton = Button(chPlayerFrame, image=confirmButtonImgResized, command=confirm)
    confirmButton.image = confirmButtonImgResized
    confirmButton.grid(row=0, column=1, sticky=W)

        # back button - changing player frame
    def back():
        if chPlayerEntry.get() != '' and chPlayerEntry.get() != defaultText:
            q = messagebox.askyesno('UNCONFIRMED CHANGES','You have UNCONFIRMED data. Do you want to CONFIRM?')
            if q:
                confirm()
            else:
                chPlayerFrame.destroy()
        else:
            chPlayerFrame.destroy()
        chPlayerButton.configure(state=NORMAL)

    backButtonImgPath = srcPath+r'\img\backButtonImg.png'
    backButtonImg = PhotoImage(file = backButtonImgPath)
    backButtonImgResized = backButtonImg.subsample(2, 2)

    backButton = Button(chPlayerFrame, image=backButtonImgResized, command=back)
    backButton.image = backButtonImgResized
    backButton.grid(row=0, column=0, sticky=W)

    def click(event):
        if chPlayerEntry.get() == defaultText:
            chPlayerEntry.configure(state=NORMAL, fg='black')
            chPlayerEntry.delete(0, END)
            chPlayerEntry.unbind('<Button-1>', clicked)
        else:
            return

    clicked = chPlayerEntry.bind('<Button-1>', click)

chPlayer_font = tkFont.Font(size='15', weight='bold')
chPlayerButton = Button(root, text='CHANGE PLAYER', font=chPlayer_font, activeforeground='orange', relief=RIDGE,
                        bd=0, command=change_player)
chPlayerButton.grid(row=4, column=0, ipadx=10, sticky=W)
chPlayerButton.bind('<Enter>', on_enter)
chPlayerButton.bind('<Leave>', on_leave)

    
    # exit button
def exit():
    root.destroy()

exit_font = tkFont.Font(size='15', weight='bold')
exitButton = Button(root, text='EXIT', font=exit_font, activeforeground='orange', relief=RIDGE, bd=0, 
                    command=exit)
exitButton.grid(row=5, column=0, ipadx=10, sticky=W)
exitButton.bind('<Enter>', on_enter)
exitButton.bind('<Leave>', on_leave)





root.mainloop()