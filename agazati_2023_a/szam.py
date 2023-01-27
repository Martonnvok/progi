import random

def elso():

    szamR = random.randint(1,50)
    print("I/A:")
    print("\t A generált szám:"+str(szamR))
    if szamR % 5==0 :
        print("I/B:")
        print("\t A szám öttel osztható!")
    elif szamR % 3 == 0:
        print("I/B:")
        print("\t A szám hárommal  osztható!")
    elif szamR % 5 == 0 and szamR % 0 == 3:
        print("I/B:")
        print("\t A szám öttel és hárommal is osztható!")