import time
import random
import sys
import pdb


def Challenge2():
    global Health
    global MHealth
    global Score
    global GHealth
    global GHealth
    global Key
    global Shovel
    MGhealth = 0
    Shovel = False
    Health = 0
    Key = False
    GHealth = 0
    Score = 0
    def My_raw_input(Question):
        Answer = raw_input(Question)
        if Answer == 'i' or Answer == 'I':
            print"Your health at this moment is " + str(Health) + "."
            print"Your score at this moment is " + str(Score) + "."
            time.sleep(4)
            return My_raw_input(Question)
        if Answer == 'q' or Answer == 'Q':
            print"You quit the game."
            time.sleep(2)
            sys.exit()
        #print Answer
        return Answer
    print"At any question you may type;"
    time.sleep(2)
    print"i for info"
    print"q to quit the game"
    time.sleep(4)
    print"Your goal in this game is to do whatever you need to do to escape."
    time.sleep(3)
    name = My_raw_input("May I ask you of your name: ")
    time.sleep(1)
    print"Thank you for your cooperation."
    time.sleep(1)
    gender = My_raw_input("Now, what might your gender be (Male or Female): ")
    while gender != 'Male' and gender != 'male' and gender != 'Female' and gender != 'female':
        gender = My_raw_input("What is your gender be (Male or Female): ")
    print"Thank you."
    time.sleep(1)
    Type = My_raw_input("What are you (Mage, Warrior or Archer): ")
    while Type != 'Mage' and Type != 'mage' and Type != 'Warrior' and Type != 'warrior' and Type != 'Archer' and Type != 'archer':
        print"Sorry that is not an option."
        time.sleep(1.4)
        Type = My_raw_input("What are you(Mage, Warrior or Archer): ")
    time.sleep(1)
    print"I thank you once again."
    time.sleep(1)
    print"Your name is " + name + "."
    time.sleep(1.5)
    print"And you are a " + gender + "."
    time.sleep(2)
    print"You are also a(n) " + Type + "."
    time.sleep(2)
    print"Your score is set to " + str(Score) + " right now."
    time.sleep(2)
    Key = False
    if Type == 'Mage' or Type == 'mage':
        MHealth = 10
        MGHealth = 5
    elif Type == 'Warrior' or Type == 'warrior':
        MHealth = 20
        MGHealth = 15
    elif Type == 'Archer' or Type == 'archer':
        MHealth = 15
        MGHealth = 10
    GHealth = MGHealth
    Health = MHealth
    print"Your health is at " + str(Health) + "."
    time.sleep(2)
    print"You are in the countryside manor of John Smith."
    time.sleep(2)
    print'         __           __                                            '
    print'        /  \\    _    /  \\                                         '
    print'       /    \\  / \\  / _  \\                                       '
    print'      /      \\/ _ \\/ |_|  \\___                                   '
    print'     /   ___  \\|_| \\ ____/     \\                    ___          '
    print'    /   |   |  \\____\\   /  ___  \\                  /   \\        '
    print'    |   |___|   \\    | /  |___|  \\     _          |  o  |         '
    print'    |____________\\   |/___________\\   / \\          \\___/        '
    print'    |  _    _    |   |             | /   \\           |             '
    print'    | |_|  |_|   |   |   _______   |/  __ \\          |             '
    print'    |    ___     |   |  |_______|  |  |  | |         |              '
    print'    |___|:|:|____|___|_____________|__|  |_|         |              '
    time.sleep(3.7)
    print"The room you reside in is the dungeons."
    time.sleep(3)
    print"You have fallen through a trapdoor and cannot get back out again."
    time.sleep(3.5)
    def N_room():
        global Key
        global Score
        global Shovel
        print"???: Hello? Is someone there?"
        time.sleep(1.6)
        Game = My_raw_input("???: I haven't had a guest in ages. Would you like to play a game with me(y or n): ")
        while Game != 'y' and Game != 'n':
            time.sleep(1)
            Game = My_raw_input("???: YES OR NO. What do you not get?: ")
        if Game == 'n':
            print"???: You have just made a big mistake"
            time.sleep(2)
            print"*CRACK*"
            time.sleep(2.1)
            print"???: I just cracked your skull."
            time.sleep(2.6)
            print"GAMEOVER"
            time.sleep(2)
            dungeon_room()
        elif Game == 'y':
            print"???: You chose well."
            time.sleep(1.4)
            print"???: My name is Samuel."
            Rand_number = int(random.uniform(1,10))
            time.sleep(1.6)
            print"Samuel: I am thinking of a number between 1 and 9."
            time.sleep(2.7)
            print"Samuel: Guess right and I will let you pass."
            time.sleep(3.3)
            print"Samuel: Guess wrong and..... well.... it's best you not know."
            time.sleep(3.8)
            print"Samuel: Oh, and you also get 3 tries."
            time.sleep(2)
            for x in range(1,4):
                while True:
                    try:
                        Users_input = int(My_raw_input("What is the number I am thinking about: "))
                        break
                    except ValueError:
                        print"Samuel: Hmmm... You did not answer my question."
                if Users_input > 9:
                    print"That is to high of a number"
                    time.sleep(1.7)
                if Users_input == Rand_number:
                    break
            if Users_input == Rand_number:
                Score += 100
                print"Samuel: He He He. You got it correct. You can now get behind me."
                time.sleep(3.8)
                print"The wall behind Samuel opens up to another room."
                time.sleep(4)
                print"Samuel steps aside."
                time.sleep(1)
                ShovelR = My_raw_input("Would you like to enter (y or n): ")
                while ShovelR != 'y' and ShovelR != 'Y' and ShovelR != 'n' and ShovelR != 'N':
                    print"Not an option"
                    time.sleep(2)
                    ShovelR = My_raw_input("Would you like to enter (y or n): ")
                if ShovelR == 'n' or ShovelR == 'N':
                    print"You turn back and walk to the main room."
                    time.sleep(2)
                    dungeon_room()
                elif ShovelR == 'y' or ShovelR == 'Y':
                    print"You walk in and find a large chest right in the middle of the room."
                    time.sleep(3)
                    if Key == True:
                        print"You take out the key from the giant and slip it into the lock."
                        time.sleep(3)
                        print"The lock clicks and the lid of the chest pops open."
                        time.sleep(2)
                        print"Inside is a shovel. You take it and sling it over your back."
                        time.sleep(2.3)
                        Shovel = True
                        print"You walk back to the main room."
                        time.sleep(1)
                        dungeon_room()
                    elif Key == False:
                        print"The chest has a big lock on the side."
                        time.sleep(2)
                        print"You do not have a key so you turn back to the main room."
                        time.sleep(3)
                        dungeon_room()
            else:
                print"Samuel: He He He. You should have guessed " + str(Rand_number) + "."
                time.sleep(2.6)
                print"Samuel: Goodnight and don't let the bed-bugs bite!"
                time.sleep(2.3)
                print"All the torches in the dungeon flicker.... and go out."
                time.sleep(2.5)
                print"GAMEOVER"
                time.sleep(2)
                dungeon_room()
    def S_room():
        print"Your eyes adjust to the darkness and you find a tall archway standing off to the side."
        time.sleep(5)
        B_back = My_raw_input("Do you wish to go back(y or n): ")
        while B_back != 'y' and B_back != 'n':
            print"You walked into the wall."
            B_back = My_raw_input("Do you wish to go back(y or n): ")
        if B_back == 'n':
            Monster_way = My_raw_input("Do you wish to enter the arch(y or n): ")
            while Key == True:
                print"You peek your head in but nothing sticks out."
                time.sleep(2.3)
                print"You turn back toward the main room."
                time.sleep(1.7)
                dungeon_room()
            while Monster_way != 'y' and Monster_way != 'n':
                print"You walked into the wall."
            if Monster_way == 'n':
                print"You turned and walked back to the main room."
                time.sleep(1.7)
                dungeon_room()
            elif Monster_way == 'y':
                arch_room()
        elif B_back == 'y':
            print"You turn and walk back to the main room."
            time.sleep(2)
            dungeon_room()
    def arch_room():
        print"You step through the doorway and light floods your eyes."
        time.sleep(3)
        print"In front of you a giant looms over a fire on the ground."
        time.sleep(3)
        print"He turns around, steps over you and blocks the doorway."
        time.sleep(3)
        global GHealth
        global Health
        global MHealth
        while GHealth > 0 and Health > 0:
            print"Your health right now is at " + str(Health) + "."
            print"And the giants health is at " + str(GHealth) + "."
            time.sleep(4)
            Fight = My_raw_input("Fight the giant or run away?(Run or Fight): ")
            while Fight != 'run' and Fight != 'fight' and Fight != 'Fight' and Fight != 'Run':
                print"That is not an option."
                time.sleep(1)
                Fight = My_raw_input("Run or fight, which is it going to be: ")
            if Fight == 'run' or Fight == 'Run':
                rand_hit_giant = int(random.uniform(1,MHealth + 1))
                print"You bolt under the foul beast's arm but his club clips your shoulder."
                time.sleep(3)
                Check_H(rand_hit_giant)
                print"You will live to see another day."
                time.sleep(2)
                print"You quickly get up and run to the main room."
                time.sleep(2.3)
                dungeon_room()
            elif Fight == 'fight' or Fight == 'Fight':
                rand_hit = int(random.uniform(1,MGHealth + 1))
                rand_hit_giant = int(random.uniform(1,MHealth + 1))
                if Type == 'Archer' or Type == 'archer':
                    print"You nock an arrow in your bow and let it fly."
                    time.sleep(2)
                    
                elif Type == 'Mage' or Type == 'mage':
                    print"You raise your staff and shoot a fireball."
                    time.sleep(3)
                    
                elif Type == 'Warrior' or Type == 'warrior':
                    print"With your sword raised high, you run at the giant."
                    time.sleep(2.5)
                    
                Check_GH(rand_hit)
                if Key == True:
                    print"You quickly run back to the main room."
                    time.sleep(1.6)
                    dungeon_room()
                if GHealth > 0:
                    print"The giant swings his club."
                    time.sleep(2)
                    print"You slam against the wall."
                    time.sleep(2)
                Check_H(rand_hit_giant)
    def Check_GH(Hit):
        global GHealth
        global Key
        global Score
        GHealth = GHealth - Hit
        if GHealth < 1:
            print"The giant falls down."
            time.sleep(1.3)
            print"A key is dangling from his belt."
            time.sleep(1.8)
            print"You take it and slip it into your robe."
            time.sleep(2)
            Key = True
            Score += 100
    def Check_H(Hit):
        global Health
        Health = Health - Hit
        if Health < 1:
            print"You have incurred a mortal wound."
            time.sleep(2)
            print"GAMEOVER"
            sys.exit()
    def E_room():
        global Shovel
        print"You have found a grand room with lots of gold and coins."
        time.sleep(2.2)
        print"Directly in front of you, across the room, is a doorway."
        time.sleep(2.1)
        B_back = My_raw_input("Do you wish to go back(y or n): ")
        while B_back != 'y' and B_back != 'n':
            print"You walked into the wall."
            B_back = My_raw_input("Do you wish to go back(y or n): ")
        if B_back == 'n':
            print"THOOOOM!!!"
            time.sleep(2)
            print"A dragon has just erupted out of the mountain of gold!"
            time.sleep(3)
            Lastwords = My_raw_input("Any last words: ")
            while Lastwords == 'yolo' or Lastwords == 'Yolo' or Lastwords == 'YOLO':
                print"The dragon burnt you to a crisp."
                time.sleep(2)
                print"GAMEOVER"
                time.sleep(2)
                dungeon_room()
            if Lastwords != 'yolo' and Lastwords != 'Yolo' and Lastwords != 'YOLO':
                print"The dragon falls back asleep."
                time.sleep(1.4)
                print"And you face the doorway."
                time.sleep(1.5)
                Doorway = My_raw_input("Would you like to enter (y or n): ")
                while Doorway != 'y' and Doorway != 'Y' and Doorway != 'n' and Doorway != 'N':
                    print"Not an option."
                    time.sleep(2)
                    Doorway = My_raw_input("Enter or not (y or n): ")
                if Doorway == 'n' or Doorway == 'N':
                    print"You turn and walk back to the main room"
                    time.sleep(2)
                    dungeon_room()
                elif Doorway == 'y' or Doorway == 'Y':
                    print"As you step in... cold air washes over you."
                    time.sleep(2)
                    print"The ground is uneven as you step over it."
                    time.sleep(2)
                    print"The dirt is loose and in hard clumps."
                    while Shovel == True:
                        print"You take out your shovel and start digging."
                        time.sleep(2)
                        print"A few minutes later you fall through into a tunnel."
                        time.sleep(2)
                        print"Behind you is a dead end so you walk the other way."
                        time.sleep(2)
                        print"A few turns later a small bit of daylight appears at the end of the tunnel."
                        time.sleep(3)
                        print"When you get to the end, you find a beautiful view of rolling hills and bright sunlight."
                        time.sleep(4)
                        print"You have successfully escaped the dungeon."
                        time.sleep(2)
                        print"YOU WIN!!!"
                        time.sleep(3)
                        sys.exit()
                    if Shovel == False:
                        print"Nothing of interest appears to you so you walk back to the main room"
                        time.sleep(3)
                        dungeon_room()
            print"The dragon burnt you to a crisp."
            time.sleep(2.4)
            print"GAMEOVER"
            time.sleep(2)
            dungeon_room()
        elif B_back == 'y':
            dungeon_room()
    def W_room():
        global Health
        global HealthP
        global MHealth
        global Key
        print"You enter a small room about the size of your kitchen."
        time.sleep(2)
        print"At the side of the room there is a doorway leading outside."
        time.sleep(2)
        print"In front of you there is a doorway leading into another room"
        time.sleep(2)
        Escape = My_raw_input("Would you like to go through to the outside (y or n): ")
        while Escape != 'y' and Escape != 'Y' and Escape != 'n' and Escape != 'N':
            print"Not an option."
            time.sleep(1)
            Escape = My_raw_input("Outside or no (y or n): ")
        if Escape == 'y' or Escape == 'Y':
            print"When you step through the door you find a 100 foot drop yawning at you."
            time.sleep(3)
            print"You fall to your death"
            time.sleep(2)
            print"GAMEOVER"
            time.sleep(2)
            dungeon_room()
        elif Escape == 'n' or Escape == 'N':
            Room = My_raw_input("Do you wish to enter the doorway leading to another room(y or n): ")
            while Room != 'y' and Room != 'Y' and Room != 'n' and Room != 'N':
                print"Not an Option"
                time.sleep(2)
                Room = My_raw_input("Another room or not (y or n): ")
            if Room == 'n' or Room == 'N':
                print"You turn back and walk to the main room."
                time.sleep(2)
                dungeon_room()
            elif Room == 'y' or Room == 'Y':
                print"When you step through the doorway you see a small canister floating above the ground."
                time.sleep(3.5)
                print"You walk over and pick it up"
                time.sleep(2)
                HealthP = True
                #print HealthP
                #print Health
                #print MHealth
                #print Key
                if HealthP == True and Health < MHealth and Key == True:
                    Health = MHealth
                    print"The small canister starts glowing and then disapears."
                    time.sleep(2)
                    print"You suddenly feel much better and all your cuts seem to have disapeared."
                    time.sleep(3)
                    print"You walk over back to the main room."
                    time.sleep(1.4)
                    dungeon_room()
                else:
                    print"The canister seems to have no use."
                    time.sleep(2)
                    print"Your chuck it across the room and leave."
                    time.sleep(2)
                    dungeon_room()
    def dungeon_room():
        print"The dungeon has no windows and four doors, one in each direction."
        time.sleep(3)
        direction = My_raw_input("Where would you like to go(n, s, e, or w): ")
        #print "dungeon_room" + direction
        while direction != 'n' and direction != 's' and direction != 'e' and direction != 'w':
            print"You walked into the wall."
            direction = My_raw_input("Where would you like to go(n, s, e, or w): ")
            #print "dungeon_room" + direction
        if direction == 'n':
            N_room()
        elif direction == 's':
            S_room()
        elif direction == 'e':
            E_room()
        elif direction == 'w':
            W_room()
    dungeon_room()

global Score
global HeathP
HealthP = False
Score = 0
Challenge2()