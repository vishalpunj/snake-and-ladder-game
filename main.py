import random
p1pos=0
p2pos=0      


def dice():
    i=input("roll dice? y/n ")
    if(i=='y'):
        n=random.randint(1,6)
        print(n)
        
    elif(i=='n'):
        print("game ends")
def snakeandladder(x):
    snakes={10:2,22:6,50:15,71:35,98:1}

    ladder={5:30,13:70,44:60,60:81,82:95}
   
    if (x in snakes.keys()):
        x=snakes[x]
        print("snake encountered!!! new position is :",x)
    elif (x in ladder.keys()):
        x=ladder[x]
        print("ladder encountered!!! new position is :",x)
   
    
def play():
    
    if (p1pos<100 and 0<p2pos<100):
        print("player1 start: ")
        n=0
        dice()
        p1pos=p1pos+n
        print("p1 position is :",p1pos)
        snakeandladder(p1pos)
        print("plaeyer 2 start: ")
        dice()
        p2pos=p2pos+n
        print("p2 position is: ",p2pos)
        snakeandladder(p2pos)
    elif(p1pos==100 or p2pos==100):
        print("game ends")
play()
