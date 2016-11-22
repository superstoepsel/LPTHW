from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "Every Scene Class has to have an enter function, that's why this is here."
        exit(1) #I fuckin don't understand what this is doing here....

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    lost = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "You are such a loser.",
        "My 2-year-old cousin is better at this."
    ]

    def enter(self):
        print Death.lost[randint(0, len(self.lost)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "This is the description of the scene that should be super creative."

        action = raw_input("> ")

        if action == "something":
            print "You did something."
            return 'death'

        elif action == "something else":
            print "you did something else and will survive."
            return 'laser_weapon_armory'

        else:
            print "Does not compute!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print "You have to guess a code to save the world. You have 10 chances to do it right."
        code = "%d%d%d" %(randint(1,9), randint(1,9), randint(1,9)) # this sets the numbers for the code the player has to get
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print "Not right!"
            guesses +=1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "You guessed right!"
            return 'the_bridge'

        else:
            print "YOu gessed wrong 10 times and will die."
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print "You got the code, now you have to do something."

        action = raw_input("> ")

        if action == "do something wrong":
            print "You did something wrong and will die."
            return 'death'

        elif action == "do something":
            print "You did something right and will survive."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return 'the_bridge'

class EscapePod(Scene):

    def enter(self):
        print "You did much right and survived till now."
        print "Now you have to guess right again, with a number between 1 and 5."
        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You guessed wrong."
            return 'death'
        else:
            print "You won!"
            return 'finished'

class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'


class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
