# ROCK-PAPER-SCISSORS GAME
# 2022-04-08

import random
from tkinter import *
import tkinter.font as tkFont

version = 'version: beta_v1_2022-04-08'


## WINDOWS / ROOTS
# main window
root=Tk()
root.title("ROCK-PAPER-SCISSORS GAME")
# root.geometry("1000x800")

    ## main-LABELS
    # time
timeLabel_font=tkFont.Font(slant='italic')
timeLabel=Label(root, text='time', font=timeLabel_font)
timeLabel.grid(row=0, column=0, sticky=W)

    # version
versionLabel_font=tkFont.Font(slant='italic')
versionLabel=Label(root, text=version, font=versionLabel_font)
versionLabel.grid(row=0, column=1, sticky=E)

    # title
title_font=tkFont.Font(family='Helvetica', size='32', weight='bold', slant='italic')
titleLabel=Label(root, text='ROCK-PAPER-SCISSORS\nGAME', padx=200, pady=20, font=title_font)
titleLabel.grid(row=1, columnspan=2, sticky=W+E)

    # player name
global player
player='undefined'
player_label='Player name: {}'.format(player)
name_font=tkFont.Font(slant='italic')
nameLabel=Label(root, text=player_label, font=name_font)
nameLabel.grid(row=2, column=0, sticky=W)


    ## main-BUTTONS
def on_enter(e):
    e.widget['foreground'] = 'orange'

def on_leave(e):
    e.widget['foreground'] = 'black'

    # start button
start_font=tkFont.Font(size='30', weight='bold')
startButton=Button(root, text='START', font=start_font, activeforeground='orange', relief=RIDGE, bd=0)
startButton.grid(row=3, column=0, sticky=W)
startButton.bind('<Enter>', on_enter)
startButton.bind('<Leave>', on_leave)

    # change player button
def change_player():
    chPlayerFrame=LabelFrame(root, text='CHANGE PLAYER')
    chPlayerFrame.grid(row=3, rowspan=3, column=1)

    chPlayerEntry=Entry(chPlayerFrame, width=50, fg='gray')
    chPlayerEntry.grid(row=0,column=0)
    chPlayerEntry.insert(0, 'Type a player name or choose from list below...')

    clearButton=Button(chPlayerFrame, text='Clear')
    clearButton.grid(row=0, column=1)

    confirmButton=Button(chPlayerFrame, text='Confirm')
    confirmButton.grid(row=2, columnspan=2)

    backButton=Button(chPlayerFrame, text='Back')
    backButton.grid(row=3, columnspan=2)



    def click(event):
        chPlayerEntry.configure(state=NORMAL, fg='black')
        chPlayerEntry.delete(0, END)
        chPlayerEntry.unbind('<Button-1>', clicked)
    
    clicked = chPlayerEntry.bind('<Button-1>', click)


    

chPlayer_font=tkFont.Font(size='15', weight='bold')
chPlayerButton=Button(root, text='CHANGE PLAYER', font=chPlayer_font, activeforeground='orange', relief=RIDGE,
                        bd=0, command=change_player)
chPlayerButton.grid(row=4, column=0, ipadx=10, sticky=W)
chPlayerButton.bind('<Enter>', on_enter)
chPlayerButton.bind('<Leave>', on_leave)

    
    # exit button
def exit():
    root.destroy()

exit_font=tkFont.Font(size='15', weight='bold')
exitButton=Button(root, text='EXIT', font=exit_font, activeforeground='orange', relief=RIDGE, bd=0, 
                    command=exit)
exitButton.grid(row=5, column=0, ipadx=10, sticky=W)
exitButton.bind('<Enter>', on_enter)
exitButton.bind('<Leave>', on_leave)



# start root
    ## start root - LABELS
    # computer choice
    # player choice
    # communicator
    # counter-all
    # counter-wins
    # counter-percentage
    # counter-choices
    # counter-which choice wins most time

    ## start root - BUTTONS
    # rock button
    # paper button
    # scissors button
    # show more statistics
    # reset button
    # quit game button
# type name root
    ## type name - LABELS
    # name entry
    # names list

    ## type name - BUTTONS
    # start button
    # back button



root.mainloop()