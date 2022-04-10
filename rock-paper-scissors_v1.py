# ROCK-PAPER-SCISSORS GAME
# 2022-04-08

import random
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import ImageTk, Image

version = 'version: beta_v1_2022-04-08'


## WINDOWS / ROOTS
# main window
root=Tk()
root.title("ROCK-PAPER-SCISSORS GAME")
# root.iconbitmap(r'D:\Dokumenty\KURSY\PYTHON\projekty\rock-paper-scissors\img\backButtonImg — kopia.ico')
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
def show_player_label(player):
    player_label='Player name: {}'.format(player)
    name_font=tkFont.Font(slant='italic')
    global nameLabel
    nameLabel=Label(root, text=player_label, font=name_font)
    nameLabel.grid(row=2, column=0, sticky=W)
show_player_label(player)

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
global players
players = ['Patryk', 'Magda']

def change_player():
    chPlayerButton.configure(state=DISABLED)

        # frame - changing player frame
    chPlayerFrame=LabelFrame(root)
    chPlayerFrame.grid(row=3, rowspan=3, column=1, sticky=W)

        # entry - changing player frame
    chPlayerEntry=Entry(chPlayerFrame, width=50, fg='gray')
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
    drop.grid(row=1, column=2, sticky=W+E)
    
        # clear button - changing player frame
    def clear():
        chPlayerEntry.delete(0, END)
    
    clearButton=Button(chPlayerFrame, text='Clear', command=clear)
    clearButton.grid(row=1, column=3, sticky=W)

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
    
    confirmButton=Button(chPlayerFrame, text='Confirm', command=confirm)
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

    # backButton=Button(chPlayerFrame, text='Back', command=back)
    # backButton = Button(chPlayerFrame, command=back, image=backButtonImg)
    # backButton.grid(row=0, column=0, sticky=W)

    path = r'D:\Dokumenty\KURSY\PYTHON\projekty\rock-paper-scissors\img\backButtonImg.png'
    # backButtonImg = ImageTk.PhotoImage(Image.open(path))
    backButtonImg = PhotoImage(file = path)
    backButtonImgResized = backButtonImg.subsample(2, 2)
    #backButtonImgResized = backButtonImg.resize((300,205), Image.ANTIALIAS)

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