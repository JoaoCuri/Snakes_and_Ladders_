import tkinter as tk
from PIL import ImageTk,Image
import random
from tkinter import messagebox

rodada=1

dic={1:(30,295),2:(85,295),3:(140,295),4:(190,295),5:(245,295),6:(310,295),
     7:(310,240),8:(245,240),9:(190,240),10:(140,240),11:(85,240),12:(30,240),
     13:(30,185),14:(85,185),15:(140,185),16:(190,185),17:(245,185),18:(310,185),
     19:(310,130),20:(245,130),21:(190,130),22:(140,130),23:(85,130),24:(30,130),
     25:(30,75),26:(85,75),27:(140,75),28:(190,75),29:(245,75),30:(310,75),
     31:(310,20),32:(245,20),33:(190,20),34:(140,20),35:(85,20),36:(30,20)}

def star_game():
    global im
    global b1,b2
    
    
    
        
    #players buttons
    #player 1
    #b1=tk.Button(root,text='player 1',bg="#3085C3",fg="white",command=jogando_o_dado)
    b1.place(x=400,y=250)

    #b2=tk.Button(root,text='player 2',bg="#016A70",fg="white",command=jogando_o_dado)
    b2.place(x=400,y=300)

    #dado
    im=Image.open('dado.png')
    im=im.resize((60,60))
    im=ImageTk.PhotoImage(im)
    
    

    exite=tk.Button(root,text='Para o Jogo',bg="red",fg="white",command=reset_game)
    exite.place(x=400,y=10)
    
def reset_game():
    global player_1,player_2
    global ps1,ps2
    
    #posição inicial dos jogadores
    player_1.place(x=30,y=295)
    player_2.place(x=30,y=295)
    
    ps1=1
    ps2=1
    
def Load_faces_do_dado():
    global dado
    #nomes=['1.png','2.png','3.png','4.png','5.png','6.png']
    for i in range(1,7):        
        im=Image.open(f'{i}.png')
        im=im.resize((60,60))
        im=ImageTk.PhotoImage(im)        
        dado.append(im)
        
def check_ladders_rodada(Rodada):
    global ps1,ps2
    global ladders
    
    f=0
    if rodada==1:
        if ps1 in ladders:
            ps1 = ladders[ps1]
            f=1
    else:
        if ps2 in ladders:
            ps2 = ladders[ps2]
            f=1
    return f

def check_snake(Rodada):
    global ps1,ps2
    if Rodada ==1:
        if ps1 in snakes:
            ps1=snakes[ps1]
    else:
        if Rodada ==2:
            if ps2 in snakes:
                ps2=snakes[ps2]
    
def jogando_o_dado():
    global dado
    global rodada
    global ps1,ps2
    global b1,b2  
    
      
    
    r = random.randint(1, 6)    
    b3=tk.Button(root,image=dado[r-1],height=55,width=55,bg="white")
    b3.place(x=400,y=100)
    
    
    
    if rodada==1:        
        
        if (ps1+r)<=36:
            ps1+=r
            print(ps1)
            print(f'player 1:{ps1}')
            
        Lad=check_ladders_rodada(rodada)
        check_snake(rodada)
        move_players(rodada,ps1)
        #if r!=6 and Lad!=1:
        rodada=2
        b1.configure(state='disable')
        b2.configure(state='normal')
            
    
              
        
    else:
        if (ps2+r)<=36:
            ps2+=r
            print(ps2)
            print(f'player 2:{ps2}')
        Lad=check_ladders_rodada(rodada)
        check_snake(rodada)
        move_players(rodada,ps2)
        #if r!=6 and Lad!=1 :  
        rodada=1
        b2.configure(state='disable')
        b1.configure(state='normal')
            
        
    winner()
    #move_players(r)
def winner():
    global ps1,ps2
    
    if ps1==36:
        msg='player 1 venceu'
        messagebox.showinfo("info", msg)
        reset_game()
    elif ps2==36:
        msg='player 2 venceu'
        messagebox.showinfo("info", msg)
        reset_game()
    
        
    
def move_players(Rodada,r):
    global player_1,player_2
    #global Index
    
    if(Rodada==1):
        player_1.place(x=dic[r][0],y=dic[r][1])
    else:
        player_2.place(x=dic[r][0],y=dic[r][1])
    

dado=[]

#coordenadas x e y
Index={}

#posições iniciais dos jogadores
ps1=1
ps2=1

ladders = {3: 16, 5: 7, 15: 25, 18: 20, 21: 32}
snakes = {12: 2, 14: 11, 17: 4, 31: 19, 35: 22}

root=tk.Tk()
root.geometry('500x360')
root.configure(bg='#FAF2D3')

f1=tk.Frame(root,width=368,height=360,relief='raised')
f1.place(x=0,y=0)

#imagens
#Board game
img1 = ImageTk.PhotoImage(Image.open('S&L.png'))
lab = tk.Label(f1,image=img1)
lab.pack()

b1=tk.Button(root,text='player 1',bg="#3085C3",fg="white",command=jogando_o_dado)
b2=tk.Button(root,text='player 2',bg="#016A70",fg="white",command=jogando_o_dado)

#peça jogador 1
player_1 = tk.Canvas(root,width=15,height=15)
player_1.create_oval(2,2,15,15,fill="#3085C3")


#peça jogador 2
player_2 = tk.Canvas(root,width=15,height=15)
player_2.create_oval(2,2,15,15,fill="green")

#player 1 inicia o jogo
rodada=1

#volta os jogadores p/ posição inicial
reset_game()

#get_index()

Load_faces_do_dado()

star_game()


root.mainloop()