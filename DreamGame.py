# 2/23/2023

from pygame import mixer

def death():
    skull = """
        .... NO! ...                  ... MNO! ...
    ..... MNO!! ...................... MNNOO! ...
    ..... MMNO! ......................... MNNOO!! .
    .... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
    ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
        ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
    ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
    ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...  
        ....... MMMMM..    OPPMMP    .,OMI! ....
        ...... MMMM::   o.,OPMP,.o   ::I!! ...
            .... NNM:::.,,OOPM!P,.::::!! ....
            .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
            ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
            .. MMMMMNNOOMMNNIIIPPPOO!! ......
            ...... MMMONNMMNNNIIIOO!..........
        ....... MN MOMMMNNNIIIIIO! OO ..........
        ......... MNO! IiiiiiiiiiiiI OOOO ...........
    ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
    .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
    ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
        ...... OO! ................. ON! .......
            ................................
            """
    print(skull)
    print("You have died.\n")
    while True:
        respawn_decision = input("Respawn? (y/n)\nYour decision: ")
        if respawn_decision == "y":
            return True
        elif respawn_decision == "n":
            return False
        else:
            print("\n >> Invalid Action <<\n")

def main(welcome_message):
    print(welcome_message)
    input("\n> Press 'Enter' to advance through the events.")

    # Game Stage - The Mountain
    input("\n-- The Mountain --")
    print("You wake up feeling a burning sensation on your left forearm. On your wrist, you see a tattoo of a pine tree, but")
    print("you don't remember ever getting one. It also glows orange briefly for a moment, but fades before you can blink")
    input("and believe what you saw.")

    print("\nStanding up, you find yourself on a small grassy field in a forest. The surrounding terrain is mildly steep,")
    print("and when you look up, you see an opening through the trees going uphill. Behind you, there's also appears to be")
    input("a path heading down the mountain.")
    # Decision - UPHILL or DOWNHILL
    while True:
        print("\nWhich way do you go?")
        starting_path = input("(a) uphill\n(b) downhill\nYour decision: ")
        if starting_path == "b":
            print("\nAs you descend, you're able to see far below and admire the beauty of the landscape and the vast canyon below.")
            input("It all seems so raw and untouched, as if humans have never been here to exploit it and spoil it.")

            print("\nSoon, you reach flat ground in the forest and lose sight of the canyon. After a brief walk, you reach a deserted")
            print("gravel road. Looking left, you can seen the sun setting over the road which heads toward the canyon. To your right,")
            input("the road bends around the mountainside, and you can't see where it goes.")

            print("\nWhere do you go next?")
            # Decision - ROAD RIGHT, GO BACK, ROAD LEFT
            while True:
                downhill_options = ["(a) Go right and walk along the road", "(b) Retrace your steps uphill", "(c) Go left and walk along the road"]
                for text in downhill_options:
                    print(text)
                downhill = input("Your decision: ")
                if downhill != "a" and downhill != "b" and downhill != "c":
                    print("\n >> Invalid Action <<\n")
                    continue
                if downhill == "b":
                    starting_path = "a"
                    break
                if downhill == "a":
                    # Game Stage - Rockslide
                    input("\n-- Rockslide --")
                    print("As you walk around the bend, the sun gets blocked out by the mountain and it gets dark quickly. Up ahead, you see")
                    input("a massive rockslide that blocks the road. You could try to climb over it, but you can't see what's on the other side.")
                    # Decision - ROAD LEFT, CLIMB
                    while True:
                        rockslide = input("\nWhat do you do?\n(a) Walk back the other way\n(b) Climb\nYour decision: ")
                        if rockslide != "a" and rockslide != "b":
                            print("\n >> Invalid Action <<")
                            continue
                        elif rockslide == "a":
                            downhill = "c"
                            break
                        elif rockslide == "b":
                            print("\nYou begin the climb, which is near vertical in some parts and extremely tiring. Just as you near the top,")
                            input("your excitement to see what lies beyond gets the better of you and you hastily pull yourself upwards on a loose rock.")
                            input("\nThe rock falls, tumbles violently down the rockslide, and into the canyon below - and so do you.")
                            respawn_rockslide = death()
                            return respawn_rockslide
                if downhill == "c":
                    print("\nAfter hours of walking, fatigue sets in. There is nothing along this road and nobody here. You consider")
                    print("backtracking, but you've already come too far. The canyon walls towering over the road get higher and higher")
                    input("as the sun sets. You can't see what's ahead and can't remember what was behind you.")

                    print("\nSoon, all sources of light cease to exist. The darkness confuses you, and you stray from the road")
                    input("and stumble into a ditch.")

                    print("\nThe temperature drops, hypothermia sets in and just as your consciousness fades, you get a vision")
                    print("of a figure approaching you. You struggle to get a better look, and see that the figure is")
                    input("skeleton rising from the floor of a house, coming towards you.")
                    respawn_downhill = death()
                    return respawn_downhill
        if starting_path == "a":
            break
        else:
            print("\n >> Invalid Action <<")

    print("\nAfter a long trek uphill, you make it to a new clearing on the mountain,")
    input("and in the center sits a temple, hidden beneath the forest canopy.")
    
    # Game Stage - House of Ancestors
    input("\n-- House of Ancestors --")
    print("In the twilight, you walk towards the temple. The answers you need are likely hidden with whatever lies inside,")
    input("and you intend to find them one way or another.")

    input("\nEntering the doorway, you see a wooden staircase leading upstairs. You consider where to look first.")
    temple_options = ["(a) Explore the first floor", "(b) Go upstairs", "(c) Check near the doorway"]
    # Decision - FIRST FLOOR, UPSTAIRS, CHECK BEHIND
    while True:
        print("\nPick a place to look: ")
        for text in temple_options:
            print(text)
        explore = input("Your decision: ")
        if explore == "a" and "(a) Explore the first floor" in temple_options:
            temple_options.remove("(a) Explore the first floor")
            print("\nOn the far side of the room, there are inscriptions on the wall. The worn text")
            input("is hard to read in the fading light, but you make out a few words.")
            
            print("\nIt says the poison was buried with the one who created it to prevent others from finding what")
            print("no one should have. It also says something about requiring the permission of the ancestors to receive it,")
            input("and risking death if they disapprove. What poison are they talking about?")
        elif explore == "b" and "(b) Go upstairs" in temple_options:
            temple_options.remove("(b) Go upstairs")
            print("\nProceeding up the creaky staircase, you find coffins lined against the wall. Each one is nailed shut")
            print("and has a unique marking in the wood. You walk along the coffins, examining each marking as you try to")
            print("piece together what they mean. Upon inspecting the last coffin, you see that the marking here is a pine")
            input("tree. Intruiged that the marking is identical to the one on your wrist, you look closer.")
            
            print("\nAs you lean forward, the rotting wood floor gives way and both you and the coffin fall,")
            input("crashing hard onto the floor below in a cloud of dust.")
            
            print("\nThe fall destroys the coffin, and you find yourself lying on top of an exposed skeleton in a")
            print("pile of dust, dirt, and broken bones. Unhurt but shaken, you get up and feel pity for the")
            input("remains of the past life you see before you. You wonder what the pine marking has to do with you.")
        elif explore == "c" and "(c) Check near the doorway" in temple_options:
            temple_options.remove("(c) Check near the doorway")
            print("\nOn the walls next to the doorway, you see symbols and drawings that appear to be warnings.")
            print("There are images of death in various forms, but the one image that is not death is a drawing")
            input("of a person holding their right hand out, palm upward. Interestingly, this person appears at peace.")
            
            input("\nThis drawing does not match the others, which makes you think there must be something important about it.")
        else:    
            print("\n >> Invalid Action <<")
            continue
        if not temple_options:
            break
    
    # Game Stage - The Figures
    print("\nBefore you can finish your thoughts, the room suddenly goes cold. The temperature drops almost instantly,")
    input("and you hear a quiet rustling behind you.")

    print("\nYou turn around and find yourself standing face to face with a frightening, spectral figure. The figure")
    print("blocks your path to the doorway, yet the doorway is still slightly visible through the figure. You freeze,")
    input("as there is a face on this figure, something resembling a young woman. She stares at you as you stand frozen.")

    print("\nNot knowing what to do, you stay still and wait for her next move. Her eyes then look above you, and you")
    print("see multiple other figures come from the wall behind you. More than ten of the ghostly figures form")
    input("a semicircle with the woman around the wall, blocking off any form of escape for you.")

    print("\nShe looks at each of them slowly, and each figure in turn studies you. As the woman turns her head,")
    print("you notice more of her facial features and can't help but think that she looks familiar. The air is still")
    print("freezing, but you're not scared anymore. Something about this place makes you feel nostalgic, and it")
    input("almost feels nice to be here.")

    print("\nThe woman eventually nods, and one by one all the figures fade into dust, disappearing from the temple.")
    print("In her place, you now see a wooden cup with a lid on the ground. All alone now, you pick up the cup and")
    print("lift the lid, revealing a black, viscous liquid inside. Unsure of what to do, you go back to the drawings")
    input("in the doorway for hints.")
    
    print("\nNone of the images of death have anything to do with drinking liquid, which reassures you.")
    print("Remembering that you have the same pine marking as one of the ancestors in the coffin, you feel")
    input("a sense of belonging and that this cup must have been intended for you.")

    # Decision - DRINK or DON'T DRINK
    while True:
        drink = input("\nWhat do you do with the cup?\n(a) Dip your finger in the liquid to see what it could be\n(b) Drink it\nYour decision: ")
        if drink != "a" and drink != "b":    
            print("\n >> Invalid Action <<")
            continue
        elif drink == "a":
            print("\nA little worried about what the drink might do, you try dipping your index finger in it first.")
            input("Immediately, the substance on your finger begins to expand and starts engulfing your entire arm.")

            print("\nNow in complete panic, you drop the cup, which spills on the ground, and try to wipe off the")
            print("substance with your other hand. This instantly spreads it onto your other arm. Unbeknownst to")
            input("you, the substance has started spreading on the floor now, turning the floor black as well.")

            print("\nJust as you realize what's happening to the floor, you suddenly feel yourself begin to fall.")
            print("The darkness of the floor created by the substance had become a hole, which fully immerses you as")
            input("you get sucked into oblivion.")

            respawn_drink = death()
            return respawn_drink
        elif drink == "b":
            input("\nYou drink the cup, which is tasteless. Nothing happens.")
            
            print("\nYou inspect the drawings one more time, with your attention again on the peaceful figure with an")
            input("outstretched palm. Curious as to what it means, you make the gesture as well.")

            print("\nAnd with that, the substance begins to take effect. Your vision blurs as you notice your surroundings")
            print("disappear in a manner that feels like they're getting sucked away behind you. Images of places and")
            print("people flash before you and you get the sensation that you're traveling at high speed, but you're going")
            print("too fast to make sense of what you're seeing. You could be getting taken to a far distance place")
            input("on Earth, or perhaps through time.")

            input("\nThen everything comes screeching to a halt as your vision goes black.")

            print("\nSlowly, you start to see light. Your vision clears and you see two people in the distance")
            input("walking through the vast, untouched landscape.")

            print("\nYou recognize the person closer to you as the woman from before, but alive and well. Walking alongside")
            print("her is someone you can't get a good look at. You can't tell if they know you're there, but get closer for")
            input(" a better look. Out in the open now, the woman sees you and waves.")

            input("\nThe second person turns to look at you too, and it's the last person you're expecting.")

            input("\nThe person is you - a younger you. ")
            
            input("\nThe two of them look away, and continue on their walk.\n")
            return False

welcome_message = """
> You wake up and find yourself in an unfamiliar place. Explore your surroundings to gain clues about your situation.
> Without learning more about what this place is, you may never get out. You've lived this dream before. Recollect
> the events and uncover the clues to escape."""

end_message = """>
> End of game.
>"""

if __name__ == "__main__":
    gameplay = True
    mixer.init()                    # Instantiate mixer
    # Load audio file - must specify path in one of these formats for Python (different than Windows)
    #   r'C:\Users\expoperialed\Desktop\Python'         specify raw string
    #   'C:\\Users\\expoperialed\\Desktop\\Python'      use double backslash
    #   'C:/Users/expoperialed/Desktop/Python'          use single forward slash - may be able to use double forward slash too
    mixer.music.load(r'C:\Users\justi\Desktop\Python\DreamGame\soundtrack.mp3')
    mixer.music.set_volume(0.8)     # Set volume
    mixer.music.play(-1)            # Number of *repeats*: (1) for 1 repeat aka 2 plays, () for 0 repeats, -1 for infinite loop
    while gameplay == True:        
        gameplay = main(welcome_message)
    print(end_message)
    mixer.music.stop()