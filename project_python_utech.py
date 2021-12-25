import tk#inter as tk
import random # plain random module, not numpy's
import numpy as np
from random import shuffle
import random
from PIL import Image, ImageTk
import os.path
from tk import messagebox
import time
import os
from playsound import playsound
import pygame



    
''' in this game you have to choose all block that is not bomb and
    for help each block that you choose show you how many of neighbor block are bomb.
    if you choose bomb block you lose the game and if you choose all safe block you win'''
        
'''minesweeper --->  level_of_game ------>  game_page  ----->   play
                                   ------>  help
'''
def minesweeper():
    
    
    #  window configuration
    global win    
    win = tk.Tk()
    win.resizable(False,False)
    win.minsize(500,500)
    win.title('minesweeper')
    win.configure(bg='gray83')
    
    game_photo = tk.PhotoImage(file = 'download.png')    # icon for game
    win.iconphoto(True,game_photo)

    ###############################################################
    # -------------------first page : welcom page ----------------#
    ###############################################################
    global welcom_page_photo
    welcom_page_photo = tk.Label(win,compound = tk.CENTER,image=game_photo,background='gray83')
    welcom_page_photo.image = game_photo
    welcom_page_photo.config(font=("mitra", 25),foreground = 'darkorange')
    welcom_page_photo.place(x = 150,y = 200)
    welcom_page_photo.bind('<Button>',lambda _:level_of_game())
        
    global welcom_page_label
    welcom_page_label = tk.Label(win,text = 'minesweeper',background='gray83')
    welcom_page_label.config(font=("mitra", 25))
    welcom_page_label.place(x = 150,y = 100)
    welcom_page_label.bind('<Button>',lambda _:level_of_game())
        
    pygame.mixer.init() # music of game
    pygame.mixer.music.load('1.mp3')
    pygame.mixer.music.play(loops=120)


    
    ###############################################################
    # -------------------------variation--------------------------#
    ###############################################################
    global worn_label
    worn_label = tk.Label(win)
    worn_label.place(x=700,y=700)
    
    global bomb
    bomb = 0
    global logo_photo1
    logo1 = tk.PhotoImage(file = 'download-Copy.png')
    logo_photo1 = tk.Label(win,image=logo1,background='gray83')
    logo_photo1.image = logo1
        
    global board_frame
    board_frame = tk.Frame(win)
    board_frame.config( highlightbackground="gray83",relief = "ridge", highlightcolor='gray25', highlightthickness=6)

    global board_frame1
    board_frame1 = tk.Frame(win)
    board_frame1.config( highlightbackground="gray77",relief = "ridge", highlightcolor='gray77', highlightthickness=8)
    
    global files
    global sound_photo1
    files = 'download111.png'
    sound1 = tk.PhotoImage(file = files)
    sound_photo1 = tk.Label(board_frame1,image=sound1,background='gray83',relief = "flat")
    sound_photo1.image = sound1
    sound_photo1.bind('<Double-Button>',lambda _:sound())


    global home_photo1
    home1 = tk.PhotoImage(file = 'download333.png')
    home_photo1 = tk.Label(board_frame1,image=home1,relief = "flat",background='gray83')
    home_photo1.image = home1
    home_photo1.bind('<Double-Button>',lambda _:home())


    global reset_btn
    reset = tk.PhotoImage(file = 'download444.png')
    reset_btn = tk.Label(board_frame1,image=reset,relief = "flat",background='gray83')
    reset_btn.image = reset
    reset_btn.bind('<Double-Button>',lambda _:game_page())
    


        
def level_of_game():
    #   delete first page
    welcom_page_label.place_forget()
    welcom_page_photo.place_forget()
    
    
    ###############################################################
    # ------------second page : choose level of game -------------#
    ###############################################################
    
    global logo_photo
    logo = tk.PhotoImage(file = 'download-Copy.png')
    logo_photo = tk.Label(win,image=logo,background='gray83')
    logo_photo.image = logo
    logo_photo.place(x = 200,y = 20)

    
    global hardness
    global hardness_label
    hardness = tk.StringVar()# easy/medium/hard
    hardness_label = tk.Label(win,text = 'level of game')
    hardness_label.config(font = 'mitra',background='gray83',foreground = 'black')
    hardness_label.place(x=190,y = 150)


    global hardness_om  #   Choose how hard it is
    hardness_om = tk.OptionMenu(win,hardness,'easy','medium','hard')
    hardness_om.config(width = 12,height = 1,background='gray83',activebackground='gray83',foreground = 'black')
    hardness_om.place(x=190,y=180)

    
    global help_btn #   help : explanation of the game
    help_btn = tk.Button(win,text = 'help')
    help_btn.config(font = 'mitra',activeforeground = 'red',activebackground = 'gray83',background='gray83',foreground = 'black')
    help_btn.bind('<Button>',lambda _:helpp())
    help_btn.place(x = 190 ,y = 250,width = 115,height = 30 )

    
    global start_btn    #   start the game
    start_btn = tk.Button(win,text = 'start')
    start_btn.config(font = 'mitra',activeforeground = 'green',activebackground = 'red',background='red',foreground = 'black')
    start_btn.bind('<Button>',lambda _:game_page())
    start_btn.place(x = 170 ,y = 350,width = 150,height = 50 )

    global worn_label # how many bomb there are
    worn_label = tk.Label(win)
    
    
    
    


def  game_page():
        
    #   delete second page
    logo_photo.place_forget()
    hardness_label.place_forget()
    hardness_om.place_forget()
    help_btn.place_forget()
    start_btn.place_forget()
    
    ###############################################################
    # ----------------third page : game page----------------------#
    ###############################################################
    global dimention
    global dim
    global bomb
    dimention = 0 # dimention of table(3/5/7)
    bomb = 0 #  number of bomb
    dim = 0
    
    # menu bar : design of game page-------------------------------    
    logo_photo1.place(x = 400,y = 400)
    sound_photo1.grid(row=3,column=1)
    home_photo1.grid(row=1,column=1)
    reset_btn.grid(row=2,column=1)
    worn_label.place(x = 200 ,y = 10)
    
    board_frame1.place(x = 0,y = 0)
    
    # draw table : game block   ------------------------------------------------------------------------    
    
    if hardness.get()== 'easy':
        dimention,dim ,bomb = 3,3, 2
    elif hardness.get()=='medium':
        dimention,dim ,bomb = 5,2, 7 
    elif hardness.get()=='hard':
        dimention,dim ,bomb = 7,1, 13
    if dimention ==0:
        home()
    board_frame.place(x=60,y=25)    # full size table (7,7) # it's optional that draw this and then active the dimention that user wants or directly draw table in dimention that user wants
    
    global coords_list 
    global buttons_dict
    coords_list = []
    buttons_dict = {}
    for r in range(1,8):
        for c in range(1,8):
            coord = str(r)+"_"+str(c)
            coords_list.append(coord)
            buttons_dict[coords_list[-1]] = tk.Button(board_frame, width=6,height = 3,relief = "ridge",background='gray83')
            if r>=dim and c>=dim and r<=8-dim and c<=8-dim:
                ###########################################################################
                buttons_dict[coords_list[-1]]["command"] = lambda x=r, y=c: play(x,y)
                buttons_dict[coords_list[-1]].config(bg='gray35',relief = "raised")
                ###########################################################################
            buttons_dict[coords_list[-1]].grid(row=r,column=c)
   
    worn_label.config(text = 'there is '+str(bomb)+' bomb!!! be carefull',background='gray83',activebackground='gray83',foreground = 'darkorange')    
    worn_label.place(x = 200 ,y = 10)
    global data #   array as table(game blocks)
    data = [0] * ((dimention*dimention)-bomb) + [100] * bomb
    shuffle(data)
    data = np.array(data)
    data = data.reshape(dimention,dimention)
    global winner
    winner = np.zeros((dimention,dimention))
    global aaa
    aaa = zip(np.where(data >90)[0],np.where(data >90)[1])
    global bomb_pos
    bomb_pos = []
    #   neighbors number of bomb
    for (i,j) in aaa:
        winner[i][j]=2
        bomb_pos.append((i,j))
        print('bomb position:',i+1,j+1)
        if i-1>=0:
            data[i-1][j] +=1
            if j-1>=0:
                data[i-1][j-1] +=1
            if j+1<dimention:
                data[i-1][j+1] +=1
                        
        if i+1<dimention:
            data[i+1][j] +=1
            if j-1>=0:
                data[i+1][j-1] +=1
            if j+1<dimention:
                data[i+1][j+1] +=1
        if j-1>=0:    
            data[i][j-1] +=1
        if j+1<dimention:
            data[i][j+1] +=1

def home():
    logo_photo1.place_forget()
    board_frame.place_forget()
    board_frame1.place_forget()
    worn_label.place_forget()
    level_of_game()

        
def play(x, y):
    #   after every click on the table this function run 
    bomb_list =[]
    isbomb =0   
    print('mypos',x-dim+1,y-dim+1)
    for k in range(len(bomb_pos)):
        (i,j) = bomb_pos[k]
        if (x-dim+1-1)==i and (y-dim+1-1)==j:   # if block that click on is bomb
            isbomb = 1
            photo22=tk.PhotoImage(file="images(8).png")
                    
            #l.config(win,image=photo1)
            buttons_dict[str(x)+"_"+str(y)].config(image=photo22,width="48",height="48",bd=1)
            buttons_dict[str(x)+"_"+str(y)].image=photo22
            #board_frame.place_forget()
            label4 = tk.Label(win,text = 'Game over')
            label4.config(bg = 'red',font = ('mitra',25))
            label4.place(x = 150,y = 200)
            try_again = messagebox.askyesno('do you want try again?')
            if try_again ==True:
                label4.place_forget()
                game_page()
                    
            elif try_again ==False:
                EXIT = messagebox.askyesno('close the app?')
                if EXIT==True:
                    win.destroy()
                elif EXIT==False :
                    label4.place_forget()
                    worn_label.place_forget()
                    home()
    global win_photo
    if isbomb==0:
        #print('answer:\n',x,y,data)
        buttons_dict[str(x)+"_"+str(y)].config(bg = 'gray76',relief = "sunken",text = str(data[x-dim+1-1][y-dim+1-1]))
        if 0 in winner:
            winner[x-dim+1-1][y-dim+1-1]=1
            if 0 not in winner:
                print('you win')
                game_photo11 = tk.PhotoImage(file = '5330082-win-png-97-images-in-collection-page-3-win-png-423_169_preview.png')    # icon for game
                win_photo = tk.Label(win,compound = tk.CENTER,image=game_photo11,background='gray83')
                win_photo.image = game_photo11
                win_photo.config(font=("mitra", 25),foreground = 'darkorange')
                win_photo.place(x = 30,y = 200)
                try_again = messagebox.askyesno('do you want try again?')
                if try_again ==True:
                    win_photo.place_forget()
                    
                    game_page()        
                elif try_again ==False:
                    EXIT = messagebox.askyesno('close the app?')
                    if EXIT==True:
                        pygame.mixer.music.stop()
                        win.destroy()
                    elif EXIT==False :
                        win_photo.place_forget()
                        worn_label.place_forget()
                        home()
                        




    
        
def sound():
    global files
    if files =='download222.png':
        pygame.mixer.music.play(loops=120)
        #sound_photo1.place_forget()
        sound1 = tk.PhotoImage(file = 'download111.png')
        sound_photo1 = tk.Label(board_frame1,image=sound1,background='gray83',relief = "flat")
        sound_photo1.image = sound1
        sound_photo1.bind('<Double-Button>',lambda _:sound())
        sound_photo1.grid(row=3,column=1)
        files ='download111.png'

    else :
        pygame.mixer.music.stop()
        #sound_photo1.place_forget()
        sound1 = tk.PhotoImage(file = 'download222.png')
        sound_photo1 = tk.Label(board_frame1,image=sound1,background='gray83',relief = "flat")
        sound_photo1.image = sound1
        sound_photo1.bind('<Double-Button>',lambda _:sound())
        sound_photo1.grid(row=3,column=1)
        files ='download222.png'
    sound_photo1.grid(row=3,column=1)

    
def helpp():

    
    global explanation_win
    explanation_win = tk.Toplevel(win)
    explanation_win.resizable(False,False)
    explanation_win.minsize(300,300)
    explanation_win.title('help')
    explanation_win.configure(bg='gray83')
    helppp1 = '1. find all block that is not bomb'
    helppp2 = '2. each block show number of neighbor bomb block'
    helppp3 = '3. if you choose bomb block you lose'
    helppp4 = '4. if you choose all safe block you win'
    explanation_label1 = tk.Label(explanation_win,text = helppp1,bg='gray83')
    explanation_label1.place(x =0 ,y = 0 )
    explanation_label2 = tk.Label(explanation_win,text = helppp2,bg='gray83')
    explanation_label2.place(x =0 ,y = 50 )
    explanation_label3 = tk.Label(explanation_win,text = helppp3,bg='gray83')
    explanation_label3.place(x =0 ,y = 100 )
    explanation_label4 = tk.Label(explanation_win,text = helppp4,bg='gray83')
    explanation_label4.place(x =0 ,y = 150 )
        
    close_btn = tk.Button(explanation_win,text = 'close',command = explanation_win.destroy)
    close_btn.config(font = 'mitra',activeforeground = 'red',activebackground = 'gray83',background='gray83',foreground = 'black')
    close_btn.place(x = 120 ,y = 250,width = 60,height = 30 )
minesweeper()   
win.mainloop()
pygame.mixer.music.stop()
while(1):
    pass
