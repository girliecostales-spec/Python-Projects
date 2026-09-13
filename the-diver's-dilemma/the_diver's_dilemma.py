print(r'''
                      )    O
                           (   o . O
                            )   () .
                           /  O   o
                         _.|._ o .()
              _         / _:_ \
             <_><)     |.(_"_).|
                __     _\. : ./_
             |><_'>   / |..:..| \
                     /_/ `---' \_\       ,
             ,  (.   \_)        \_)  \)-<
             _) \)~    \   T   /    ,(_)
            _/ -(-<    _)__|__(_    \_)-<~
             \)~ )-<  /....|....\  .~(_,_
            >(_ (_/   """"" """""    _\
         `-.__)__\_.----'`-.______.-'  `-.__
                                                hjw

''')
print("The Deep Diver's Dilemma")
print("Choose Your Own Adventure Game \n")
print("How to Play:")
print("Read each situation and type the word for your chosen action. Your choices will determine how the adventure ends! \n")
c=input(
    "You and your friend are diving when a strong current sweeps your friend away. \n" 
    'Type "return" to return to the boat. \n'
    'Type "follow" to follow your friend. \n' 
    'Type "wait" for the current to weaken. \n'
)
if c.strip().lower() == "follow":
    c_f=input(
        "The current carries you away. You see a faint light. \n" 
        'Type "approach" to approach it. \n'
         'Type "surface" to swim upward. \n' 
         'Type "avoid" to avoid it. \n'
    )
    if c_f.strip().lower() == "surface":
        c_f_s=input(
            "The current disorients you and pushes you toward the ocean floor. You see a sunken ship, a giant clam and the source of a strange noise.\n"
            'Type "ship", "clam" or "noise". \n'
        )
        if c_f_s.strip().lower() == "ship":
            c_f_s_s=input(
                "You find the lost ship of the pirate Virgilio Dela Rosa. Its hold is filled with treasure. \n" 
                'Type "yes" to take it. Type "no" to leave it. \n'
            )
            if c_f_s_s.strip().lower() == "no":
                print(
                    "You photograph the wreck and return safely. Your pictures are published in National Geographic. \n"
                    "YOU WIN! \n"
                )
            else:
                print(
                    "The treasure slows you down, and your oxygen runs out. \n" 
                    "GAME OVER \n"
                )
        elif c_f_s.strip().lower() == "clam": 
            c_f_s_c=input(
                "Something glimmers beside the clam. \n" 
                'Type "inspect" to examine it. \n' 
                'Type "ignore" to leave it alone. \n'
            )
            if c_f_s_c.strip().lower() == "inspect":
                c_f_s_c_i=input(
                    "You discover an unusual golden coin. \n" 
                    'Type "take" to keep the coin. \n' 
                    'Type "leave" to leave it behind. \n'
                )
                if c_f_s_c_i.strip().lower() == "take":
                    c_f_s_c_i_t=input(
                        "You keep the coin, then see fish and turtles. \n" 
                        'Type "fish" or "turtle". \n'
                    )
                    if c_f_s_c_i_t.strip().lower() == "turtle":
                        c_f_s_c_i_t_t=input(
                            "The turtles lead you to your friend, who is trapped among jellyfish. \n" 
                            'Type "yes" to rescue your friend. Type "no" to escape. \n'
                        )
                        if c_f_s_c_i_t_t.strip().lower() == "yes":
                            print(
                                "You rescue your friend, and both of you return safely. You sell the valuable coin and become rich. You also receive an award for your bravery. \n" 
                                "YOU WIN! \n"
                            )
                        else:
                            print(
                                "You try to escape, but the jellyfish trap you too. \n"
                                "GAME OVER \n"
                            )
                    else:
                        print(
                            "Fishermen catch you in their net and rescue you. You sell the valuable coin and become rich. \n"
                            "YOU WIN!"
                        )
                else:
                    c_f_s_c_i_l=input(
                        "You see a school of fish and a bale of turtles. \n"
                        'Type "fish" or "turtle". \n'
                    )
                    if c_f_s_c_i_l.strip().lower() == "fish":
                        print(
                            "You are caught with the fish in a net. The fishermen pull you to safety. \n" 
                            "YOU SURVIVE! \n")
                    else:
                        print(
                            "The turtles lead you into a bloom of jellyfish. You become trapped, and your oxygen runs out. \n" 
                            "GAME OVER \n"
                        )
            else:
                print(
                    "You stay too long, and your oxygen runs out.\n" 
                    "GAME OVER \n"
                )
        else:
            c_f_s_n=input(
                "The noise comes from a research submarine. \n" 
                'Type "signal" to signal with your light. \n' 
                'Type "knock" to knock on its window. \n'
            )
            if c_f_s_n.strip().lower() == "signal":
                print(
                    "The submarine crew rescues you. You later publish a bestselling book about your adventure. \n" 
                    "YOU WIN! \n"
                )
            else:
                print(
                    "You frighten the pilot, and the submarine leaves. Your oxygen runs out. \n" 
                    "GAME OVER \n")
    elif c_f.strip().lower() == "avoid":
        c_f_a=input(
            "You swim away and realize the light belongs to a cookiecutter shark. Ahead, you see turtles and a coral reef. \n" 
            'Type "turtle" or "reef". \n'
        )
        if c_f_a.strip().lower() == "turtle":
            print(
                "The turtles lead you to an island. A conservation team finds you several days later. \n" 
                "YOU SURVIVE! \n"
            )
        else:
            c_f_a_r=input(
                "You find a giant oyster with a glimmering pearl. \n" 
                'Type "take" to take it. Type "leave" to leave it. \n'
            )
            if c_f_a_r.strip().lower() == "take":
                print(
                    "A current carries you to the surface, where a research vessel rescues you. The rare pearl makes you famous. \n" 
                    "YOU WIN!\n"
                )
            else:
                print(
                    "A current carries you to the surface. Fishermen rescue you and eventually help you return home. \n" 
                    "YOU SURVIVE \n")
    else: 
        print(
            "The light belongs to a cookiecutter shark! It bites your equipment and damages your oxygen tank. \n" 
            "GAME OVER \n")
elif c.strip().lower() == "wait":
    c_w=input(
        "You wait until the current weakens. A shadowy figure approaches. \n" 
        'Type "approach" to swim toward it. \n'
        'Type "avoid" to swim away. \n'
    )
    if c_w.strip().lower() == "approach":
        c_w_a=input(
            "The figure is a rescue diver. He asks what you would like to do. \n" 
            'Type "return" to return to the boat. \n' 
            'Type "search" to help search for your friend. \n'
        )
        if c_w_a.strip().lower() == "search":
            c_w_a_c=input(
                "You find your friend unconscious and tangled in seaweed. \n" 
                'Type "call" to call the rescue team. \n' 
                'Type "rescue" to free your friend yourself.\n'
            )
            if c_w_a_c.strip().lower() == "call":
                print(
                    "The team frees your friend. After medical treatment, both of you return home. \n"
                     "YOU BOTH SURVIVE! \n"
                )
            else:
                c_w_a_c_t=input(
                    "You free your friend, but your oxygen is almost gone. \n" 
                    'Type boat to "swim" directly to the boat. \n' 
                    'Type "team" to return to the rescue team. \n'
                )
                if c_w_a_c_t.strip().lower() == "team":
                    print(
                        "The team gives your friend an extra oxygen tank and escorts you to safety. You become famous for your bravery. \n" 
                        "YOU WIN! \n"
                    )
                else:
                    print(
                        "Your oxygen runs out, but the rescue team finds you in time. \n"
                        "YOU BOTH SURVIVE! \n"
                    )
        else:
            print(
                "You return safely, but your friend is never found. You later write a book in your friend’s memory. \n"
                "THE END \n"
            )
    else:
        print(
            "You realize too late that the figure was a rescue diver. Fortunately, the team finds your flotation device and rescues you, but your friend remains missing. \n" 
            "YOU SURVIVE \n"
        )
else:
    print(
        "You reach the boat safely, but people suspect you caused your friend’s disappearance. \n"
         "GAME OVER \n")