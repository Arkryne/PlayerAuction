import sqlite3 
#SQLITE#BASE


db = sqlite3.connect('test2.db')
cursor = db.cursor()

def printrecord():
    cursor.execute('select * from PLAYER')
    for r in cursor.fetchall():
        print('Player name : {} {}'.format(r[0],r[1]) )
        
printrecord()

def printTeam():
    cursor.execute('select * from PLAYER where TEAM = "{}"'.format(self.TEAM)) 


DATABASE NAME  -TEST2.DB

        CREATE TABLE PLAYER
                 (ID INT PRIMARY KEY     NOT NULL,
                    FNAME           TEXT    NOT NULL,
                    LNAME           TEXT    NOT NULL,
                    CATEGORY           TEXT    NOT NULL,
                    BASEVALUE           INT    NOT NULL,
                    TEAM        CHAR(50),
                    SOLDVALUE           INT,
                    PICTURE       CHAR(50));
                 
        INSERT INTO PLAYER (ID,FNAME,LNAME,CATEGORY,BASEVALUE,TEAM,SOLDVALUE,PICTURE) VALUES (1,'Shikhar',' Dhawan     ','Batsman',10000000,' ',0,NULL);
        INSERT INTO PLAYER VALUES (2,'Suresh','Raina','Batsman', 10000000,' ',0,NULL);
        INSERT INTO PLAYER VALUES (3,'Chris','Gayle','Batsman', 10000000,' ',0,NULL);
        INSERT INTO PLAYER VALUES (4,'Virat','Kohli','Batsman',10000000,' ',0,NULL);
        INSERT INTO PLAYER VALUES (5,'Mahendra','S Dhoni','Wicket-Keeper',10000000,' ',0,NULL);
        INSERT INTO PLAYER VALUES (6,'Rohit','Sharma','Batsman',10000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (7,'AB','de Villiers','Batsman',10000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (8,'Ravichandran','Ashwin','Bowling',10000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (9,'Yuzvendra','Chahal','Bowler',10000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (10,'Ben','Stokes','All-rounder',10000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (11,'Jason','Roy','Batsman',10000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (12,'Kieron','Pollard','All-rounder',8000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (13,'Rashid','Khan','Bowler',12000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (14,'Pat','Cummins','Bowler',12000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (15,'James','Faulkner','Bowler', 12000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (16,'Mitchell','Johnson','Bowler', 12000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (17,'Glenn','Maxwell','Batsman',12000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (18,'Cameron','White','Batsman',12000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (19,'Brendon','McCullum','All-rounder',12000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (20,'Dwayne','Bravo','All-rounder', 6000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (21,'Corey','Anderson','All-rounder',6000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (22,'Kamlesh','Nagarkoti','Bowler',6000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (23,'K. L.','Rahul','Batsman',6000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (24,'Evin','Lewis','Batsman', 6000000 ,' ',0,NULL);
        INSERT INTO PLAYER VALUES (25,'Colin','Munro','Batsman',6000000 ,' ',0,NULL);