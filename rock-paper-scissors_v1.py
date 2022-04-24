# ROCK-PAPER-SCISSORS GAME
# 2022-04-08

import random
from tkinter import *
from tkinter import messagebox
import tkinter.font as tkFont
from PIL import ImageTk, Image
import os
import time

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
    # startRoot.geometry('650x800')

    startFrame = LabelFrame(startRoot, bd=0)
    startFrame.grid(row=1, columnspan=3)

    statisticsFrame = LabelFrame(startRoot, text = 'Statistics')
    statisticsFrame.grid(row =0, rowspan=6, column=3, sticky=N+S, padx=(10,0))

    # def time_sleep(imagePath):
    #     compChoiceLabel.configure(image=undefinedImg)
    #     playerChoiceLabel.configure(image=undefinedImg)
    #     root.after(1000, comLabel.config(text='3'))
    #     root.after(1000, comLabel.config(text='2'))
    #     root.after(1000, comLabel.config(text='1'))
    #     show_choice(imagePath)

    global n_games
    n_games = StringVar(value='0')
    global n_comp_win
    n_comp_win = StringVar(value='0')
    global n_player_win
    n_player_win = StringVar(value='0')
    global n_draw
    n_draw = StringVar(value='0')

    global n_comp_perc
    n_comp_perc = StringVar(value='0%')
    global n_player_perc
    n_player_perc = StringVar(value='0%')
    global n_draw_perc
    n_draw_perc = StringVar(value='0%')

    def counter(action):
        def counter_all():
            n_games_new = n_games.get()
            n_games_new = int(n_games_new) + 1
            n_games_new = str(n_games_new)
            n_games.set(value=n_games_new)
            return n_games
        
        def counter_winner(action):
            if action == 2: #computer wins
                n_comp_win_new = n_comp_win.get()
                n_comp_win_new = int(n_comp_win_new) + 1
                n_comp_win_new = str(n_comp_win_new)
                n_comp_win.set(value=n_comp_win_new)
                return n_comp_win
            elif action == 3: #player wins
                n_player_win_new = n_player_win.get()
                n_player_win_new = int(n_player_win_new) + 1
                n_player_win_new = str(n_player_win_new)
                n_player_win.set(value=n_player_win_new)
                return n_player_win
            elif action == 4: #draw
                n_draw_new = n_draw.get()
                n_draw_new = int(n_draw_new) + 1
                n_draw_new = str(n_draw_new)
                n_draw.set(value=n_draw_new)
                return n_draw
            else:
                pass
        
        def counter_perc():
                n_comp_perc_new = n_comp_perc.get()
                n_comp_perc_new = n_comp_perc_new.replace('%','')
                n_comp_win_get = n_comp_win.get()
                n_games_get = n_games.get()
                n_comp_perc_new = round(float(n_comp_win_get) / float(n_games_get) * 100, 2)
                n_comp_perc_new = str(n_comp_perc_new)
                n_comp_perc.set(value=n_comp_perc_new+'%')

                n_player_perc_new = n_player_perc.get()
                n_player_perc_new = n_player_perc_new.replace('%','')
                n_player_win_get = n_player_win.get()
                n_games_get = n_games.get()
                n_player_perc_new = round(float(n_player_win_get) / float(n_games_get) * 100, 2)
                n_player_perc_new = str(n_player_perc_new)
                n_player_perc.set(value=n_player_perc_new+'%')

                n_draw_perc_new = n_draw_perc.get()
                n_draw_perc_new = n_draw_perc_new.replace('%','')
                n_draw_get = n_draw.get()
                n_games_get = n_games.get()
                n_draw_perc_new = round(float(n_draw_get) / float(n_games_get) * 100, 2)
                n_draw_perc_new = str(n_draw_perc_new)
                n_draw_perc.set(value=n_draw_perc_new+'%')

        counter_all()
        counter_winner(action)
        counter_perc()


    def winner(compChoice, playerChoice):
        playerChoice = playerChoice.replace('_trans.png','')

        if compChoice == playerChoice:
            communicator(4)
        
        if compChoice == 'rock' and playerChoice == 'scissors':
            communicator(2)
        
        if compChoice == 'paper' and playerChoice == 'rock':
            communicator(2)

        if compChoice == 'scissors' and playerChoice == 'paper':
            communicator(2)

        if playerChoice == 'rock' and compChoice  == 'scissors':
            communicator(3)
        
        if playerChoice == 'paper' and compChoice  == 'rock':
            communicator(3)

        if playerChoice == 'scissors' and compChoice  == 'paper':
            communicator(3)

    def communicator(action):
        # actions:
        # 1. choose a button - default
        # 2. computer wins
        # 3. player wins
        # 4. draw
        if action == 1:
            comLabel.config(text='Choose ROCK / PAPER / SCISSORS from below!')
        elif action == 2:
            comLabel.config(text='COMPUTER WINS!')
        elif action == 3:
            comLabel.config(text='{} WINS!'.format(player).upper())
        elif action == 4:
            comLabel.config(text='DRAW! One more time.')
        counter(action)

    def show_comp_choice(playerChoice):
        choices = ['rock', 'paper', 'scissors']
        compChoice = random.choice(choices)
        source = '''
global choosenCompImg
choosenCompImg = PhotoImage(file = srcPath+r'\img\{}_trans.png')
'''.format(compChoice)
        exec(source)
        compChoiceLabel.configure(image = choosenCompImg)
        compChoiceLabel.image = choosenCompImg
        winner(compChoice, playerChoice)

    def show_choice(imagePath):
        choosenImg = PhotoImage(file = imagePath)
        playerChoiceLabel.configure(image = choosenImg)
        playerChoiceLabel.image = choosenImg
        playerChoice = os.path.basename(imagePath)
        show_comp_choice(playerChoice)

    ## start root - LABELS
    # player label
    player_label='Player name: {}'.format(player)
    name_font = tkFont.Font(slant='italic')
    playerLabel = Label(startRoot, text=player_label, font=name_font)
    playerLabel.grid(row=0, column=0, sticky=W)

    # computer choice
    undefinedImg = PhotoImage(file = srcPath + r'\img\undefined.png')

    compChoiceLabelText = Label(startFrame, text = 'Computer')
    compChoiceLabelText.grid(row=0, column=0)

    compChoiceLabel = Label(startFrame, image = undefinedImg)
    compChoiceLabel.image = undefinedImg
    compChoiceLabel.grid(row=1, column=0)

    # player choice
    playerChoiceLabelText = Label(startFrame, text = player)
    playerChoiceLabelText.grid(row=0, column=1)

    playerChoiceLabel = Label(startFrame, image = undefinedImg)
    playerChoiceLabel.image = undefinedImg
    playerChoiceLabel.grid(row=1, column=1)

    # communicator
    comLabel = Label(startRoot, text='Choose ROCK / PAPER / SCISSORS from below!')
    comLabel.grid(row=3, columnspan=3)

    # counter-all
    counterAllText = Label(statisticsFrame, text='Number of games: ')
    counterAllText.grid(row=0, column=0, sticky=W)
    couterAll = Label(statisticsFrame, textvariable=n_games, width=5)
    couterAll.grid(row=0, column=1, sticky=W)

    # counter-wins
    counterCompWinText = Label(statisticsFrame, text='Number of computer wins: ')
    counterCompWinText.grid(row=1, column=0, sticky=W)
    counterCompWin = Label(statisticsFrame, textvariable=n_comp_win, width=5)
    counterCompWin.grid(row=1, column=1, sticky=W)

    counterPlayerWinText = Label(statisticsFrame, text='Number of {} wins: '.format(player))
    counterPlayerWinText.grid(row=2, column=0, sticky=W)
    counterPlayerWin = Label(statisticsFrame, textvariable=n_player_win, width=5)
    counterPlayerWin.grid(row=2, column=1, sticky=W)

    counterDrawText = Label(statisticsFrame, text='Number of draws: ')
    counterDrawText.grid(row=3, column=0, sticky=W)
    counterDraw = Label(statisticsFrame, textvariable=n_draw, width=5)
    counterDraw.grid(row=3, column=1, sticky=W)

    # counter-percentage
    counterCompPercText = Label(statisticsFrame, text='Percentage of computer wins: ')
    counterCompPercText.grid(row=4, column=0, sticky=W)
    counterCompPerc = Label(statisticsFrame, textvariable=n_comp_perc, width=5)
    counterCompPerc.grid(row=4, column=1, sticky=W)

    counterPlayerPercText = Label(statisticsFrame, text='Percentage of {} wins: '.format(player))
    counterPlayerPercText.grid(row=5, column=0, sticky=W)
    counterPlayerPerc = Label(statisticsFrame, textvariable=n_player_perc, width=5)
    counterPlayerPerc.grid(row=5, column=1, sticky=W)

    counterDrawPercText = Label(statisticsFrame, text='Percentage of draws: ')
    counterDrawPercText.grid(row=6, column=0, sticky=W)
    counterDrawPerc = Label(statisticsFrame, textvariable=n_draw_perc, width=5)
    counterDrawPerc.grid(row=6, column=1, sticky=W)

    # counter-choices
    # counter-which choice wins most time

    ## start root - BUTTONS
    # rock button
    rockButtonImg = PhotoImage(file = srcPath+r'\img\rock_trans.png')
    rockButtonImg = rockButtonImg.subsample(1,1)
    rockButton = Button(startRoot, image=rockButtonImg, bd = 0,
                        command = lambda: show_choice(srcPath+r'\img\rock_trans.png'))
    # rockButton = Button(startRoot, image=rockButtonImg, bd=0, command= lambda: time_sleep(srcPath+r'\img\rock_trans.png'))
    rockButton.image = rockButtonImg
    rockButton.grid(row=4, column=0)

    # paper button
    paperButtonImg = PhotoImage(file = srcPath+r'\img\paper_trans.png')
    paperButtonImg = paperButtonImg.subsample(1,1)
    paperButton = Button(startRoot, image=paperButtonImg, bd = 0,
                        command = lambda: show_choice(srcPath+r'\img\paper_trans.png'))
    paperButton.image = paperButtonImg
    paperButton.grid(row=4, column=1)

    # scissors button
    scissorsButtonImg = PhotoImage(file = srcPath+r'\img\scissors_trans.png')
    scissorsButtonImg = scissorsButtonImg.subsample(1,1)
    scissorsButton = Button(startRoot, image=scissorsButtonImg, bd = 0,
                            command = lambda: show_choice(srcPath+r'\img\scissors_trans.png'))
    scissorsButton.image = scissorsButtonImg
    scissorsButton.grid(row=4, column=2)

    # show more statistics
    # reset button

    # quit game button
    def exit_startRoot():
        startRoot.destroy()

    exit_font = tkFont.Font(size='15', weight='bold')
    exitButton = Button(startRoot, text='EXIT', font=exit_font, activeforeground='orange', relief=RIDGE, bd=0, 
                        command=exit_startRoot)
    exitButton.grid(row=5, column=0, ipadx=10, sticky=W)
    exitButton.bind('<Enter>', on_enter)
    exitButton.bind('<Leave>', on_leave)

start_font = tkFont.Font(size='30', weight='bold')
startButton = Button(root, text='START', font=start_font, activeforeground='orange', relief=RIDGE, bd=0, command=start)
startButton.grid(row=3, column=0, sticky=W)
startButton.bind('<Enter>', on_enter)
startButton.bind('<Leave>', on_leave)

    # change player button
global players
players = ['undefined', 'Patryk', 'Magda']

def change_player():
    chPlayerButton.configure(state=DISABLED)
    startButton.configure(state=DISABLED)

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
            global player
            player = newPlayerName
            nameLabel.destroy()
            show_player_label(player)
        else:
            messagebox.showinfo('CONFIRM ERROR', defaultText)
            return
        
        chPlayerButton.configure(state=NORMAL)
        startButton.configure(state=NORMAL)
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
        startButton.configure(state=NORMAL)

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