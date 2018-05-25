from tkinter import *
from threading import *
import sqlite3 


#SQLITEBASE
db = sqlite3.connect('IPL.db')
cursor = db.cursor()
create_table = "CREATE TABLE PLAYER (ID INT PRIMARY KEY NOT NULL,FNAME TEXT NOT NULL, LNAME TEXT NOT NULL, CATEGORY TEXT NOT NULL, BASEVALUE INT NOT NULL, TEAM CHAR(50), SOLDVALUE INT);"        
cursor.execute(create_table)
db.commit()

#Insert values
fh = open("IPLPLAYERS.txt","r")
for line in fh:
    cursor.execute(line)
    db.commit()


#mainwindow
class main_window:
    def __init__(self, master):
        self.master = master
        self.master.title("IPL AUCTION")
        
        self.f = Frame(self.master, height = 400, width = 400)
        self.f.propagate(0)
        self.f.pack()
        
        self.viewteam = Button(self.f, text = 'View Teams', width = 25, command = self.view_teams)
        self.viewteam.place(x=100,y=250)

        self.exit = Button(self.f, text = 'Exit', width = 25, command = self.exit_window)
        self.exit.place(x=100,y=300)


        self.auction = Button(self.f, text = 'Auction', width = 25, command = self.auction_window)        
        self.auction.place(x=100,y=200)

        logo = PhotoImage(file = r"teams/iconIpl.png")
        self.pic = Label(self.master,image = logo)
        self.pic.image = logo
        self.pic.place(x = 115, y= 20) 

     
    def exit_window(self):
        self.master.destroy()

    def view_teams(self):
        self.view_teams = Toplevel(self.master)
        self.app = viewteams(self.view_teams)

    def auction_window(self):
        self.auction_window = Toplevel(self.master)
        self.auc = auctionwindow(self.auction_window)    


#Viewteamwindow    
class viewteams:
    def __init__(self, master):
        self.master = master
        self.master.title("IPL AUCTION: TEAMS")
        self.f = Frame(self.master,height = 600, width = 1200)
        self.f.propagate(0)
        self.f.pack()

        self.CSK = Button(self.f, text = 'Chennai Super Kings', width = 20,command = lambda: self.show_team(1))
        self.CSK.place(x=50,y=50)

        self.RCB = Button(self.f, text = 'Royal Challengers', width = 20,command = lambda: self.show_team(2))
        self.RCB.place(x=50,y=100)

        self.MI = Button(self.f, text = 'Mumbai Indians', width = 20,command = lambda: self.show_team(3))
        self.MI.place(x=50,y=150)

        self.RR = Button(self.f, text = 'Rajasthan Royals', width = 20,command = lambda: self.show_team(4))
        self.RR.place(x=50,y=200)

        self.KKR = Button(self.f, text = 'Kolkata Knight Riders', width = 20,command = lambda: self.show_team(5))
        self.KKR.place(x=50,y=250)

        self.SH = Button(self.f, text = 'Sunrisers Hyderabad', width = 20,command = lambda: self.show_team(6))
        self.SH.place(x=50,y=300)
        
        self.GL = Button(self.f, text = 'Gujrat Lions', width = 20,command = lambda: self.show_team(7))
        self.GL.place(x=50,y=350)

        self.KT = Button(self.f, text = 'Kochi Tuskers', width = 20,command = lambda: self.show_team(8))
        self.KT.place(x=50,y=400)

        self.exit = Button(self.f, text = 'EXIT', width = 20, command = self.exit_window)
        self.exit.place(x=50,y=500)


    def show_team(self,i):
       
        if i == 1:
            self.name='Chennai Super Kings'
            imgg = PhotoImage(file = r"teams/csk.png")
        elif i == 2:
            self.name='Royal Challengers'
            imgg = PhotoImage(file = r"teams/rcb.png")
        elif i == 3:
            self.name='Mumbai Indians'
            imgg = PhotoImage(file = r"teams/mi.png")
        elif i == 4:
            self.name='Rajasthan Royals'
            imgg = PhotoImage(file = r"teams/rr.png")
        elif i == 5:
            self.name='Kolkata Knight Riders'
            imgg = PhotoImage(file = r"teams/kkr.png")
        elif i == 6:
            self.name='Sunrisers Hyderabad'
            imgg = PhotoImage(file = r"teams/sh.png")
        elif i == 7:
            self.name='Gujrat Lions'
            imgg = PhotoImage(file = r"teams/gl.png")
        elif i == 8:
            self.name='Kochi Tuskers'
            imgg = PhotoImage(file = r"teams/kt.png")
        

        self.l2=Label(self.master,text="FIRST NAME",width=30)
        self.l2.place(x=220,y=30)
        self.l3=Label(self.master,text="LAST NAME",width=30)
        self.l3.place(x=250*2-40,y=30)
        
        for a in range(1,20):
                for b in range(1,20):
                        self.l5=Label(self.master,text="\t\t\t\t\t\t\t\t\t\t",width=400)
                        self.l5.place(x=250*b,y=50*a)
        cursor.execute("select FNAME,LNAME from PLAYER where TEAM like '{}'".format(self.name))
        r=cursor.fetchall()
        for a in range(0,len(r)):
            for b in range(0,2):
                self.l1=Label(self.master,text=r[a][b],width=20)
                self.l1.place(x=250*(b+1),y=50*(a+1))
        self.splash = Label(self.master,image = imgg)
        self.splash.image = imgg
        self.splash.place(x = 725, y= 150) 

    def exit_window(self):
        self.master.destroy()


#Auction window
class auctionwindow:
    
    def __init__(self, master): 
        self.play = 1 
        self.master = master
        self.master.title("IPL AUCTION: AUCTION")
        self.f = Frame(self.master, height = 800, width = 1500)
        self.f.propagate(0)
        self.f.pack()

        self.l1 = Label(self.master, text = "Chennai Super Kings",font = (24))
        self.l1.place(x=100, y=100)        
        self.b1 = Button(self.f, text = 'BID',font = (24),activebackground= 'purple', command = lambda: self.bidding(1))
        self.b1.place(x=300,y=100)
       
        self.l2 = Label(self.master, text = "Royal Challengers",font = (24))
        self.l2.place(x=100, y=200)
        self.b2 = Button(self.f, text = 'BID',font = (24),activebackground= 'purple', command = lambda: self.bidding(2))
        self.b2.place(x=300,y=200)

        self.l3 = Label(self.master, text = "Mumbai Indians",font = (24))
        self.l3.place(x=100, y=300)
        self.b3 = Button(self.f, text = 'BID',font = (24), activebackground= 'purple',command = lambda: self.bidding(3))
        self.b3.place(x=300,y=300)

        self.l4 = Label(self.master, text = "Rajasthan Royals",font = (24))
        self.l4.place(x=100, y=400)
        self.b4 = Button(self.f, text = 'BID',font = (24),activebackground= 'purple', command = lambda: self.bidding(4))
        self.b4.place(x=300,y=400)

        self.l5 = Label(self.master, text = "Kolkata Knight Riders",font = (24))
        self.l5.place(x=1200, y=100)
        self.b5 = Button(self.f, text = 'BID',font = (24),activebackground= 'purple',command = lambda: self.bidding(5))
        self.b5.place(x=1100,y=100)

        self.l6 = Label(self.master, text = "Sunrisers Hyderbad",font = (24))
        self.l6.place(x=1200, y=200)
        self.b6 = Button(self.f, text = 'BID',font = (24), activebackground= 'purple',command = lambda: self.bidding(6))
        self.b6.place(x=1100,y=200)

        self.l7 = Label(self.master, text = "Gujrat Lions",font = (24))
        self.l7.place(x=1200, y=300)
        self.b7 = Button(self.f, text = 'BID',font = (24),activebackground= 'purple',command = lambda: self.bidding(7))
        self.b7.place(x=1100,y=300)

        self.l8 = Label(self.master, text = "Kochi Tuskers",font = (24))
        self.l8.place(x=1200, y=400)
        self.b8 = Button(self.f, text = 'BID',font = (24),activebackground= 'purple',command = lambda: self.bidding(8))
        self.b8.place(x=1100,y=400)
        
        self.main_l = Label(self.master, text = 'AUCTION')
        self.main_l.config(font=("Courier", 44))
        self.main_l.place(x=620, y=25)
        
        #Bidder
        self.currbid = Label(self.master, text = 'Current Bidder :',font = (24))
        self.currbid.place(x=525, y=100)
        
        #Playername
        self.name = Label(self.master, text = 'Player Name :',font = (24))
        self.name.place(x=525, y=150)
        
        #Category                
        self.cat = Label(self.master, text = 'Category :',font = (24))
        self.cat.place(x=525, y=200) 
       
        #basevalue 
        self.bval = Label(self.master, text = 'Base value :',font = (24))
        self.bval.place(x=525, y=250)  
        
        #exit
        self.exit = Button(self.f, text = 'EXIT', width = 25,activebackground= 'red',command = self.exit_window)
        self.exit.place(x=525,y=700)
        
        #start
        self.start = Button(self.f, text = 'Start', width = 25,activebackground= 'red',command = self.start_auc)
        self.start.place(x=800,y=700)

        #team icons
        img = PhotoImage(file = r"teams/csk_icon.png")
        self.kings = Label(self.master,image = img)
        self.kings.image = img
        self.kings.place(x = 10, y= 75)  

        img = PhotoImage(file = r"teams/kkr_icon.png")
        self.riders = Label(self.master,image = img)
        self.riders.image = img
        self.riders.place(x = 1400, y= 75)  

        img = PhotoImage(file = r"teams/rcb_icon.png")
        self.challengers = Label(self.master,image = img)
        self.challengers.image = img
        self.challengers.place(x = 10, y= 175)  

        img = PhotoImage(file = r"teams/sh_icon.png")
        self.sunrisers = Label(self.master,image = img)
        self.sunrisers.image = img
        self.sunrisers.place(x = 1400, y= 175)  

        img = PhotoImage(file = r"teams/mi_icon.png")
        self.indians = Label(self.master,image = img)
        self.indians.image = img
        self.indians.place(x = 10, y= 275)  

        img = PhotoImage(file = r"teams/gl_icon.png")
        self.lions = Label(self.master,image = img)
        self.lions.image = img
        self.lions.place(x = 1400, y= 275)  

        img = PhotoImage(file = r"teams/rr_icon.png")
        self.royals = Label(self.master,image = img)
        self.royals.image = img
        self.royals.place(x = 10, y= 375)  

        img = PhotoImage(file = r"teams/kt_icon.png")
        self.tuskers = Label(self.master,image = img)
        self.tuskers.image = img
        self.tuskers.place(x = 1400, y= 375)  
                
    #Start is pressed    
    def start_auc(self):
        cursor.execute("select * from PLAYER where ID like {}".format(self.play))
        for r in cursor.fetchall():
            self.playname = Label(self.master, text = r[1] + '\t' + r[2],font = (24))
            self.playname.place(x=800, y=150)
            self.playcat = Label(self.master, text = r[3] +'\t',font = (24))
            self.playcat.place(x=800, y=200)
            self.b_val = Label(self.master, text = str(r[4]) + '\t' , font = (24))
            self.b_val.place(x=800, y=250)
            self.val = r[4]
        print(self.play)
        #Next button
        self.next = Button(self.f, text = 'NEXT', activebackground= 'green',width = 25, command = self.printrecord)
        self.next.place(x=800,y=700)        
        
        #Sold Button
        self.sold = Button(self.f, text = 'SOLD', activebackground= 'yellow',width = 25, command = self.sold_to)
        self.sold.place(x=640,y=450) 
        
    def bidding(self,i):
    
        #Clearing name currentbidder area
        self.currbid = Label(self.master, text ='\t\t\t',font = (24))
        self.currbid.place(x=800, y=100)
        
        if i == 1:
            self.name='Chennai Super Kings'
        elif i == 2:
            self.name='Royal Challengers'
        elif i == 3:
            self.name='Mumbai Indians'
        elif i == 4:
            self.name='Rajasthan Royals'
        elif i == 5:
            self.name='Kolkata Knight Riders'
        elif i == 6:
            self.name='Sunrisers Hyderabad'
        elif i == 7:
            self.name='Gujrat Lions'
        elif i == 8:
            self.name='Kochi Tuskers'                
        
        #Bidding values
        if self.val < 10000000:
            self.val = self.val + 200000
        else:
            self.val = self.val + 2000000

        self.currbid = Label(self.master, text = self.name,font = (24))
        self.currbid.place(x=800, y=100)
        self.cval = Label(self.master, text = 'Current value :',font = (24))
        self.cval.place(x=525, y=300)  
        self.c_val = Label(self.master, text = self.val , font = (24))
        self.c_val.place(x=800, y=300)

    def sold_to(self):

        cursor.execute("update PLAYER set TEAM = '{}',SOLDVALUE = '{}' where ID like {} ".format(self.name,self.val,self.play))  
        db.commit()
#        print(self.name, self.val)
        self.sold = Label(self.master, text = 'Sold to :',font = (20))
        self.sold.place(x=400, y=500)
        self.sold.config(font=("Courier", 44))
        self.sold_t = Label(self.master, text = self.name  ,font = (20))
        self.sold_t.place(x=350, y=600)
        self.sold_t.config(font=("Courier", 44))   
        
        self.b1.place(x=300,y=100) 

        #display team photo

        if(self.name == 'Chennai Super Kings'):
            img = PhotoImage(file = r"teams/csk.png")
        elif(self.name == 'Royal Challengers'):
            img = PhotoImage(file = r"teams/rcb.png") 
        elif(self.name == 'Mumbai Indians'):
            img = PhotoImage(file = r"teams/mi.png")
        elif(self.name == 'Rajasthan Royals'):
            img = PhotoImage(file = r"teams/rr.png")
        elif(self.name == 'Kolkata Knight Riders'):
            img = PhotoImage(file = r"teams/kkr.png")
        elif(self.name == 'Sunrisers Hyderabad'):
            img = PhotoImage(file = r"teams/sh.png")
        elif(self.name == 'Gujrat Lions'):
            img = PhotoImage(file = r"teams/gl.png")
        elif(self.name == 'Kochi Tuskers'):
            img = PhotoImage(file = r"teams/kt.png")
        self.t1 = Label(self.master,image = img)
        self.t1.image = img
        self.t1.place(x = 35, y= 460)  
       
        #marker - display player photo

        if(self.play == 1):
            imggg = PhotoImage(file = r"people/1.png")
        elif(self.play == 2):
            imggg = PhotoImage(file = r"people/2.png")
        elif(self.play == 3):
            imggg = PhotoImage(file = r"people/3.png")
        elif(self.play == 4):
            imggg = PhotoImage(file = r"people/4.png")
        elif(self.play == 5):
            imggg = PhotoImage(file = r"people/5.png")
        elif(self.play == 6):
            imggg = PhotoImage(file = r"people/6.png")
        elif(self.play == 7):
            imggg = PhotoImage(file = r"people/7.png")
        elif(self.play == 8):
            imggg = PhotoImage(file = r"people/8.png")
        elif(self.play == 9):
            imggg = PhotoImage(file = r"people/9.png")
        elif(self.play == 10):
            imggg = PhotoImage(file = r"people/10.png")
        elif(self.play == 11):
            imggg = PhotoImage(file = r"people/11.png")
        elif(self.play == 12):
            imggg = PhotoImage(file = r"people/12.png")
        elif(self.play == 13):
            imggg = PhotoImage(file = r"people/13.png")
        elif(self.play == 14):
            imggg = PhotoImage(file = r"people/14.png")
        elif(self.play == 15):
            imggg = PhotoImage(file = r"people/15.png")
        elif(self.play == 16):
            imggg = PhotoImage(file = r"people/16.png")
        elif(self.play == 17):
            imggg = PhotoImage(file = r"people/17.png")
        elif(self.play == 18):
            imggg = PhotoImage(file = r"people/18.png")
        elif(self.play == 19):
            imggg = PhotoImage(file = r"people/19.png")
        elif(self.play == 20):
            imggg = PhotoImage(file = r"people/20.png")
        elif(self.play == 21):
            imggg = PhotoImage(file = r"people/21.png")
        elif(self.play == 22):
            imggg = PhotoImage(file = r"people/22.png")
        elif(self.play == 23):
            imggg = PhotoImage(file = r"people/23.png")
        elif(self.play == 24):
            imggg = PhotoImage(file = r"people/24.png")
        elif(self.play == 25):
            imggg = PhotoImage(file = r"people/25.png")
        self.t2 = Label(self.master,image = imggg)
        self.t2.image = imggg
        self.t2.place(x = 1200, y= 480)

        #marker end

        #Disabling buttons    
        self.b1 = Button(self.f, text = 'BID',font = (24),bg= 'red')
        self.b2 = Button(self.f, text = 'BID',font = (24),bg= 'red')
        self.b3 = Button(self.f, text = 'BID',font = (24),bg= 'red')
        self.b4 = Button(self.f, text = 'BID',font = (24),bg= 'red')
        self.b5 = Button(self.f, text = 'BID',font = (24),bg= 'red')
        self.b6 = Button(self.f, text = 'BID',font = (24),bg= 'red')
        self.b7 = Button(self.f, text = 'BID',font = (24),bg= 'red')
        self.b8 = Button(self.f, text = 'BID',font = (24),bg= 'red')
        self.b1.place(x=300,y=100)
        self.b2.place(x=300,y=200)
        self.b3.place(x=300,y=300)
        self.b4.place(x=300,y=400)
        self.b5.place(x=1100,y=100)
        self.b6.place(x=1100,y=200)
        self.b7.place(x=1100,y=300)
        self.b8.place(x=1100,y=400)
             
    #next record
    def printrecord(self):      
    
        self.sold = Label(self.master, text = '\t\t\t',font = (24))
        self.sold.place(x=350, y=550)
        self.sold.config(font=("Courier", 44))
        self.sold_t = Label(self.master, text = '\t\t\t' ,font = (24))
        self.currbid = Label(self.master, text = '\t\t\t',font = (24))
        self.c_val = Label(self.master, text = '\t\t\t' , font = (24))
        self.c_val.place(x=800, y=300)
        self.currbid.place(x=800, y=100)
        self.sold_t.place(x=675, y=550)
        self.sold_t.config(font=("Courier", 44))
        self.playname = Label(self.master, text = '\t\t\t',font = (24))
        self.playname.place(x=800, y=150)
        self.playcat = Label(self.master, text = '\t\t\t' ,font = (24))
        self.playcat.place(x=800, y=200)
        self.b_val = Label(self.master, text = '\t\t\t' , font = (24))
        self.b_val.place(x=800, y=250)        
        
        self.play = self.play + 1
        cursor.execute("select * from PLAYER where ID like {}".format(self.play))
        for r in cursor.fetchall():
            self.playname = Label(self.master, text = r[1] + ' ' + r[2],font = (24))
            self.playname.place(x=800, y=150)
            self.playcat = Label(self.master, text = r[3] ,font = (24))
            self.playcat.place(x=800, y=200)
            self.b_val = Label(self.master, text = str(r[4]) , font = (24))
            self.b_val.place(x=800, y=250)
            self.val = r[4]
        
        
       #Enabling buttons
        self.l1 = Label(self.master, text = "Chennai Super Kings",font = (24))
        self.l1.place(x=100, y=100)        
        self.b1 = Button(self.f, text = 'BID',font = (24),activebackground= 'purple', command = lambda: self.bidding(1))
        self.b1.place(x=300,y=100)
       
        self.l2 = Label(self.master, text = "Royal Challengers",font = (24))
        self.l2.place(x=100, y=200)
        self.b2 = Button(self.f, text = 'BID',font = (24),activebackground= 'purple', command = lambda: self.bidding(2))
        self.b2.place(x=300,y=200)

        self.l3 = Label(self.master, text = "Mumbai Indians",font = (24))
        self.l3.place(x=100, y=300)
        self.b3 = Button(self.f, text = 'BID',font = (24), activebackground= 'purple',command = lambda: self.bidding(3))
        self.b3.place(x=300,y=300)

        self.l4 = Label(self.master, text = "Rajasthan Royals",font = (24))
        self.l4.place(x=100, y=400)
        self.b4 = Button(self.f, text = 'BID',font = (24),activebackground= 'purple', command = lambda: self.bidding(4))
        self.b4.place(x=300,y=400)

        self.l5 = Label(self.master, text = "Kolkata Knight Riders",font = (24))
        self.l5.place(x=1200, y=100)
        self.b5 = Button(self.f, text = 'BID',font = (24),activebackground= 'purple',command = lambda: self.bidding(5))
        self.b5.place(x=1100,y=100)

        self.l6 = Label(self.master, text = "Sunrisers Hyderbad",font = (24))
        self.l6.place(x=1200, y=200)
        self.b6 = Button(self.f, text = 'BID',font = (24), activebackground= 'purple',command = lambda: self.bidding(6))
        self.b6.place(x=1100,y=200)

        self.l7 = Label(self.master, text = "Gujrat Lions",font = (24))
        self.l7.place(x=1200, y=300)
        self.b7 = Button(self.f, text = 'BID',font = (24),activebackground= 'purple',command = lambda: self.bidding(7))
        self.b7.place(x=1100,y=300)

        self.l8 = Label(self.master, text = "Kochi Tuskers",font = (24))
        self.l8.place(x=1200, y=400)
        self.b8 = Button(self.f, text = 'BID',font = (24),activebackground= 'purple',command = lambda: self.bidding(8))
        self.b8.place(x=1100,y=400)           
    def exit_window(self):
        self.master.destroy()


     

        
root = Tk()
app = main_window(root)
root.mainloop()
