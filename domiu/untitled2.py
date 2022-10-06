# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 20:01:53 2022

@author: mazen
"""


from tkinter.messagebox import *
from tkinter import *
from tkinter import Tk
import random
import time
t=time

mostleft=0
mostright=0


card_print = {"   0   0    |   0   0    \n   0   0    |   0   0    \n   0   0    |   0   0    ":[6,6],"   0   0    |   0   0    \n     0      |   0   0    \n   0   0    |   0   0    ":[5,6],"   0   0    |   0   0    \n     0      |     0    \n   0   0    |   0   0    ":[5,5],"   0   0    |   0   0    \n             |   0   0    \n   0   0    |   0   0    ":[4,6],"   0   0    |   0   0    \n            |     0    \n   0   0    |   0   0    ":[4,5],"   0   0    |   0   0    \n            |        \n   0   0    |   0   0    ":[4,4],"    0       |   0   0    \n   0        |   0   0    \n    0       |   0   0    ":[3,6],"    0   |   0   0    \n   0   |     0    \n    0   |   0   0    ":[3,5],"    0   |   0   0    \n 0    |        \n    0   |   0   0    ":[3,4],"    0   |   0    \n   0    |    0   \n    0   |   0    ":[3,3],"    0   |   0   0    \n       |   0   0    \n    0   |   0   0    ":[2,6],"    0   |   0   0    \n       |     0    \n    0   |   0   0    ":[2,5],"    0   |   0   0    \n        |        \n    0   |   0   0    ":[2,4],"    0   |   0    \n        |    0   \n    0   |   0    ":[2,3],"    0   |   0    \n        |        \n    0   |   0    ":[2,2],"        |   0   0    \n   0    |   0   0    \n        |   0   0    ":[1,6],"        |   0   0    \n   0    |     0    \n        |   0   0    ":[1,5],"        |   0   0    \n   0    |        \n        |   0   0    ":[1,4],"        |   0    \n   0    |    0   \n        |   0    ":[1,3],"        |   0    \n   0    |        \n        |   0    ":[1,2],"        |        \n   0    |   0    \n        |        ":[1,1],"        |   0   0    \n        |   0   0    \n        |   0   0    ":[0,6],"        |   0   0    \n        |     0    \n        |   0   0    ":[0,5],"        |   0   0    \n        |        \n        |   0   0    ":[0,4],"        |   0    \n        |    0   \n        |   0    ":[0,3],"        |   0    \n        |        \n        |   0    ":[0,2],"        |        \n        |   0    \n        |        ":[0,1],"        |        \n        |        \n        |        ":[0,0]}

xlef=950
xref=950
yref=200
        
openedleft=0
openedright =0       
         


cards1values=[]
cards2values=[]
allcards=list(card_print.values())
    

keys=list(card_print.keys())
val=list(card_print.values())




#                                             all constants



class card:
    
    
    
    

    def __init__(self,v=[],w=""):
        self.left=v[0]
        self.right=v[1]
        self.view=w
        self.value=v
        
        
        
        
    def isValid(self,openedleft,openedright):
        if(openedleft==self.right):
            return "n&l"
        elif(openedright==self.left):
            return "n&r"
        elif(openedleft==self.left):
            return "r&l"
        elif(openedright==self.right):
            return "r&r"
        else :
            return "non"
        
        
        
        
        
        
        
        
        
    def cardrev(self):
        self.view=self.view[ : :-1]
        

       

def addcomp():
    global compcards
    if(allcards.__len__()!=0):
    
        compcards+=1 
        xind=random.randrange(0,allcards.__len__())
        #to choose a random index
        d=card(allcards[xind],keys[val.index(allcards[xind])])
        arrcardComp.append(d)
        #creat a card have a random pair of num and   view
        cards2values.append(allcards[xind])
        #to add the pair of num to player1 cards list
        ee=Button(text=arrcard[arrcard.__len__()-1].view,font=("Snap ITC",7),bg="gray")
        
        combuts.append(ee)
        
        allcards.remove(allcards[xind])
        callbackcomp(l, r)
    
        
    





    















def addfun():
    
    global mycard
    if allcards.__len__()==0:
        showwarning(title='Message', message="there are no cards to be added.")
    else:
        
        adlab=Label(playRoot,text='ADDED CARDS ',font=("Gill Sans Ultra Bold",10),fg='gray').place(x=180,y=130)
        mycard+=1 
        xind=random.randrange(0,allcards.__len__())
        #to choose a random index
        ap=card(allcards[xind],keys[val.index(allcards[xind])])
        arrcard.append(ap)
        #creat a card have a random pair of num and   view
        cards1values.append(allcards[xind])
        #to add the pair of num to player1 cards list
        apbut=Button(text=arrcard[arrcard.__len__()-1].view,font=("Snap ITC",7),bg="gray",command = lambda x=arrcard.__len__()-1: callback(x) )
        player1buts.append(apbut)
        player1buts[arrcard.__len__()-1].place(x=210,y=150+50*(arrcard.__len__()-7))
        allcards.remove(allcards[xind])
        # print("no valid")
        
        
    #remove it from the cards
        
    
        
        
        
        
        
        
       
    


def gofun():
    global zind
    global firstbut
    global arrcard
    global arrcardComp
    global l 
    global r
    global mostleft
    global mostright
    
    addcard = Button(playRoot,text="add card",font=("Gill Sans Ultra Bold",15),bg="gray",command = lambda:addfun())
    addcard.place(x=xref,y=yref+500)    
    
    q=0




    startgamebut.destroy()




    arrcard=[0]*7
    
    arrcardComp=[0]*7
    for i in range(7):
        xind=random.randrange(0,allcards.__len__())
        #to choose a random index
        arrcard[i]=card(allcards[xind],keys[val.index(allcards[xind])])
        #creat a card have a random pair of num and   view
        cards1values.append(allcards[xind])
        #to add the pair of num to player1 cards list
        allcards.remove(allcards[xind])
        #remove it from the cards
        
    
        
        
        
        
        
        #            
        # 
        # 
        
        
        
        player1buts[i].configure(text=arrcard[i].view,font=("Snap ITC",7))
       
    
    
       #now we want to creat a computer cards
       
  
        yind=random.randrange(0,allcards.__len__())
        # while yind==xind and q<4:   
        #    yind=random.randrange(0,allcards.__len__()) 
        #    q+=1
        
        cards2values.append(allcards[yind])
        arrcardComp[i]=card(allcards[yind],keys[val.index(allcards[yind])])
        allcards.remove(allcards[yind])
    
        combuts[i].configure(text=arrcardComp[i].view)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
  
    

    # for i in range(7):
    #      cardsplayer2[i].destroy()
    zind=random.randrange(0,cards2values.__len__())
    combuts[zind].place(x=xref,y=yref)
    #to take a random card to the new position 
    combuts[zind].configure(text=arrcardComp[zind].view,font=("Snap ITC",9),bg="gray")
    # sepl=Label(playRoot,text='|\n|\n|\n|\n|\n|\n|\n|',font=("Gill Sans Ultra Bold",25),fg='#B30000')
    # sepl.place(x=xref+50,y=yref+100)
    # cards2values.remove(cards2values[zind])
    # 
    # print(cards2values)
    mostleft= combuts[zind]
    mostright= combuts[zind]
    l=arrcardComp[zind].left
    r=arrcardComp[zind].right
       
  
 

usedcard2=[]
def endgame(q):
    global playRoot
    if q=="n":
        showinfo(title='Message', message="YOU LOSE.")
    elif q=="y":
        showinfo(title='Message', message="||congratulation ||\nYOU WIN.")
    playRoot.destroy()
compcards=6        
def callbackcomp(ll,rr):
    
    
    global zind
    global xref
    global xlef
    global yref
    global Cexist
    global l
    global r
    global mostleft
    global mostright
    global t
    global mycard
    global compcards
    
    if mycard==0:
        endgame("y")
    elif compcards==0:
        endgame("n")
    usedcard2.append(zind)
    # print("this is zind "+str(zind))
    # print("this is z ind:")
    # print(zind)
    
    
   
    for i in range(cards2values.__len__()) :
        
        
        if i not in usedcard2 :
    
                
            # zind=random.randrange(0,cards2values.__len__())
            
            if(arrcardComp[i].isValid(l,r)=="n&l"):
                compcards-=1
                oo=Label(playRoot,text=str(compcards),font=("Gill Sans Ultra Bold",19),fg='#14A7A7')   
                oo.place(x=1250,y=100)
                usedcard2.append(i)
                # print("this is i "+str(i))
                # print("_____________... n&l")
                
                # print("comp view ")
                # print(arrcardComp[i].view)
                xlef=xlef-150
                
                combuts[i].configure(text=arrcardComp[i].view,font=("Snap ITC",9),bg="gray")
                combuts[i].place(x=xlef,y=yref)
                Cexist[0]+=1
                if Cexist[0]==3 or Cexist[1]==3:
                    yref+=70    
                    xref=950
                    xlef=950
                    Cexist[0]=0
                    Cexist[1]=0
                    lee=Label(playRoot,text="|\nv",font=("Gill Sans Ultra Bold",12),fg='#B30000')
                    lee.place(x=xref+50,y=yref)
                mostleft=combuts[i]
                
                
                # cards2values.remove(cards2values[i])
                l=arrcardComp[i].left
                # print()
                # print()
                # print()
                # print(xref)
                # print(yref)
                for i in player1buts +combuts :
                    i.configure(bg="gray")
                mostleft.configure(bg="white")
                mostright.configure(bg="white")
                if mycard==0:
                    endgame("y")
                elif compcards==0:
                    endgame("n")
                return
                
            elif(arrcardComp[i].isValid(l,r)=="n&r"):
                compcards-=1
                oo=Label(playRoot,text=str(compcards),font=("Gill Sans Ultra Bold",19),fg='#14A7A7')   
                oo.place(x=1250,y=100)
                usedcard2.append(i)
                # print("this is i "+str(i))
                # print("_____________... n&r")
                # print("comp view ")
                # print(arrcardComp[i].view)
                
                combuts[i].configure(text=arrcardComp[i].view,font=("Snap ITC",9),bg="gray")
                xref=xref+150
                combuts[i].place(x=xref,y=yref)
                Cexist[1]+=1
                if Cexist[0]==3 or Cexist[1]==3:
                    yref+=70    
                    xref=950
                    xlef=950
                    Cexist[0]=0
                    Cexist[1]=0
                    lee=Label(playRoot,text="|\nv",font=("Gill Sans Ultra Bold",12),fg='#B30000')
                    lee.place(x=xref+50,y=yref)
                mostright=combuts[i]
                
                # cards2values.remove(cards2values[i])
                r=arrcardComp[i].right
                # print()
                # print()
                # print()
                # print(xref)
                for i in player1buts +combuts :
                    i.configure(bg="gray")
                mostleft.configure(bg="white")
                mostright.configure(bg="white")# print(yref)                
                if mycard==0:
                    endgame("y")
                elif compcards==0:
                    endgame("n")
                return
                
            elif(arrcardComp[i].isValid(l,r)=="r&r"):
                compcards-=1
                oo=Label(playRoot,text=str(compcards),font=("Gill Sans Ultra Bold",19),fg='#14A7A7')   
                oo.place(x=1250,y=100)
                usedcard2.append(i)
                # print("this is i "+str(i))
                # print("_____________... r&r")
                # print("comp view ")
                # print(arrcardComp[i].view)
                # arrcard[x].cardrev()
                arrcardComp[i].cardrev()
                combuts[i].configure(text=arrcardComp[i].view,font=("Snap ITC",9),bg="gray")
                xref=xref+150
                combuts[i].place(x=xref,y=yref)
                Cexist[1]+=1
                if Cexist[0]==3 or Cexist[1]==3:
                    yref+=70    
                    xref=950
                    xlef=950
                    Cexist[0]=0
                    Cexist[1]=0
                    lee=Label(playRoot,text="|\nv",font=("Gill Sans Ultra Bold",12),fg='#B30000')
                    lee.place(x=xref+50,y=yref)
                mostright=combuts[i]
                
                # cards2values.remove(cards2values[i])
                r=arrcardComp[i].left
                # print()
                # print()
                # print()
                # print(xref)
                for i in player1buts +combuts :
                    i.configure(bg="gray")
                mostleft.configure(bg="white")
                mostright.configure(bg="white")# print(yref)         
                if mycard==0:
                    endgame("y")
                elif compcards==0:
                    endgame("n")
                return
                
            elif(arrcardComp[i].isValid(l,r)=="r&l"):
                compcards-=1
                oo=Label(playRoot,text=str(compcards),font=("Gill Sans Ultra Bold",19),fg='#14A7A7')   
                oo.place(x=1250,y=100)
                usedcard2.append(i)
                # print("this is i "+str(i))
                # print("_____________... r&l")
                # print("comp view ")
                # print(arrcardComp[i].view)
                # arrcard[x].cardrev()
                arrcardComp[i].cardrev()
                
                combuts[i].configure(text=arrcardComp[i].view,font=("Snap ITC",9),bg="gray")
                xlef=xlef-150
                combuts[i].place(x=xlef,y=yref)
                Cexist[0]+=1
                if Cexist[0]==3 or Cexist[1]==3:
                    yref+=70    
                    xref=950
                    xlef=950
                    Cexist[0]=0
                    Cexist[1]=0
                    lee=Label(playRoot,text="|\nv",font=("Gill Sans Ultra Bold",12),fg='#B30000')
                    lee.place(x=xref+50,y=yref)
                mostleft=combuts[i]
                
                # cards2values.remove(cards2values[i])
                l=arrcardComp[i].right
                for i in player1buts +combuts :
                    i.configure(bg="gray")
                mostleft.configure(bg="white")
                mostright.configure(bg="white")# print()
                # print()
                # print()
                # print(xref)
                # print(yref)  
                if mycard==0:
                    endgame("y")
                elif compcards==0:
                    endgame("n")
                return
                 
        
    
    
    addcomp()
    
    




















numExist=0


usedcard=[]


def noact(Cexist):

    showwarning(title='Message', message="this card is already used.")
    

mycard=7

Cexist=[0,0]        
def callback(wantedcard):
    global xref
    global xlef
    global yref
    global l 
    global r
    global Cexist
    global usedcard
    global mostleft
    global mostright
    global mycard
    # global ysrt
    # print(arrcard[wantedcard].isValid(l,r))
    # combuts[zind].configure(text=arrcardComp[zind].view,font=("Gill Sans Ultra Bold",5),bg="gray")
    # combuts[zind].place(x=1455,y=220)
    # print("++++++++++++++++++++++++++++++++++++++++")
    # print(Cexist[0])
    # print(Cexist[1])

   
    
    if(arrcard[wantedcard].isValid(l,r)=="non")   :
        showwarning(title='Message', message="this card is not valid to use.")
    elif(arrcard[wantedcard].isValid(l,r)=="n&l"):
        if wantedcard in usedcard: 
            player1buts[wantedcard].configure(command=noact(Cexist),font=("Snap ITC",9))        
        else:
            xlef=xlef-150
            player1buts[wantedcard].place(x=xlef,y=yref)
            player1buts[wantedcard] .configure(font=("Snap ITC",9))
            
            l=arrcard[wantedcard].left
            # ysrt-=50hj
            # cards1values.remove(cards1values[wantedcard])
    
            Cexist[0]+=1
            if Cexist[0]==3 or Cexist[1]==3:
                yref+=70
                xref=950
                xlef=950
                Cexist[0]=0
                Cexist[1]=0
                lee=Label(playRoot,text="|\nv",font=("Gill Sans Ultra Bold",12),fg='black')
                lee.place(x=xref+50,y=yref)
            mostleft=player1buts[wantedcard]
            for i in player1buts +combuts :
                        i.configure(bg="gray")
                        # combuts[i].configure(bg="gray")
            mostleft.configure(bg="white")
            mostright.configure(bg="white")
            usedcard.append(wantedcard)
            mycard-=1
            t.sleep(0.9)
            callbackcomp(l,r)
    elif(arrcard[wantedcard].isValid(l,r)=="n&r"):
        if wantedcard in usedcard: 
            player1buts[wantedcard].configure(command=noact(Cexist),font=("Snap ITC",9))   
        else:    
            xref=xref+150
            player1buts[wantedcard].place(x=xref,y=yref)
            player1buts[wantedcard] .configure(font=("Snap ITC",9))
            
            r=arrcard[wantedcard].right
            # ysrt-=50
            # cards1values.remove(cards1values[wantedcard])
    
            Cexist[1]+=1
            if Cexist[0]==3 or Cexist[1]==3:
                yref+=70
                xref=950
                xlef=950
                Cexist[0]=0
                Cexist[1]=0
                lee=Label(playRoot,text="|\nv",font=("Gill Sans Ultra Bold",12),fg='#B30000')
                lee.place(x=xref+50,y=yref)
            mostright=player1buts[wantedcard]
            for i in player1buts +combuts :
                        i.configure(bg="gray")
                        # combuts[i].configure(bg="gray")
            mostleft.configure(bg="white")
            mostright.configure(bg="white")
            usedcard.append(wantedcard)
            mycard-=1
            t.sleep(0.9)
            callbackcomp(l,r)
    elif(arrcard[wantedcard].isValid(l,r)=="r&r"):
        if wantedcard in usedcard: 
            player1buts[wantedcard].configure(command=noact(Cexist),font=("Snap ITC",9))  
        else:
            xref=xref+150
            arrcard[wantedcard].cardrev()
            player1buts[wantedcard].configure(text=arrcard[wantedcard].view,font=("Snap ITC",9))
            
            
            player1buts[wantedcard].place(x=xref,y=yref)
            
            r=arrcard[wantedcard].left
            # ysrt-=50
            # cards1values.remove(cards1values[wantedcard])
    
            Cexist[1]+=1
            if Cexist[0]==3 or Cexist[1]==3:
                yref+=70    
                xref=950
                xlef=950
                Cexist[0]=0
                Cexist[1]=0
                lee=Label(playRoot,text="|\nv",font=("Gill Sans Ultra Bold",12),fg='#B30000')
                lee.place(x=xref+50,y=yref)
            mostright=player1buts[wantedcard]
            for i in player1buts +combuts :
                        i.configure(bg="gray")
                        # combuts[i].configure(bg="gray")
            mostleft.configure(bg="white")
            mostright.configure(bg="white")
            usedcard.append(wantedcard)
            mycard-=1
            t.sleep(0.9)
            callbackcomp(l,r)
    elif(arrcard[wantedcard].isValid(l,r)=="r&l"):
        if wantedcard in usedcard: 
            player1buts[wantedcard].configure(command=noact(Cexist),font=("Snap ITC",9))
        else:
            xlef=xlef-150
            arrcard[wantedcard].cardrev()
            
            player1buts[wantedcard].configure(text=arrcard[wantedcard].view,font=("Snap ITC",9))
            
            
            
            player1buts[wantedcard].place(x=xlef,y=yref)
            
            l=arrcard[wantedcard].right
            # ysrt-=50
            # cards1values.remove(cards1values[wantedcard])
    
            Cexist[0]+=1.
            if Cexist[0]==3 or Cexist[1]==3:
                yref+=70
                xref=950
                xlef=950
                Cexist[0]=0
                Cexist[1]=0
                lee=Label(playRoot,text="|\nv",font=("Gill Sans Ultra Bold",12),fg='#B30000')
                lee.place(x=xref+50,y=yref)
            mostleft=player1buts[wantedcard]
            for i in player1buts +combuts :
                        i.configure(bg="gray")
                        # combuts[i].configure(bg="gray")
                        
            mostleft.configure(bg="white")
            mostright.configure(bg="white")
            usedcard.append(wantedcard)
            mycard-=1
            t.sleep(0.9)
            callbackcomp(l,r)
        
# ysrt=140


def startPlay():
    global labPlayerr2
    global cardsplayer2
    global startgamebut
    global playRoot
    global player1buts
    global combuts
    global l
    global r
    global compcards
    # global ysrt
    
    mainRoot.destroy()
    
    
    
    
    
    
    
    
    
    
    
    playRoot=Tk()
    playRoot.title("play")
    w=playRoot.winfo_screenwidth()
    h=playRoot.winfo_screenheight()
    playRoot.geometry("%dx%d+0+0"%(w,h))

    bilmLabel=Label(playRoot,text="  Domiu   GAME  ",cursor='heart',font=("Jokerman",65,"bold"),bg='#14A7A7', fg='white')
    bilmLabel.pack()
    # showinfo(title='Message', message=" information of the game:\n  ________________________________\n\n ")
    # gameEnterybut=Button(playRoot,text="   0   0    |   0   0    \n        |        \n   0   0    |   0   0    ",font=("Bernard MT Condensed",20),cursor='hand2',bg="#BEBEBE")
    # gameEnterybut.place(x=1000,y=500)
    labPlayerr1=Label(playRoot,text='YOUR CARDS ',font=("Gill Sans Ultra Bold",25),fg='#B30000')   
    labPlayerr1.place(x=50,y=70)
    labPlayerr2=Label(playRoot,text="COMPUTER CARDS",font=("Gill Sans Ultra Bold",19),fg='#14A7A7')   
    labPlayerr2.place(x=1250,y=70)

























    player1buts = [0]*7
    for i in range(7):
        player1buts[i] = Button(playRoot,text="\n\n\n                                ",font=("Snap ITC",7),bg="gray",command = lambda x=i: callback(x))
        player1buts[i].place(x=50,y=140+i*50)
        

    combuts = [0]*7
    for i in range(7):
        combuts[i] = Button(playRoot,text="\n\n\n                                ",font=("Snap ITC",7),bg="gray")
        # combuts[i].place(x=1350,y=140+i*50)
        
        
        




    
    
    startgamebut=Button(playRoot,text="GO",font=("Gill Sans Ultra Bold",40),bg="grey",command = lambda:gofun())
    startgamebut.place(x=700,y=300)


    
    playRoot.mainloop()
    













































def main():
    global mainRoot
    mainRoot=Tk()
    mainRoot.title("domiu game")
    w=mainRoot.winfo_screenwidth()
    h=mainRoot.winfo_screenheight()
    mainRoot.geometry("%dx%d+0+0"%(w,h))
    wellcome=Label(mainRoot,text="WELCOME in:",font=("Bernard MT Condensed",100),fg="#BEBEFE")
    wellcome.pack()
    domLabel=Label(mainRoot,text="  Domiu   GAME  ",cursor='heart',font=("Jokerman",120,"bold"),bg='#14A7A7', fg='white')
    domLabel.pack()
    startButton=Button(mainRoot,text="START",font=("Bernard MT Condensed",40,"bold"),cursor='hand2',bg="#BEBEBE",command= lambda:startPlay() )
    startButton.place(x=720,y=600)    
    
    
    
    
    
    
    
    
    
    mainRoot.mainloop()
if __name__=="__main__":main()
