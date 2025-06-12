# Text based rpg: One wish away
# Welcome user to the game and ask their name
name = input("Welcome to One wish away! What is your name? ")
print(f"Hi {name}! Are you ready to explore your destiny so lets get started...\n")

# Start the game
print("You are a person who always daydreams a lot to become a superhero in real life.One day, you were walking home from school and notice an old man lying on the ground.")
print("Now what will you do?")
print("[A]pproach the man carefully.")
print("[I]gnore him and keep walking.")
ans1 = input("Your answer: ").lower().strip()

# Check their answer.
if ans1 == "a":
    
    print("You kneel beside him. He opens his eyes slowly and begs for food and water.")
    print("What will you prefer to do? ")
    print("[G]ive him food and water.")
    print("[L]eave him behind.")
    ans2 = input("Choice: ").lower().strip()
   
    if ans2 == "g":
        print("He grabs the food and eats wildly.")
        print('"You have a good heart," he says. "I will grant you one wish. Anything you desire."')
        print("[B]ecome a superhero.")
        print("[R]eject the offer.")
        ans3 = input("Choice: ").lower().strip()   
           
        if ans3 == "b":
            print("He asks: What kind of superhero do you want to be?")
            print("[S]uperman")
            print("[SP]iderman")
            ans4 = input("Choice: ").lower().strip()
            
            if ans4 == "s":
                print("A golden light surrounds you. You awaken as Superman.")
                print("You find a letter: 'Dear Superman, my mommy hasn’t come home in 3 days.'")
                print("You hear whispers from an old subway tunnel.")
                print("[B]reak in and rescue the people immediately.")
                print("[Q]uietly go in and call the police.")
                print("[H]ear the criminals using your super hearing.")
                ans5 = input("Choice: ").lower().strip()
                
                if ans5 == "b":
                    print("You smash in and rescue hostages. You spot a woman sitting in the corner.")
                    print("Do you ask:")
                    print("[A] 'Are you Sara’s mom?'")
                    print("[W] 'Why are you sitting in a corner not on the chair?'")
                    ans6 = input("Choice: ").lower().strip()
                    
                    if ans6 == "a":
                        print('"Yes, I am," she says with teary eyes.')
                        print('"Your daughter is waiting for you," you say. "She sent me to save you."')
                        print("You bring her home. Sara hugs her mom and calls you her hero.")
                        print("She gives you a small flower. 'We’re all counting on you,' she says.")
                        print("You fly into the sunset, feeling proud and renewed.")
                    elif ans6 == "w":
                        print("She becomes furious and refuses to answer.")
                    else:
                        print("Invalid choice! Please restart the game and choose a valid option.")
                        
                elif ans5 == "q":
                    print("You wait too long. The bad guys notice you. Sara's mom doesn't make it out.")
                elif ans5 == "h":
                    print("You try listening but fall into a trap. You’re badly injured. The hostages are moved.")
                else:
                    print("Invalid choice! Please restart the game and choose a valid option.")
                    
            elif ans4 == "sp":
                print("You wake up with powers. Later, Aunt May tells you Uncle Ben was shot.")
                print("You remember the thief you let go earlier.")
                print("[C]hase the thief.")
                print("[S]tay with Aunt May.")
                print("[P]hone the police.")
                ans7 = input("Choice: ").lower().strip()

                if ans7 == "c":
                    print("You catch the thief. It's the one you let go. It's not satisfying. You feel guilty.")
                elif ans7 == "s":
                    print("You stay with Aunt May. You both cry together. Family first.")
                elif ans7 == "p":
                    print("You call the police. They catch the thief. But it gives you no peace.")
                else:
                    print("Invalid choice! Please restart the game and choose a valid option.")
                    
        elif ans3 == "r":
            print("Oops! You lost a great opportunity.")
        else:
            print("Invalid choice! Please restart the game and choose a valid option.")

    elif ans2 == "l":
        print("Be generous to help others.")
    else:
        print("Invalid choice! Please restart the game and choose a valid option.")

elif ans1 == "i":
    print("You ignored a person in need. Sadly, that wasn't a very good choice.")
else:
    print("Invalid choice! Please restart the game and choose a valid option.")

print("Thanks for playing!")
                    
                    
                    
                    
