backpack = []

def staircase():
    print "After 8 steps, there is a big gap with 3 missing steps."
    print "What will you do? Jump or go back to the lobby?"

    if "ladder" in backpack:
        print "Your third option now is to use the ladder to bridge the gap."

    stairchoice = raw_input("> ")

    if "jump" in stairchoice:
        dead("You are too fat to jump 3 steps upwards.")
    elif "back" in stairchoice or "lobby" in stairchoice:
        backpack.append("beenToStairs")
        start()
    elif "ladder" in backpack and "ladder" in stairchoice:
        print "Ohoh, the ladder builds not a safe bridge."
        print "What do you do?"
        print "1. Rush over the ladder"
        print "2. Try to get over the ladder slowly"
        print "3. Not take the ladder"

        gapchoice = raw_input("> ")
        gapchoiceNumber = int(gapchoice)

        if gapchoiceNumber == 1:
            dead("Rushing is not safe. You fall down!")
        elif gapchoiceNumber == 2:
            print "Yay, you've done it! You can go further upstairs."
            print "You've found the treasure. It's an old golden medallion."
            print "As you go back to the granny she tells you that it's worth over 1 Million $."
            print "Congratulations! You are rich!"
            exit(0)
        else:
            dead("Well, you had your chance, but no risk, no fun!")
    else:
        print "You better make a choice."
        staircase()


def front_door():
    print "As you go outside, you stand on a beautiful field of flowers."
    if "spokenwithgranny" not in backpack:
        print "It's a beuatiful day and I can't stop myself from smiling..."
        print "But now go back inside."
        start()
    else:
        print "Wanna pick some?"

        flowerchoice = raw_input("> ")

        if "yes" in flowerchoice:
            print "There are 3 red ones and 20 blue ones."
            print "1. Which color do you choose?"
            colorchoice = raw_input("> ")
            print "2. How many will you pick?"
            numberchoice = raw_input("> ")
            numberchoiceNumber = int(numberchoice)

            if "red" in colorchoice and numberchoiceNumber > 3:
                print "I said, there are only 3 red ones, dumbass!"
                print "You get one more chance:"
                front_door()
            elif "red" in colorchoice and numberchoiceNumber <=3:
                print "You got", numberchoice, "red flowers in your backpack."
                backpack.append("flowers")
                print "Sun is strong today. You better go inside."
                start()
            elif "blue" in colorchoice and numberchoiceNumber <= 20:
                print "You could pick", numberchoice, "blue flowers."
                print "But do you remember what granny wanted?"
                print "Are you sure you want to take", numberchoice, "blue flowers?"

                flowerchance = raw_input("> ")

                if "Yes" in flowerchance:
                    dead("Well, if you can't do what you're told, you will die with", numberchoice, "blue flowers in your backpack.")
                elif "No" in flowerchance:
                    front_door()
            elif "blue" in colorchoice and numberchoiceNumber > 20:
                dead("You can't take more flowers than there are, greedy environmental wrecker!")
            else:
                print "You have to make a choice, dumbass!"
                front_door()

        else:
            dead("If you go back to granny, she would slay you with the rolling pin. \nNobody dissapoints an old lady!")


def grannys_room():
    print "An old lady is sitting in a wheelchair at the end of the room."
    print "She greets and waves you nearer."
    print "What do you do?"

    grannychoice = raw_input("> ")

    if "back" in grannychoice or "leave" in grannychoice:
        print "You are a unfriendly bastard! If a granny waves, you can't just go!"
        start()
    elif ("granny" in grannychoice or "go to" in grannychoice) and "spokenwithgranny" not in backpack:
        print "Granny takes your hand and whispers in your ear:"
        print "\"Dear Child, would you be as nice to bring me some flowers?"
        print "But I don't like blue ones - only red ones!\""
        backpack.append("spokenwithgranny")
        print "\tShe sends you back to the lobby."
        start()
    elif "beentogrannytwice" in backpack and "flowers" not in backpack:
        dead("You are too silly to pick flowers for granny - you should not proceed this game!")
    elif ("granny" in grannychoice or "go to" in grannychoice) and "spokenwithgranny" in backpack:
        if "flowers" in backpack and "beenToStairs" not in backpack:
            print "You give the red flowers to Granny."
            print "She smiles at you and takes your hand."
            print "Then she says:"
            print "\"Good child, you have to know, I am rich and I am old."
            print "As I can't walk anymore, I can't reach the treasure on the first floor anymore."
            print "But you are young, and you can do this - so go get the treasure!\""
            print "\tShe sends you back to the lobby."
            start()
        elif "flowers" in backpack and "beenToStairs" in backpack:
            print "Granny smiles at you and takes your hand."
            print "Then she says:"
            print "\"Good child, you have to know, I am rich and I am old."
            print "As I can't walk anymore, I can't reach my treasure on the first floor anymore."
            print "But you are young, and you can do this - so go get the treasure!"
            print "As you say, you already tried to go upstairs and there is a gap in the stairs:"
            print "In the room across the lobby there must be a ladder that should help you cross the gap."
            print "Here you have the key to open the door.\""
            backpack.append("key")
            print "\tShe sends you back to the lobby."
            start()
        else:
            print "You nasty child, granny asked for flowers, so go get her some!"
            backpack.append("beentogrannytwice")
            print "\tShe sends you back to the lobby."
            start()
    else:
        print "There are only to choices: go to her or leave the room!"
        grannys_room()


def ladderroom():
    if "key" not in backpack:
        print "The door is locked. No chance to get in this room."
        backpack.append("tried_to_go_in_locked_room")
        start()
    elif "key" not in backpack and "tried_to_go_in_locked_room" in backpack:
        print "Are you silly? I said there is no chance you will get inside!"
        dead("You should not proceed this game, your IQ seems to be too low.")
    elif "key" in backpack:
        print "The door is locked."
        print "And now?"

        opendoor = raw_input("> ")

        if "unlock" in opendoor or "key" in opendoor or "open" in opendoor:
            print "Congratulations! Granny's key fits and you can open the door!"
            print "As you go in, you see a ladder leaning on the opposite wall."
            print "In the corner, there is an opened safe. Inside, there are 5.000 $."
            print "What do you do?"

            ladderchoice = raw_input("> ")

            if "ladder" in ladderchoice:
                print "Great! You grab the ladder and go back to the lobby."
                backpack.append("ladder")
                start()
            elif "money" in ladderchoice:
                print "You are a greedy bastard!"
                dead("Upstairs, there would have been 1 million dollar. \nBut greedy bastards never get rich, bitch!")
            else:
                print "You have to make a valid choice, dumbass!"
                ladderroom()
        else:
            print "If you do nothing, you have to go backwards."
            start()


def start():
    print "You are in the lobby of a big house."
    print "There is a staircase in front of you,"
    print "a door to the left, a door to the right"
    print "and the front door behind you."
    print "Where do you go?"

    choice = raw_input("> ")

    if "left" in choice:
        ladderroom()
    elif "right" in choice:
        grannys_room()
    elif "backwards" in choice or "door" in choice or "back" in choice or "behind" in choice:
        front_door()
    elif "stair" in choice or "front" in choice:
        staircase()
    else:
        print "Dude, are you too silly to make a proper choice?"
        dead("You are not qualified to win this game.")

def dead(why):
    print why, "Too bad!"
    exit(0)

start()
