from Tkinter import *
import time

diff='Easy'
class Character:
    def __init__(self):
        # opening image files 
        self.dwn1=PhotoImage(file='Char1.1.gif')
        self.dwn2=PhotoImage(file='Char1.2.gif')
        self.dwn22=PhotoImage(file='Char1.21.gif')
        self.dwn3=PhotoImage(file='Char1.3.gif')
        
        self.l1=PhotoImage(file='Char2.1.gif')
        self.l2=PhotoImage(file='Char2.2.gif')
        self.l3=PhotoImage(file='Char2.3.gif')
        
        self.r1=PhotoImage(file='Char3.1.gif')
        self.r2=PhotoImage(file='Char3.2.gif')
        self.r3=PhotoImage(file='Char3.3.gif')
        
        self.up1=PhotoImage(file='Char4.1.gif')
        self.up2=PhotoImage(file='Char4.2.gif')
        self.up3=PhotoImage(file='Char4.3.gif')
        
        self.wall1=PhotoImage(file='wall1.gif')
        self.rocks=PhotoImage(file='Rock 2.gif')
        self.end=PhotoImage(file='end.gif')
        self.fin=PhotoImage(file='Fin.gif')
        
        self.door1=PhotoImage(file='Door 1.gif')
        self.door2=PhotoImage(file='Door 2.gif')
        self.door3=PhotoImage(file='Door 3.gif')
        self.door4=PhotoImage(file='Door 4.gif')
        self.door5=PhotoImage(file='Door 5.gif')
        self.door6=PhotoImage(file='Door 6.gif')
        
        self.crown=PhotoImage(file='Item 3.gif')
        #self.crown0=PhotoImage(file='3-final.gif')
        self.crown1=PhotoImage(file='crown1.gif')
        self.crown2=PhotoImage(file='crown2.gif')
        
        self.gold=PhotoImage(file='Gold bars.gif')
        #self.gold0=PhotoImage(file='7-final.gif')
        self.gold1=PhotoImage(file='gold1.gif')
        self.gold2=PhotoImage(file='gold2.gif')
        self.gold3=PhotoImage(file='gold3.gif')
        self.gold4=PhotoImage(file='gold4.gif')
        self.gold5=PhotoImage(file='gold5.gif')
        self.gold6=PhotoImage(file='gold6.gif')
        self.gold7=PhotoImage(file='gold7.gif')
        
        self.key=PhotoImage(file='Key.gif')
        #self.key0=PhotoImage(file='4-final.gif')
        self.key1=PhotoImage(file='key1.gif')
        self.key2=PhotoImage(file='key2.gif')
        self.key3=PhotoImage(file='key3.gif')
        
        self.lantern=PhotoImage(file='Item 2.gif')
        #self.lantern0=PhotoImage(file='2-final.gif')
        self.lantern1=PhotoImage(file='lantern1.gif')
        
        self.mud=PhotoImage(file='Mud.gif')
        #self.mud0=PhotoImage(file='5-final.gif')
        self.mud1=PhotoImage(file='mud1.gif')
        self.mud2=PhotoImage(file='mud2.gif')
        
        self.paper=PhotoImage(file='Paper 1.gif')
        #self.paper0=PhotoImage(file='6-final.gif')
        self.paper1=PhotoImage(file='paper1.gif')
        self.paper2=PhotoImage(file='paper2.gif')
        self.paper3=PhotoImage(file='paper3.gif')
        self.paper4=PhotoImage(file='paper4.gif')
        self.paper5=PhotoImage(file='paper5.gif')
        self.paper6=PhotoImage(file='paper6.gif')
        self.paper7=PhotoImage(file='paper7.gif')
        self.paper8=PhotoImage(file='paper8.gif')
        self.paper9=PhotoImage(file='paper9.gif')
        self.paper10=PhotoImage(file='paper10.gif')
        self.paper11=PhotoImage(file='paper11.gif')
        self.paper12=PhotoImage(file='paper12.gif')
        self.paper13=PhotoImage(file='paper13.gif')
        self.paper14=PhotoImage(file='paper14.gif')
        self.paper15=PhotoImage(file='paper15.gif')
        
        self.wand=PhotoImage(file='Item 1.gif')
        #self.wand0=PhotoImage(file='1-final.gif')
        self.wand1=PhotoImage(file='wand1.gif')
        self.wand2=PhotoImage(file='wand2.gif')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

class Mode:
    # map for different difficulties
    def __init__(self):
        self.wallCoord_easy=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
                             [1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,24],
                             [1,24],
                             [1,6,7,8,9,10,11,14,15,16,17,18,19,24],
                             [1,6,7,8,9,10,11,14,15,16,17,18,19,24],
                             [1,2,4,5,6,7,8,9,10,11,14,15,16,17,18,19,20,21,23,24],
                             [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24],
                             [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24],
                             [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24],
                             [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24],
                             [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24],
                             [1,2,4,5,6,7,8,9,10,15,16,17,18,19,20,21,23,24],
                             [1,2,15,16,17,18,23,24],
                             [1,2,15,16,17,18,23,24],
                             [1,2,4,5,6,7,8,9,10,15,16,17,18,19,20,21,23,24],
                             [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24],
                             [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24],
                             [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24],
                             [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24],
                             [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24],
                             [1,2,4,5,6,7,8,9,10,11,14,15,16,17,18,19,20,21,23,24],
                             [1,6,7,8,9,10,11,14,15,16,17,18,19,24],
                             [1,6,7,8,9,10,11,14,15,16,17,18,19,24],
                             [1,24],
                             [1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,24],
                             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]]              
        self.wallCoord_medi=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
                             [1,2,3,4,5,6,7,8,24],
                             [1,2,3,4,5,6,7,8,11,12,13,15,16,17,19,20,21,22,23,24],
                             [1,2,3,4,5,6,7,8,11,12,13,15,16,17,19,20,21,22,23,24],
                             [1,2,3,4,5,6,7,8,11,12,13,14,15,16,17,21,24],
                             [1,2,3,4,5,6,7,8,16,17,18,19,21,24],
                             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,21,23,24],
                             [1,2,3,4,5,6,7,8,14,16,17,18,21,23,24],
                             [1,2,3,4,5,6,7,8,10,11,14,16,17,18,21,23,24],
                             [1,2,7,8,10,11,14,16,17,18,19,21,23,24],
                             [1,2,7,8,10,11,12,13,14,16,17,18,19,21,23,24],
                             [1,2,7,8,10,11,12,13,14,24],
                             [1,2,16,17,18,19,20,21,22,23,24],
                             [1,2,16,22,24],
                             [1,2,7,8,9,10,12,14,16,18,22,24],
                             [1,2,7,8,9,10,12,14,16,18,22,24],
                             [1,2,7,8,12,14,16,18,19,20,21,22,24],
                             [1,2,3,4,5,6,7,8,12,14,16,24],
                             [1,2,3,4,5,6,7,8,9,10,11,12,14,16,18,20,21,22,24],
                             [1,2,3,4,5,6,7,8,18,20,21,22,24],
                             [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,20,22,24],
                             [1,2,3,4,5,6,7,8,16,18,20,22,24],
                             [1,2,3,4,5,6,7,8,10,11,13,14,16,18,20,22,24],
                             [1,2,3,4,5,6,7,8,10,14,16,18,20,22,24],
                             [1,2,3,4,5,6,7,8,10,14,18,24],
                             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]]     
        self.wallCoord_hard=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24],
                             [1,3,4,5,7,8,10,24],
                             [1,8,10,12,13,15,17,18,19,20,21,22,23,24],
                             [1,2,3,4,5,7,8,10,13,15,24],
                             [1,2,3,4,10,12,15,17,19,20,21,23,24],
                             [1,2,3,4,5,6,7,9,10,12,13,14,15,17,19,21,23,24],
                             [1,4,7,10,16,17,19,23,24],
                             [1,2,4,5,7,8,10,12,13,15,17,19,20,21,23,24],
                             [1,2,10,12,13,15,17,24],
                             [1,2,4,5,6,7,8,10,13,17,18,19,20,21,22,23,24],
                             [1,4,8,10,12,13,14,15,24],
                             [1,3,4,8,10,15,17,19,20,21,22,24],
                             [1,3,5,7,8,9,10,12,13,15,17,19,22,24],
                             [1,3,5,7,10,12,13,15,17,18,19,21,22,24],
                             [1,3,5,10,12,13,14,15,19,24],
                             [1,3,5,7,10,17,18,19,20,21,22,23,24],
                             [1,3,5,7,8,9,10,11,12,13,14,15,24],
                             [1,3,5,13,14,15,17,18,19,21,22,23,24],
                             [1,3,5,6,7,8,9,10,11,15,17,18,22,23,24],
                             [1,3,13,15,17,20,23,24],
                             [1,3,4,5,6,7,8,9,10,11,12,13,19,20,21,24],
                             [1,13,15,17,20,23,24],
                             [1,2,3,4,5,6,7,8,9,10,11,15,17,18,22,23,24],
                             [1,13,14,15,17,18,19,21,22,23,24],
                             [1,3,4,5,6,8,9,10,11,12,13,14,15,24],
                             [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]]
        
        self.end_easy=[14,14]
        self.doorCoord_easy=[[3,6],[24,6]]
        self.rockCoord_easy=[]
        
        self.end_medi=[14,3]
        self.doorCoord_medi=[[12,21],[14,18],[13,7],[14,7]]
        self.rockCoord_medi=[[5,20],[10,20],[13,9],[14,9],[22,15],[22,9],[18,19]]
        
        self.end_hard=[2,2]
        self.doorCoord_hard=[[17,17],[21,17],[25,17],[20,11],[18,11],[22,3]]
        self.rockCoord_hard=[[14,20],[24,10],[16,11],[4,19]]
                
        self.crownCoord_easy=[]
        self.goldCoord_easy=[]
        self.keyCoord_easy=[[5,20]]
        self.lanternCoord_easy=[]
        self.mudCoord_easy=[]
        self.paperCoord_easy=[[21,12],[6,12]]
        self.wandCoord_easy=[[14,19]]
        
        self.crownCoord_medi=[[17,9]]
        self.goldCoord_medi=[]
        self.keyCoord_medi=[[20,9]]
        self.lanternCoord_medi=[[4,14]]
        self.mudCoord_medi=[[7,16]]
        self.paperCoord_medi=[[13,14],[15,20],[8,13],[21,21]]
        self.wandCoord_medi=[[22,17]]
        
        self.crownCoord_hard=[[15,18],[5,13]]
        self.goldCoord_hard=[[8,16],[13,21],[21,23],[13,4],[11,6]]
        self.keyCoord_hard=[]
        self.lanternCoord_hard=[[4,23]]
        self.mudCoord_hard=[[14,14]]
        self.paperCoord_hard=[[21,14],[6,20],[13,18]]
        self.wandCoord_hard=[[4,12]]
        
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        

class Boundary:
    #setting of the map
    #position of the character
    #check if character on an item
    #checking for obstacle/boundary next to the character
    def __init__(self,x=42,y=720):
        self.x=float(x)
        self.y=float(y)
        self.pos=[float((self.x+14)/28),float((self.y+16)/32)]
        self.difficulty=diff
        self.mode=Mode()
        
        if self.difficulty=='Easy':
            self.wallCoord=self.mode.wallCoord_easy

            self.doorCoord=self.mode.doorCoord_easy
            self.rockCoord=self.mode.rockCoord_easy
        
            self.crownCoord=self.mode.crownCoord_easy
            self.goldCoord=self.mode.goldCoord_easy
            self.keyCoord=self.mode.keyCoord_easy
            self.lanternCoord=self.mode.lanternCoord_easy
            self.mudCoord=self.mode.mudCoord_easy
            self.paperCoord=self.mode.paperCoord_easy
            self.wandCoord=self.mode.wandCoord_easy
            self.end=self.mode.end_easy
            
        if self.difficulty=='Medium':
            self.wallCoord=self.mode.wallCoord_medi

            self.doorCoord=self.mode.doorCoord_medi
            self.rockCoord=self.mode.rockCoord_medi
        
            self.crownCoord=self.mode.crownCoord_medi
            self.goldCoord=self.mode.goldCoord_medi
            self.keyCoord=self.mode.keyCoord_medi
            self.lanternCoord=self.mode.lanternCoord_medi
            self.mudCoord=self.mode.mudCoord_medi
            self.paperCoord=self.mode.paperCoord_medi
            self.wandCoord=self.mode.wandCoord_medi
            self.end=self.mode.end_medi
            
        if self.difficulty=='Hard':
            self.wallCoord=self.mode.wallCoord_hard

            self.doorCoord=self.mode.doorCoord_hard
            self.rockCoord=self.mode.rockCoord_hard
        
            self.crownCoord=self.mode.crownCoord_hard
            self.goldCoord=self.mode.goldCoord_hard
            self.keyCoord=self.mode.keyCoord_hard
            self.lanternCoord=self.mode.lanternCoord_hard
            self.mudCoord=self.mode.mudCoord_hard
            self.paperCoord=self.mode.paperCoord_hard
            self.wandCoord=self.mode.wandCoord_hard
            self.end=self.mode.end_hard
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
        
        self.checkDoor1=False
        self.checkDoor2=False
        self.checkDoor3=False
        self.checkDoor4=False
        self.checkDoor5=False
        self.checkDoor6=False
        self.checkRock=False


        
    def checkXleft(self):
        if int(self.pos[1]) in self.wallCoord[int(self.pos[0]+0.75)-2] or int(self.pos[1]+0.75) in self.wallCoord[int(self.pos[0]+0.75)-2]:
            return False
        elif [self.pos[0]-1,self.pos[1]] in self.rockCoord and self.checkRock==False:
            return False
        else:
            return True
            
    def checkXright(self):
        if int(self.pos[1]) in self.wallCoord[int(self.pos[0])] or int(self.pos[1]+0.75) in self.wallCoord[int(self.pos[0])]:
            return False
        elif [self.pos[0]+1,self.pos[1]] in self.rockCoord and self.checkRock==False:
            return False
        else:
            return True
            
    def checkYup(self):
        if int(self.pos[1]-0.25) in self.wallCoord[int(self.pos[0])-1] or int(self.pos[1]-0.25) in self.wallCoord[int(self.pos[0]+0.75)-1]:
            return False
        elif [self.pos[0],self.pos[1]-1] in self.rockCoord and self.checkRock==False:
            return False
        elif [self.pos[0],self.pos[1]-1] in self.doorCoord:
            n=self.doorCoord.index([self.pos[0],self.pos[1]-1])
            if n==0:
                if self.checkDoor1==False:
                    return False
                else:
                    return True
            elif n==1:
                if self.checkDoor2==False:
                    return False
                else:
                    return True
            elif n==2:
                if self.checkDoor3==False:
                    return False
                else:
                    return True
            elif n==3:
                if self.checkDoor4==False:
                    return False
                else:
                    return True
            elif n==4:
                if self.checkDoor5==False:
                    return False
                else:
                    return True
            elif n==5:
                if self.checkDoor6==False:
                    return False
                else:
                    return True
        else:
            return True
            
    def checkYdown(self):
        if int(self.pos[1]+1) in self.wallCoord[int(self.pos[0])-1] or int(self.pos[1]+1) in self.wallCoord[int(self.pos[0]+0.75)-1]:
            return False
        elif [self.pos[0],self.pos[1]+1] in self.rockCoord and self.checkRock==False:
            return False
        elif [self.pos[0],self.pos[1]+1] in self.doorCoord:
            n=self.doorCoord.index([self.pos[0],self.pos[1]+1])
            if n==0:
                if self.checkDoor1==False:
                    return False
                else:
                    return True
            elif n==1:
                if self.checkDoor2==False:
                    return False
                else:
                    return True
            elif n==2:
                if self.checkDoor3==False:
                    return False
                else:
                    return True
            elif n==3:
                if self.checkDoor4==False:
                    return False
                else:
                    return True
            elif n==4:
                if self.checkDoor5==False:
                    return False
                else:
                    return True
            elif n==5:
                if self.checkDoor6==False:
                    return False
                else:
                    return True
        else:
            return True
            
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

    def checkCrown(self):
        if self.pos in self.crownCoord:
            return True
        else:
            return False
            
    def checkKey(self):
        if self.pos in self.keyCoord:
            return True
        else:
            return False
            
    def checkLantern(self):
        if self.pos in self.lanternCoord:
            return True
        else:
            return False
            
    def checkWand(self):
        if self.pos in self.wandCoord:
            return True
        else:
            return False
            
    def checkGold(self):
        if self.pos in self.goldCoord:
            return True
        else:
            return False
            
    def checkMud(self):
        if self.pos in self.mudCoord:
            return True
        else:
            return False
            
    def checkPaper(self):
        if self.pos in self.paperCoord:
            return True
        else:
            return False
                    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------          
class World:
    #main class
    #asigning of the placement of the widgets
    def __init__(self):
        self.window=Tk()
        self.window.title('1D Game')
        self.char=Character()
        self.check=Boundary()
        self.counter=StringVar()
        self.counter.set('0')  
        self.k=0
        self.fin=False                      
        
        self.map=Frame(self.window)
        self.hud=Frame(self.window)
        self.map.pack(side=LEFT)
        self.hud.pack(side=RIGHT)
        
        self.hud1=LabelFrame(self.hud, text="Inventory", bg="beige",width=100, height=100)
        self.hud2=Frame(self.hud)
        self.hud1.pack(side=TOP)
        self.hud2.pack(side=BOTTOM)
                
        self.canvas=Canvas(self.map,height=768,width=728,bg='white')
        self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.dwn1,tags='old')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
        #creation of the map
        self.canvas.create_image((self.check.end[0]*28)-14,(self.check.end[1]*32)-16,image=self.char.end)
        
        for n in range(26):
            self.mapX=n+1
            for self.mapY in self.check.wallCoord[n]:
                self.canvas.create_image((self.mapX*28)-14,(self.mapY*32)-16,image=self.char.wall1)
                
        for n in range(len(self.check.crownCoord)):
            self.canvas.create_image((self.check.crownCoord[n][0]*28)-14,(self.check.crownCoord[n][1]*32)-16,image=self.char.crown,tags='crown'+str(n))
            
        for n in range(len(self.check.keyCoord)):
            self.canvas.create_image((self.check.keyCoord[n][0]*28)-14,(self.check.keyCoord[n][1]*32)-16,image=self.char.key,tags='key'+str(n))
            
        for n in range(len(self.check.lanternCoord)):
            self.canvas.create_image((self.check.lanternCoord[n][0]*28)-14,(self.check.lanternCoord[n][1]*32)-16,image=self.char.lantern,tags='lantern'+str(n))
            
        for n in range(len(self.check.wandCoord)):
            self.canvas.create_image((self.check.wandCoord[n][0]*28)-14,(self.check.wandCoord[n][1]*32)-16,image=self.char.wand,tags='wand'+str(n))
            
        for n in range(len(self.check.goldCoord)):
            self.canvas.create_image((self.check.goldCoord[n][0]*28)-14,(self.check.goldCoord[n][1]*32)-16,image=self.char.gold,tags='gold'+str(n))
            
        for n in range(len(self.check.mudCoord)):
            self.canvas.create_image((self.check.mudCoord[n][0]*28)-14,(self.check.mudCoord[n][1]*32)-16,image=self.char.mud,tags='mud'+str(n))
            
        for n in range(len(self.check.wandCoord)):
            self.canvas.create_image((self.check.wandCoord[n][0]*28)-14,(self.check.wandCoord[n][1]*32)-16,image=self.char.wand,tags='wand'+str(n))
            
        for n in range(len(self.check.paperCoord)):
            self.canvas.create_image((self.check.paperCoord[n][0]*28)-14,(self.check.paperCoord[n][1]*32)-16,image=self.char.paper,tags='paper'+str(n))
            
        for n in range(len(self.check.rockCoord)):
            self.canvas.create_image((self.check.rockCoord[n][0]*28)-14,(self.check.rockCoord[n][1]*32)-16,image=self.char.rocks,tags='rock')
           
        for n in range(len(self.check.doorCoord)):
            if n==0:
                self.canvas.create_image((self.check.doorCoord[n][0]*28)-14,(self.check.doorCoord[n][1]*32)-16,image=self.char.door1,tags='door'+str(n))
            if n==1:
                self.canvas.create_image((self.check.doorCoord[n][0]*28)-14,(self.check.doorCoord[n][1]*32)-16,image=self.char.door2,tags='door'+str(n))
            if n==2:
                self.canvas.create_image((self.check.doorCoord[n][0]*28)-14,(self.check.doorCoord[n][1]*32)-16,image=self.char.door3,tags='door'+str(n))
            if n==3:
                self.canvas.create_image((self.check.doorCoord[n][0]*28)-14,(self.check.doorCoord[n][1]*32)-16,image=self.char.door4,tags='door'+str(n))
            if n==4:
                self.canvas.create_image((self.check.doorCoord[n][0]*28)-14,(self.check.doorCoord[n][1]*32)-16,image=self.char.door5,tags='door'+str(n))
            if n==5:
                self.canvas.create_image((self.check.doorCoord[n][0]*28)-14,(self.check.doorCoord[n][1]*32)-16,image=self.char.door6,tags='door'+str(n))
     
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        #creation of the textbox 
        self.textBox=Text(self.hud2,bg='grey')
        self.textBox.grid(row=2,column=1,columnspan=2)
        self.textBox.insert(END,'Welcome to The 1D Game!\n Objective: \n Find your way to the end! But the maze is littered with obstacles. Find a way \n around these obstacles, or remove them entirely by stringing pieces of code \n found by picking up items! Good Luck! \n Use Arrow Keys to navigate \n Press \'ENTER\' to interact with objects once you are on top of them \n Press \'CLEAR\' to begin')
        self.textBox.configure(state='disabled')
        
        buttonEnter=Button(self.hud2,text='Enter',command=self.CheckCode)
        buttonEnter.grid(row=3,column=2,sticky=W)
        
        buttonClear=Button(self.hud2,text='Clear',command=self.cleartext)
        buttonClear.grid(row=3,column=1,sticky=E)
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        #creation of button layout
        self.Wand = Label(self.hud1, image = self.char.wand)
        self.Wand.grid(row=11,column=0,padx=5,pady=5)

        
        self.Lantern = Label(self.hud1, image = self.char.lantern)
        self.Lantern.grid(row=9,column=0,padx=5,pady=5)

        
        self.Crown = Label(self.hud1, image = self.char.crown)
        self.Crown.grid(row=7,column=3,padx=5,pady=5)

        
        self.Key = Label(self.hud1, image = self.char.key)
        self.Key.grid(row=7,column=0,padx=5,pady=5)

            
        self.Mud = Label(self.hud1, image = self.char.mud)
        self.Mud.grid(row=9,column=3,padx=5,pady=5)

            
        self.Paper = Label(self.hud1, image = self.char.paper)
        self.Paper.grid(row=0,column=0, rowspan=3, padx=5,pady=5)

            
        self.Gold = Label(self.hud1, image = self.char.gold)
        self.Gold.grid(row=4,column=0, rowspan=2, padx=5,pady=5)

            
        self.Paper_code_1=Button(self.hud1,text="door",command=self.ColPaper1)
        self.Paper_code_1.grid(row=0,column=1,padx=5,pady=5)
        self.Paper_code_1.config(state="disabled")
        
        self.Paper_code_2=Button(self.hud1,text="door[1]",command=self.ColPaper2)
        self.Paper_code_2.grid(row=0,column=2,padx=5,pady=5)
        self.Paper_code_2.config(state="disabled")
            
        self.Paper_code_3=Button(self.hud1,text="door[2]",command=self.ColPaper3)
        self.Paper_code_3.grid(row=0,column=3,padx=5,pady=5)
        self.Paper_code_3.config(state="disabled")
            
        self.Paper_code_4=Button(self.hud1,text="door[3]",command=self.ColPaper4)
        self.Paper_code_4.grid(row=0,column=4,padx=5,pady=5)
        self.Paper_code_4.config(state="disabled")

        self.Paper_code_5=Button(self.hud1,text="door[4]",command=self.ColPaper5)
        self.Paper_code_5.grid(row=0,column=5,padx=5,pady=5)
        self.Paper_code_5.config(state="disabled")
            
        self.Paper_code_6=Button(self.hud1,text="door[5]",command=self.ColPaper6)
        self.Paper_code_6.grid(row=1,column=1,padx=5,pady=5)
        self.Paper_code_6.config(state="disabled")
            
        self.Paper_code_7=Button(self.hud1,text="door[6]",command=self.ColPaper7)
        self.Paper_code_7.grid(row=1,column=2,padx=5,pady=5)
        self.Paper_code_7.config(state="disabled")
            
        self.Paper_code_8=Button(self.hud1,text="n",command=self.ColPaper8)
        self.Paper_code_8.grid(row=1,column=3,padx=5,pady=5)
        self.Paper_code_8.config(state="disabled")
            
        self.Paper_code_9=Button(self.hud1,text="[1]",command=self.ColPaper9)
        self.Paper_code_9.grid(row=1,column=4,padx=5,pady=5)
        self.Paper_code_9.config(state="disabled")

        self.Paper_code_10=Button(self.hud1,text="[2]",command=self.ColPaper10)
        self.Paper_code_10.grid(row=1,column=5,padx=5,pady=5)
        self.Paper_code_10.config(state="disabled")

        self.Paper_code_11=Button(self.hud1,text="[3]",command=self.ColPaper11)
        self.Paper_code_11.grid(row=3,column=1,padx=5,pady=5)
        self.Paper_code_11.config(state="disabled")
            
        self.Paper_code_12=Button(self.hud1,text="[4]",command=self.ColPaper12)
        self.Paper_code_12.grid(row=3,column=2,padx=5,pady=5)
        self.Paper_code_12.config(state="disabled")
            
        self.Paper_code_13=Button(self.hud1,text="[5]",command=self.ColPaper13)
        self.Paper_code_13.grid(row=3,column=3,padx=5,pady=5)
        self.Paper_code_13.config(state="disabled")
            
        self.Paper_code_14=Button(self.hud1,text="[6]",command=self.ColPaper14)
        self.Paper_code_14.grid(row=3,column=4,padx=5,pady=5)
        self.Paper_code_14.config(state="disabled")

        self.Paper_code_15=Button(self.hud1,text="[n]",command=self.ColPaper15)
        self.Paper_code_15.grid(row=3,column=5,padx=5,pady=5)
        self.Paper_code_15.config(state="disabled")
            
        self.Gold_code_1=Button(self.hud1,text="range",command=self.ColGold1)
        self.Gold_code_1.grid(row=4,column=1,padx=5,pady=5)
        self.Gold_code_1.config(state="disabled")
            
        self.Gold_code_2=Button(self.hud1,text="(1,2)",command=self.ColGold2)
        self.Gold_code_2.grid(row=4,column=2,padx=5,pady=5)
        self.Gold_code_2.config(state="disabled")
            
        self.Gold_code_3=Button(self.hud1,text="(1,3)",command=self.ColGold3)
        self.Gold_code_3.grid(row=4,column=3,padx=5,pady=5)
        self.Gold_code_3.config(state="disabled")       
            
        self.Gold_code_4=Button(self.hud1,text="(1,4)",command=self.ColGold4)
        self.Gold_code_4.grid(row=4,column=4,padx=5,pady=5)
        self.Gold_code_4.config(state="disabled")          
        
        self.Gold_code_5=Button(self.hud1,text="(1,5)",command=self.ColGold5)
        self.Gold_code_5.grid(row=5,column=1,padx=5,pady=5)
        self.Gold_code_5.config(state="disabled")           
        
        self.Gold_code_6=Button(self.hud1,text="(1,6)",command=self.ColGold6)
        self.Gold_code_6.grid(row=5,column=2,padx=5,pady=5)
        self.Gold_code_6.config(state="disabled")        
        
        self.Gold_code_7=Button(self.hud1,text="(1,7)",command=self.ColGold7)
        self.Gold_code_7.grid(row=5,column=3,padx=5,pady=5)
        self.Gold_code_7.config(state="disabled")
       
        self.Key_code_1=Button(self.hud1,text="'OPEN'",command=self.ColKey1)
        self.Key_code_1.grid(row=7,column=1,padx=5,pady=5)
        self.Key_code_1.config(state="disabled")
        
        self.Key_code_2=Button(self.hud1,text="'CLOSED'",command=self.ColKey2)
        self.Key_code_2.grid(row=7,column=2,padx=5,pady=5)
        self.Key_code_2.config(state="disabled")
        
        self.Crown_code_1=Button(self.hud1,text="'BREAK'",command=self.ColCrown1)
        self.Crown_code_1.grid(row=7,column=4,padx=5,pady=5)
        self.Crown_code_1.config(state="disabled")
        
        self.Crown_code_2=Button(self.hud1,text="for",command=self.ColCrown2)
        self.Crown_code_2.grid(row=7,column=5,padx=5,pady=5)
        self.Crown_code_2.config(state="disabled")   
       
        self.Lantern_code_1=Button(self.hud1,text="rocks",command=self.ColLantern1)
        self.Lantern_code_1.grid(row=9,column=1,padx=5,pady=5)
        self.Lantern_code_1.config(state="disabled")   
        
        self.Mud_code_1=Button(self.hud1,text="in",command=self.ColMud1)
        self.Mud_code_1.grid(row=9,column=4,padx=5,pady=5)
        self.Mud_code_1.config(state="disabled")                    
       
        self.Wand_code_1=Button(self.hud1,text="'OPEN'",command=self.ColWand1)
        self.Wand_code_1.grid(row=11,column=1,padx=5,pady=5)
        self.Wand_code_1.config(state="disabled")             
        
        self.operator1=Button(self.hud1,text="=",command=self.standard1)
        self.operator1.grid(row=11,column=4,padx=5,pady=5)
        self.operator1.config(state="normal") 
            
        self.operator2=Button(self.hud1,text="==",command=self.standard2)
        self.operator2.grid(row=11,column=5,padx=5,pady=5)
        self.operator2.config(state="normal")
            
        self.operator3=Button(self.hud1,text=":",command=self.standard3)
        self.operator3.grid(row=11,column=6,padx=5,pady=5)
        self.operator3.config(state="normal")  
            
        self.hud1.focus_set()
        
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
        #binding of controls
        self.window.bind('<KeyPress-Up>',self.up)
        self.window.bind('<KeyPress-Down>',self.down)
        self.window.bind('<KeyPress-Left>',self.left)
        self.window.bind('<KeyPress-Right>',self.right)
        
        self.window.bind('<KeyPress-Return>',self.action)
        self.window.bind('<KeyPress-Escape>',self.back)
        
        self.canvas.pack()
        self.window.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       
    #control functions
    def up(self,event):
        if self.check.checkYup()==True:
            self.check.y+=-8
            self.check.pos=[float((self.check.x+14)/28),float((self.check.y+16)/32)]
            self.fin=False
            if self.counter.get()=='0' or self.counter.get()=='1':
                self.canvas.delete('old')
                self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.up1,tags='old')
                self.counter.set(str(int(self.counter.get())+1))
            elif self.counter.get()=='2' or self.counter.get()=='3':
                self.canvas.delete('old')
                self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.up2,tags='old')
                self.counter.set(str(int(self.counter.get())+1))
            elif self.counter.get()=='4' or self.counter.get()=='5':
                self.canvas.delete('old')
                self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.up3,tags='old')
                if self.counter.get()=='4':
                    self.counter.set(str(int(self.counter.get())+1))
                else:
                    self.counter.set('0')
        elif self.check.pos==self.check.end:
            self.fin=True
        print (self.check.pos,self.fin)
        
    def down(self,event):
        if self.check.checkYdown()==True:
            self.check.y+=8
            self.check.pos=[float((self.check.x+14)/28),float((self.check.y+16)/32)]
            self.fin=False
            if self.counter.get()=='0' or self.counter.get()=='1':
                self.canvas.delete('old')
                self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.dwn1,tags='old')
                self.counter.set(str(int(self.counter.get())+1))
            elif self.counter.get()=='2' or self.counter.get()=='3':
                self.canvas.delete('old')
                self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.dwn2,tags='old')
                self.counter.set(str(int(self.counter.get())+1))
            elif self.counter.get()=='4' or self.counter.get()=='5':
                self.canvas.delete('old')
                self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.dwn3,tags='old')
                if self.counter.get()=='4':
                    self.counter.set(str(int(self.counter.get())+1))
                else:
                    self.counter.set('0')
        elif self.check.pos==self.check.end:
                self.fin=True
        print (self.check.pos,self.fin)
                           
    def left(self,event):
        if self.check.checkXleft()==True:
            self.check.x+=-7
            self.check.pos=[float((self.check.x+14)/28),float((self.check.y+16)/32)]
            self.fin=False
            if self.counter.get()=='0' or self.counter.get()=='1':
                self.canvas.delete('old')
                self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.l1,tags='old')
                self.counter.set(str(int(self.counter.get())+1))
            elif self.counter.get()=='2' or self.counter.get()=='3':
                self.canvas.delete('old')
                self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.l2,tags='old')
                self.counter.set(str(int(self.counter.get())+1))
            elif self.counter.get()=='4' or self.counter.get()=='5':
                self.canvas.delete('old')
                self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.l3,tags='old')
                if self.counter.get()=='4':
                    self.counter.set(str(int(self.counter.get())+1))
                else:
                    self.counter.set('0')
        elif self.check.pos==self.check.end:
                self.fin=True
        print (self.check.pos,self.fin)
                         
    def right(self,event):
        if self.check.checkXright()==True:
            self.check.x+=7
            self.check.pos=[float((self.check.x+14)/28),float((self.check.y+16)/32)]
            self.fin=False
            if self.counter.get()=='0' or self.counter.get()=='1':
                self.canvas.delete('old')
                self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.r1,tags='old')
                self.counter.set(str(int(self.counter.get())+1))
            elif self.counter.get()=='2' or self.counter.get()=='3':
                self.canvas.delete('old')
                self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.r2,tags='old')
                self.counter.set(str(int(self.counter.get())+1))
            elif self.counter.get()=='4' or self.counter.get()=='5':
                self.canvas.delete('old')
                self.current=self.canvas.create_image(self.check.x,self.check.y,image=self.char.r3,tags='old')
                if self.counter.get()=='4':
                    self.counter.set(str(int(self.counter.get())+1))
                else:
                    self.counter.set('0')
        elif self.check.pos==self.check.end:
                self.fin=True
        print (self.check.pos,self.fin)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
    #execution of command when button is pressed
    def ColWand1(self):
        self.textBox.configure(state='normal')
        code="'OPEN'"
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
        
        
    def ColKey1(self):
        self.textBox.configure(state='normal')
        code="'OPEN'"
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColKey2(self):
        self.textBox.configure(state='normal')
        code="'CLOSED'"
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
        
    
    def ColLantern1(self):
        self.textBox.configure(state='normal')
        code='rocks'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
        
        
    def ColMud1(self):
        self.textBox.configure(state='normal')
        code='in '
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
        
        
    def ColPaper1(self):
        self.textBox.configure(state='normal')
        code='door'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper2(self):
        self.textBox.configure(state='normal')
        code='door[1]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper3(self):
        self.textBox.configure(state='normal')
        code='door[2]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper4(self):
        self.textBox.configure(state='normal')
        code='door[3]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper5(self):
        self.textBox.configure(state='normal')
        code='door[4]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper6(self):
        self.textBox.configure(state='normal')
        code='door[5]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper7(self):
        self.textBox.configure(state='normal')
        code='door[6]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper8(self):
        self.textBox.configure(state='normal')
        code='n '
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper9(self):
        self.textBox.configure(state='normal')
        code='[1]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper10(self):
        self.textBox.configure(state='normal')
        code='[2]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper11(self):
        self.textBox.configure(state='normal')
        code='[3]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper12(self):
        self.textBox.configure(state='normal')
        code='[4]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper13(self):
        self.textBox.configure(state='normal')
        code='[5]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper14(self):
        self.textBox.configure(state='normal')
        code='[6]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColPaper15(self):
        self.textBox.configure(state='normal')
        code='[n]'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
        
    
    def ColGold1(self):
        self.textBox.configure(state='normal')
        code='range'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColGold2(self):
        self.textBox.configure(state='normal')
        code='(1,2)'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColGold3(self):
        self.textBox.configure(state='normal')
        code='(1,3)'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled') 
    def ColGold4(self):
        self.textBox.configure(state='normal')
        code='(1,4)'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled') 
    def ColGold5(self):
        self.textBox.configure(state='normal')
        code='(1,5)'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColGold6(self):
        self.textBox.configure(state='normal')
        code='(1,6)'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled') 
    def ColGold7(self):
        self.textBox.configure(state='normal')
        code='(1,7)'
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')  
        
    
    def ColCrown1(self):
        self.textBox.configure(state='normal')
        code="'BREAK'"
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
    def ColCrown2(self):
        self.textBox.configure(state='normal')
        code='for '
        self.textBox.insert(END,code)
        self.textBox.configure(state='disabled')
             
        
    def standard1(self):
        self.textBox.configure(state='normal')
        self.textBox.insert(END,'=')
        self.textBox.configure(state='disabled')
    def standard2(self):
        self.textBox.configure(state='normal')
        self.textBox.insert(END,'==')
        self.textBox.configure(state='disabled')
    def standard3(self):
        self.textBox.configure(state='normal')
        self.textBox.insert(END,':')
        self.textBox.configure(state='disabled')
        
    def cleartext(self):
        self.textBox.configure(state='normal')
        self.textBox.delete('1.0',END)
        self.textBox.configure(state='disabled')
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    def back(self,event):
        self.window.destroy()
        Game()
    
    #interaction function. Differs for different difficulties since items vary
    def action(self,event):
        if self.check.difficulty=='Easy':
            if self.fin==True:
                self.canvas.delete('old')
                self.canvas.create_image((self.check.end[0]*28)-14,(self.check.end[1]*32)-16,image=self.char.dwn22,tags='old')
                self.canvas.create_image(384,364,image=self.char.fin)
                
            elif self.check.checkCrown()==True:
                n=self.check.crownCoord.index(self.check.pos)
                self.canvas.delete('crown'+str(n))
                self.canvas.create_image(384,364,image=self.char.crown1,tags='old')
                self.check.checkCrown()==False
            
            elif self.check.checkKey()==True:
                n=self.check.keyCoord.index(self.check.pos)
                self.canvas.delete('key'+str(n))
                self.canvas.create_image(384,364,image=self.char.key2,tags='old')
                self.check.checkKey()==False
            
            elif self.check.checkLantern()==True:
                n=self.check.lanternCoord.index(self.check.pos)
                self.canvas.delete('lantern'+str(n))
                self.canvas.create_image(384,364,image=self.char.lantern1,tags='old')
                self.check.checkLantern()==False
            
            elif self.check.checkWand()==True:
                n=self.check.wandCoord.index(self.check.pos)
                self.canvas.delete('wand'+str(n))
                self.canvas.create_image(384,364,image=self.char.wand1,tags='old')
                self.check.checkWand()==False
                self.Wand_code_1.config(state="normal")
                 
            elif self.check.checkGold()==True:
                n=self.check.goldCoord.index(self.check.pos)
                self.canvas.delete('gold'+str(n))
                self.canvas.create_image(384,364,image=self.char.gold1,tags='old')
                self.check.checkGold()==False
            
            elif self.check.checkMud()==True:
                n=self.check.mudCoord.index(self.check.pos)
                self.canvas.delete('mud'+str(n))
                self.canvas.create_image(384,364,image=self.char.mud1,tags='old')
                self.check.checkMud()==False
            
            elif self.check.checkPaper()==True:
                n=self.check.paperCoord.index(self.check.pos)
                if n==0:
                    self.canvas.delete('paper'+str(n))
                    self.canvas.create_image(384,364,image=self.char.paper2,tags='old')
                    self.check.checkPaper()==False
                    self.Paper_code_2.config(state="normal")
                elif n==1:
                    self.canvas.delete('paper'+str(n))
                    self.canvas.create_image(384,364,image=self.char.paper3,tags='old')
                    self.check.checkPaper()==False
                    self.Paper_code_3.config(state="normal")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                    
        if self.check.difficulty=='Medium':
            if self.fin==True:
                self.canvas.delete('old')
                self.canvas.create_image((self.check.end[0]*28)-14,(self.check.end[1]*32)-16,image=self.char.dwn22,tags='old')
                self.canvas.create_image(384,364,image=self.char.fin)
                
            elif self.check.checkCrown()==True:
                n=self.check.crownCoord.index(self.check.pos)
                self.canvas.delete('crown'+str(n))
                self.canvas.create_image(384,364,image=self.char.crown1,tags='old')
                self.Crown_code_1.config(state="normal")
                self.check.checkCrown()==False
            
            elif self.check.checkKey()==True:
                n=self.check.keyCoord.index(self.check.pos)
                self.canvas.delete('key'+str(n))
                self.canvas.create_image(384,364,image=self.char.key1,tags='old')
                self.Key_code_1.config(state="normal")
                self.Key_code_2.config(state="normal")
                self.check.checkKey()==False
            
            elif self.check.checkLantern()==True:
                n=self.check.lanternCoord.index(self.check.pos)
                self.canvas.delete('lantern'+str(n))
                self.canvas.create_image(384,364,image=self.char.lantern1,tags='old')
                self.Lantern_code_1.config(state="normal")
                self.check.checkLantern()==False
            
            elif self.check.checkWand()==True:
                n=self.check.wandCoord.index(self.check.pos)
                self.canvas.delete('wand'+str(n))
                self.canvas.create_image(384,364,image=self.char.wand2,tags='old')
                self.check.checkWand()==False
                 
            elif self.check.checkGold()==True:
                n=self.check.goldCoord.index(self.check.pos)
                self.canvas.delete('gold'+str(n))
                self.canvas.create_image(384,364,image=self.char.gold1,tags='old')
                self.check.checkGold()==False
            
            elif self.check.checkMud()==True:
                n=self.check.mudCoord.index(self.check.pos)
                self.canvas.delete('mud'+str(n))
                self.canvas.create_image(384,364,image=self.char.mud2,tags='old')
                self.check.checkMud()==False
            
            elif self.check.checkPaper()==True:
                n=self.check.paperCoord.index(self.check.pos)
                if n==0:
                    self.canvas.delete('paper'+str(n))
                    self.canvas.create_image(384,364,image=self.char.paper1,tags='old')
                    self.check.checkPaper()==False
                    self.Paper_code_1.config(state="normal")
                elif n==1:
                    self.canvas.delete('paper'+str(n))
                    self.canvas.create_image(384,364,image=self.char.paper12,tags='old')
                    self.check.checkPaper()==False
                    self.Paper_code_12.config(state="normal")
                elif n==2:
                    self.canvas.delete('paper'+str(n))
                    self.canvas.create_image(384,364,image=self.char.paper9,tags='old')
                    self.check.checkPaper()==False
                    self.Paper_code_9.config(state="normal")
                elif n==3:
                    self.canvas.delete('paper'+str(n))
                    self.canvas.create_image(384,364,image=self.char.paper10,tags='old')
                    self.check.checkPaper()==False
                    self.Paper_code_10.config(state="normal")
                    
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                    

        if self.check.difficulty=='Hard':
            if self.fin==True:
                self.canvas.delete('old')
                self.canvas.create_image((self.check.end[0]*28)-14,(self.check.end[1]*32)-16,image=self.char.dwn22,tags='old')
                self.canvas.create_image(384,364,image=self.char.fin)
                
            elif self.check.checkCrown()==True:
                n=self.check.crownCoord.index(self.check.pos)
                if n==0:
                    self.canvas.delete('crown'+str(n))
                    self.canvas.create_image(384,364,image=self.char.crown1,tags='old')
                    self.Crown_code_1.config(state="normal")
                    self.check.checkCrown()==False
                elif n==1:
                    self.canvas.delete('crown'+str(n))
                    self.canvas.create_image(384,364,image=self.char.crown2,tags='old')
                    self.Crown_code_2.config(state="normal")
                    self.check.checkCrown()==False
            
            elif self.check.checkKey()==True:
                n=self.check.keyCoord.index(self.check.pos)
                self.canvas.delete('key'+str(n))
                self.canvas.create_image(384,364,image=self.char.key1,tags='old')
                self.check.checkKey()==False
            
            elif self.check.checkLantern()==True:
                n=self.check.lanternCoord.index(self.check.pos)
                self.canvas.delete('lantern'+str(n))
                self.canvas.create_image(384,364,image=self.char.lantern1,tags='old')
                self.Lantern_code_1.config(state="normal")
                self.check.checkLantern()==False
            
            elif self.check.checkWand()==True:
                n=self.check.wandCoord.index(self.check.pos)
                self.canvas.delete('wand'+str(n))
                self.canvas.create_image(384,364,image=self.char.wand1,tags='old')
                self.check.checkWand()==False
                self.Wand_code_1.config(state="normal")
                 
            elif self.check.checkGold()==True:
                n=self.check.goldCoord.index(self.check.pos)
                if n==0:
                    self.canvas.delete('gold'+str(n))
                    self.canvas.create_image(384,364,image=self.char.gold1,tags='old')
                    self.Gold_code_1.config(state='normal')
                    self.check.checkGold()==False
                elif n==1:
                    self.canvas.delete('gold'+str(n))
                    self.canvas.create_image(384,364,image=self.char.gold4,tags='old')
                    self.Gold_code_4.config(state='normal')
                    self.check.checkGold()==False
                elif n==2:
                    self.canvas.delete('gold'+str(n))
                    self.canvas.create_image(384,364,image=self.char.gold5,tags='old')
                    self.Gold_code_5.config(state='normal')
                    self.check.checkGold()==False
                elif n==3:
                    self.canvas.delete('gold'+str(n))
                    self.canvas.create_image(384,364,image=self.char.gold6,tags='old')
                    self.Gold_code_6.config(state='normal')
                    self.check.checkGold()==False
                elif n==4:
                    self.canvas.delete('gold'+str(n))
                    self.canvas.create_image(384,364,image=self.char.gold7,tags='old')
                    self.Gold_code_7.config(state='normal')
                    self.check.checkGold()==False
            
            elif self.check.checkMud()==True:
                n=self.check.mudCoord.index(self.check.pos)
                self.canvas.delete('mud'+str(n))
                self.canvas.create_image(384,364,image=self.char.mud1,tags='old')
                self.Mud_code_1.config(state='normal')
                self.check.checkMud()==False
            
            elif self.check.checkPaper()==True:
                n=self.check.paperCoord.index(self.check.pos)
                if n==0:
                    self.canvas.delete('paper'+str(n))
                    self.canvas.create_image(384,364,image=self.char.paper1,tags='old')
                    self.check.checkPaper()==False
                    self.Paper_code_1.config(state="normal")
                if n==1:
                    self.canvas.delete('paper'+str(n))
                    self.canvas.create_image(384,364,image=self.char.paper15,tags='old')
                    self.check.checkPaper()==False
                    self.Paper_code_15.config(state="normal")
                if n==2:
                    self.canvas.delete('paper'+str(n))
                    self.canvas.create_image(384,364,image=self.char.paper8,tags='old')
                    self.check.checkPaper()==False
                    self.Paper_code_8.config(state="normal")
               
    
    #code checker to see if input code is the correct answer of not
    def CheckCode(self):
        codes=self.textBox.get('1.0',END).splitlines()
        self.textBox.configure(state='normal')
        
        if self.check.difficulty=='Easy':
            if codes==[u"door[1]='OPEN'"]:
                answer='\n'+'You are correct! The first door is now open :)'
                self.check.checkDoor1=True
            elif codes==[u"door[2]='OPEN'"]:
                answer='\n'+'You are correct! The second door is now open :)'
                self.check.checkDoor2=True
            elif codes==[u"rocks='BREAK'"]:
                answer='\n'+'ALL THE ROCKS ARE BROKEN!'
            else: 
                answer='\n'+'Press [clear] and try again.'
        
        if self.check.difficulty=='Medium':
            if codes==[u"rocks='BREAK'"]:
                answer='\n'+'ALL THE ROCKS ARE BROKEN!'
                self.check.checkRock=True
                self.canvas.delete('rock')
            elif codes==[u"door[1]='OPEN'"]:
                answer='\n'+'You are correct! The first door is now open :)'
                self.check.checkDoor1=True
            elif codes==[u"door[2]='OPEN'"]:
                answer='\n'+'You are correct! The second door is now open :)'
                self.check.checkDoor2=True
            elif codes==[u"door[3]='OPEN'"]:
                answer='\n'+'You are correct! The third door is now open :)'
                self.check.checkDoor3=True
            elif codes==[u"door[4]='OPEN'"]:
                answer='\n'+'You are correct! The fourth door is now open :)'
                self.check.checkDoor4=True
            else: 
                answer='\n'+'Press [clear] and try again.'
                
        if self.check.difficulty=='Hard':
            if codes==[u"rocks='BREAK'"]:
                answer='\n'+'ALL THE ROCKS ARE BROKEN!'
                self.check.checkRock=True
                self.canvas.delete('rock')
            elif codes==[u"for n in range(1,4):door[n]='OPEN'"]:
                answer='\n'+'You are correct! The first, second and third doors are now open :)'
                self.check.checkDoor1=True
                self.check.checkDoor2=True
                self.check.checkDoor3=True
            elif codes==[u"for n in range(1,5):door[n]='OPEN'"]:
                answer='\n'+'You are correct! The first, second, third and fourth doors are now open :)'
                self.check.checkDoor1=True
                self.check.checkDoor2=True
                self.check.checkDoor3=True
                self.check.checkDoor4=True
            elif codes==[u"for n in range(1,6):door[n]='OPEN'"]:
                answer='\n'+'You are correct! The first to fifth doors are now open :)'
                self.check.checkDoor1=True
                self.check.checkDoor2=True
                self.check.checkDoor3=True
                self.check.checkDoor4=True
                self.check.checkDoor5=True
            elif codes==[u"for n in range(1,7):door[n]='OPEN'"]:
                answer='\n'+'You are correct! The first to sixth doors are now open :)'
                self.check.checkDoor1=True
                self.check.checkDoor2=True
                self.check.checkDoor3=True
                self.check.checkDoor4=True
                self.check.checkDoor5=True
                self.check.checkDoor6=True
            else: 
                answer='\n'+'Press [clear] and try again.'
            
        self.textBox.insert(END,answer)
        self.textBox.configure(state='disabled')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

class Game:
    #start screen and choosing difficulty
    def __init__(self):
        
        
        self.window=Tk()
        self.window.title('1D Game')  
        self.window.geometry('400x400')
        self.background=PhotoImage(file='Start Screen.gif')
        background_label=Label(self.window,image=self.background)   
        background_label.place(x=0,y=0,relwidth=1,relheight=1)
              
        self.easy=Button(self.window,text="Easy",command=self.start_easy,width=12,height=5)
        self.easy.grid(row=1,column=1,padx=20,pady=270)
        
        self.medi=Button(self.window,text="Intermediate",command=self.start_medi,width=12,height=5)
        self.medi.grid(row=1,column=2,padx=20,pady=270)
        
        self.hard=Button(self.window,text="Hard",command=self.start_hard,width=12,height=5)
        self.hard.grid(row=1,column=3,padx=20,pady=270)
        
        self.window.mainloop()
        
    def start_easy(self):
        self.window.destroy()
        global diff
        diff='Easy'
        World()
            
    def start_medi(self):
        self.window.destroy()
        global diff
        diff='Medium'
        World()
            
    def start_hard(self):
        self.window.destroy()
        global diff
        diff='Hard'
        World()
        
                                       
Game()