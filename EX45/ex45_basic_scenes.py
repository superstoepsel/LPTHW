from sys import exit

class Scene(object):
    def enter(self):
        pass

    def WrongDecision(self):
        print "If you can't make choices you will be no detective and the murder will find and kill you!"
        return 'dead'
        exit(1)

class Basement(Scene): # the Start scene. Setting and task have to be explained.

     def enter(self):
         print "It's Saturday 10AM and you went on a weekend trip"
         print "to the swedish Block House of your friend Paul"
         print "with 4 other people you know more or less."
         print "There is a huge gale blowing outside that locks"
         print "you into the house and all of your phones have poor signal."
         print "Yesterday, you had a big party and you can't remember"
         print "anything that happened after 11pm, because you had some"
         print "Tequila shots that were just too much."
         print "Half an hour ago you found something really shocking in the basement bathroom:"
         print "Paul lies there on the floor in a huge pool of blood."
         print "With a blood-covered pen sticking in his throat, he stares at the"
         print "ceiling and his body is already stiff."
         print "It's obvious that he must have been murdered - but who the hell would do this?"
         print "Besides this, the murder must be still in this house, as the gale is blowing since yesterday afternoon!"
         print "You have to find out who did this and why - maybe the killer is a psycho that will murder more people?"
         print "Will you be brave and take a closer look to the corpse?"

         action = raw_input("> ")

         if action == "Yes" or action == "yes":
             print "Ugh, corpses are cold and ugly!"
             print "This is waaaaay too much blood that is spilled over Paul's body!"
             print "But wait, there is something written on the pen in his throat:"
             print "'Harvard University' it says there."
             print "The murder must still be in this house - scary!"
             print "While you are looking for more hints, "
             print "you see that there is a little red piece of fabric in Paul's stiff hand."
             print "He must have been fighting before the murder killed him!"
             print "There are no more hints here. You go upstairs to find out what to do next."
             return 'decision'
         elif action == "No" or action == "no":
             print "Okay, then finding the murder will be much harder."
             print "You go upstairs to find out more."
             return 'decision'
         else:
            print "You have to decide!"
            return 'basement'

class TheBigDecision(Scene): # First task for the player: Will he proceed or will he crash the game?

    def enter(self):
        print "Now you have to decide:"
        print "Will you tell the others what you found "
        print "Or will you try to find out by yourself what happened?"

        decision = raw_input("> ")

        if "tell" in decision or "others" in decision:
            print "As you bring everyone together in the living room"
            print "and tell them that you found Paul dead in the basement toilet,"
            print "his brother completely overacts and kills everyone of you."
            print "You will never find out what he did and why...."
            return 'dead'
        elif "myself" in decision or "find" in decision:
            print "Good choice! You never know what a murder is able to do!"
            print "You are in the central corridor in the house."
            print "In this house, there must be 3 more people: Anna, Rebecca and Kevin."
            print "Kevin is Paul's brother. Rebecca is his girlfriend and Anna is her best friend."
            return 'central_corridor'
        else:
            return self.WrongDecision()

class CentralCorridor(Scene): # define the central corridor of the house.
    #This is the scene where the player can actively decide for a scene.

    def enter(self):
        print "Your room is to your right,"
        print "the Living room to your left."
        print "Anna's room is behind you and"
        print "in front of you, there are the stairs."
        print "Where will you go?"

        direction = raw_input("> ")

        if "my" in direction or "My" in direction or "right" in direction:
            return 'your_room'
        elif "iving" in direction or "left" in dircetion:
            return 'living_room'
        elif "stairs" or "front" in direction:
            return 'first_floor'
        elif "behind" in direction or "Anna" in direction:
            return 'annas_room'
        else:
            return self.WrongDecision()

class Death(Scene):

    lost = 'Too pity!'

    def enter(self):
        print Death.lost
        exit(0)

class GuessingScene(Scene):
    def enter(self):
        pass

    def WrongDecision(self):
        pass

    def wanna_guess(self):
        print "Do you think you have enough hints to know the murder?"

        makeAGuess = raw_input("> ")

        if makeAGuess == ["Yes" or "yes"]:
            return 'who_is_it'
        else:
            pass

class YourRoom(GuessingScene): # The player will find one more hint on his phone
    def enter(self):
        print "In your room, you find your phone."
        print "As you unlock it, you find some group-selfies from tonight, around 1am:"
        print "There you are, all of you smiling into the camera:"
        print "On the left, there is Anna. She is wearing a white shirt and Jeans."
        print "All over her shirt, she has spilled red wine and she seems very drunk."
        print "Next to her, there is Rebecca. She wears her big fat Harvard Shirt and"
        print "some cozy joggers and has a big smile for the camera."
        print "In the middle, there is you. If you look at your face, it is obvious"
        print "why you can't remember anything, you look reeeeeally drunk. You wear your"
        print "You wear your favourite yellow "

    def wanna_guess(self):
        super(YourRoom, self).wanna_guess()
        return 'your_room'

class LivingRoom(Scene): # Here, the player will find Kevin.
    pass

class AnnasRoom(Scene): # Here, the player will find Anna.
    pass

class FirstFloor(Scene): # Here is only one more room that is accesible: The safe.
    pass

class WhoIsIt(Scene):

    def enter(self):
        print "You think you know the murder?"
        print "Make a choice:"
        print "1. You"
        print "2. Anna"
        print "3. Rebecca"
        print "4. Kevin"

        murderGuess = raw_input("[keypad]> ")

        if murderGuess == "4":
            print "You are right! Kevin murdered his brother..."
            print "Wanna know why? It's simple: They are professional thieves!"
            print "Time to time, they invite friends to their house and steal their things..."
            print "Upstairs, they have a huge safe for their stolen goods."
            print "Yesterday night, Paul showed Anna this safe. Kevin did not understand"
            print "why his brother revealed their secret, got really angry and killed Paul."
            return 'finished'
        else:
            print "You are wrong... Seems like you should have catched more hints..."
            print "Now the real murder will find and kill you."
            return 'dead'


class Saved(Scene):
    pass

class Map(object):
    scenes = {
    'basement' : Basement(),
    'decision' : TheBigDecision(),
    'central_corridor' : CentralCorridor(),
    'your_room' : YourRoom(),
    'living_room' : LivingRoom(),
    'annas_room' : AnnasRoom(),
    'first_floor' : FirstFloor(),
    'finished' : Saved(),
    'dead' : Death(),
    'who_is_it' : WhoIsIt()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
