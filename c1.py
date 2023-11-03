import os 
import random
x= "choosen Dare"
y= "choosen Truth"
z= "do 50 pushups"
z1 = "do 50 situps"
random_number = random.randint(0,1)
print("Butterfly, Butterfly ,which colour do you like ? : 1) Blue 2) Red ")
a = input("Enter the colour: ")
if a == "Blue":
    print("Choose the number: 1) 4 2) 8 ")
    b = int(input("Enter the number : "))
    if b ==4:
        if random_number==1:
            print(x)
        elif random_number==0:
            print(y)   
    elif b==8:
        print(random(a,b))
        if random_number==1:
            print(x)
        elif random_number==0:
            print(y)
if a == "Red":
    print("Choose the number: 1) 4 2) 8 ")
    b = int(input("Enter the number : "))
    if b ==4:
        if random_number==1:
            print(z)
        elif random_number==0:
            print(z1)   
    elif b==8:
        if random_number==1:
            print(z)
        elif random_number==0:
            print(z1)
if a == str(1):
    exit
            




