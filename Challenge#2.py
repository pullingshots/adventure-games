import time
import random

def Challenge2():
    name = raw_input("May I ask you of your name: ")
    time.sleep(1)
    print"Thank you for your cooperation."
    time.sleep(1)
    gender = raw_input("Now, what might your gender be (Male or Female): ")
    time.sleep(1)
    print"I thank you once again."
    time.sleep(1)
    print"Your name is " + name + "."
    time.sleep(1.5)
    print"And you are a " + gender + "."
    time.sleep(2)
    print"You are in the countryside manor of Eledir Maskati."
    print'      _                       _'
    print'     / \\         ___        /   \\'
    print'    /   \\       /   \\      |  o  |'
    print'   /  _  \\_____/  _  \\      \\ _ /'
    print'   | |_| |       |_| |        | '
    print'   |  _  |   ____    |        | '
    print'   | | | |  |____|   |        | '
    time.sleep(3.7)
    print"The room you reside in is the dungeons."
    time.sleep(3)
    print"You had fallen through a trapdoor and cannot get back out again."
    time.sleep(3.5)
    def N_room():
        print"???: Hello? Is someone there?"
        time.sleep(1.6)
        Game = raw_input("???: I haven't had a guest in ages. Would you like to play a game with me(y or n): ")
        while Game != 'y' and Game != 'n':
            time.sleep(1)
            Game = raw_input("???: YES OR NO. What do you not get?: ")
        if Game == 'n':
            print"You have just made a big mistake"
            time.sleep(2)
            print"*CRACK*"
            time.sleep(2.1)
            print"GAMEOVER"
            time.sleep(2)
            dungeon_room()
        elif Game == 'y':
            print"???: You chose well."
            time.sleep(1.4)
            print"Samuel: My name is Samuel."
            Rand_number = int(random.uniform(1,1000))
            time.sleep(1.6)
            print"Samuel: I am thinking of a number between 1 and 999."
            time.sleep(2.7)
            print"Samuel: Guess right and I will free you from this dungeon."
            time.sleep(3.3)
            print"Samuel: Guess wrong and..... well.... it's best you not know."
            time.sleep(3.8)
            while True:
                try:
                    Users_input = int(raw_input("What is the number I am thinking about: "))
                    break
                except ValueError:
                    print"Samuel: Hmmm... You did not answer my question."
            if Users_input == Rand_number:
                print"Samuel: He He He. You got it correct. You are now free."
                time.sleep(3.8)
                print"The wall behind Samuel opens up to a plain of rolling hills."
                time.sleep(4)
                print"Samuel steps aside and lets you walk through."
                time.sleep(2.7)
                print"YOU WIN"
            else:
                print"Samuel: He He He. You should have guessed " + str(Rand_number) + "."
                time.sleep(2.6)
                print"Samuel: Goodnight and don't let the bed-bugs bite!"
                time.sleep(2.3)
                print"All the torches in the dungeon flicker.... and go out."
                time.sleep(2.5)
                print"GAMEOVER"
    def S_room():
        print"A horde of slowly-moving corpses are coming towards you."
        time.sleep(2.3)
        B_back = raw_input("Do you wish to go back(y or n): ")
        while B_back != 'y' and B_back != 'n':
            print"You walked into the wall."
            B_back = raw_input("Do you wish to go back(y or n): ")
        if B_back == 'n':
            print"You got close enough to see their sharp, crude teeth."
            time.sleep(2.5)
            print"AIEEEEEEEEEEE!!!!!"
            time.sleep(1)
            print"GAMEOVER"
            time.sleep(2)
            dungeon_room()
        elif B_back == 'y':
            dungeon_room()
    def E_room():
        print"You have found a grand room with lots of gold and coins."
        time.sleep(2.2)
        print"Think there might be a dragon sleeping under all of it?"
        time.sleep(2.2)
        B_back = raw_input("Do you wish to go back(y or n): ")
        while B_back != 'y' and B_back != 'n':
            print"You walked into the wall."
            B_back = raw_input("Do you wish to go back(y or n): ")
        if B_back == 'n':
            print"THOOOOM!!!"
            time.sleep(2)
            print"A dragon has just erupted out of the mountain of gold!"
            time.sleep(3)
            print"Any last words?"
            time.sleep(2.4)
            print"GAMEOVER"
            time.sleep(2)
            dungeon_room()
        elif B_back == 'y':
            dungeon_room()
    def W_room():
        print"Ha! You found an escape out!"
        time.sleep(2)
        print"Only to fall into the moat with snapping crocodiles."
        time.sleep(2.3)
        print"GAMEOVER"
        time.sleep(2)
        dungeon_room()
    def dungeon_room():
        print"The dungeon has no windows and four doors, one on each side."
        time.sleep(5)
        print"The walls are made of aging brick."
        time.sleep(3.5)
        direction = raw_input("Do you wish to go n, s, e, or w: ")
        while direction != 'n' and direction != 's' and direction != 'e' and direction != 'w':
            print"You walked into the wall."
            direction = raw_input("Do you wish to go n, s, e, or w: ")
        if direction == 'n':
            N_room()
        elif direction == 's':
            S_room()
        elif direction == 'e':
            E_room()
        elif direction == 'w':
            W_room()

    dungeon_room()

Challenge2()