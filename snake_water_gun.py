import random
import time
lst=["s","w","g"]
choice1 = random.choice(lst)
a = 0  # user
b = 0  # computer
print("For snake use \'s\', for water use \'w\', for gun use \'g\' ")
num = int(input("How many times you want to play the game: "))
time.sleep(1)
for i in range(1,num+1):
    inp= input("Snake , water or gun: ")
    time.sleep(2)
    print("^_^ My turn:",choice1)
    if inp==choice1:
        a+=0
        b+=0
    elif inp=="s" and choice1=="w":
        a+=1
        b+=0
    elif inp == "w" and choice1 == "s":
        a += 0
        b += 1
    elif inp == "g" and choice1 == "w":
        a+=0
        b+=1
    elif inp == "w" and choice1 == "g":
        a+=1
        b+=0
    elif inp == "g" and choice1 == "s":
        a+=1
        b+=0
    elif inp == "s" and choice1 == "g":
        a+=0
        b+=1
    i+=1
if a==b:
    print("--------------------------------------------------------")
    print("--------------------------------------------------------")
    print("Oops,it\'s a toss!")
elif a>b:
    print("--------------------------------------------------------")
    print("--------------------------------------------------------")
    print("Fab!! U won ;)")
else:
    print("--------------------------------------------------------")
    print("--------------------------------------------------------")
    print("Hehe...better luck next time >_<")
print("Your score:",a)
