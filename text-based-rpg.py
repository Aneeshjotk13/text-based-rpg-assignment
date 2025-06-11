# Text based rpg: One wish away
# Welcome user to the game and ask their name
name = input("Welcome to One wish away! Get ready your journey begins now.")
print(f"Hi {name}! Wishing you have a delightful gaming experience.Here we go....")

# Describe the game.
# Describe the starting scene.
print("You are a person who always daydreams a lot to become a superhero in real life.One day, you were walking home from school and accidentally noticed an old man who was poorly lying on the floor.")
print("What do yo do?")
print("a) Approach the man carefully.")
print("b) Ignore him and walk away.")
ans1 = input("Your answer: ").lower().strip()

# Check their answer.
if ans1 == "a":
    print("You knelt beside and asked him that \"What do you want?\".He opens his eyes slowly and begs you for water.")
    print("Now what will you do? ")
    print("a) Give him some food and water.")
    print("b) Leave him behind.")
    ans2 = input("Your answer: ").lower().strip() 

    if ans2 == "a":
        print("He grabs the food and water from you and starts eating it wildly.")
        print("After finishing it,he said,\"You have a good heart...because you helped me, I will grant you one wish.Anything your heart desires.")
        print("You are amused by what the old man said and don't know how to react ?")
        print("After thinking for a while you asked him,\"Are you kidding me?\"")
        print("He said,\"No,i am not kidding with you.It's real.\"")
        print("Before making your wish, you ask\: “Who are you really?\”")
        print("He smiles, and time pauses.Few ever ask that. Most just wish.")
        print("He tells you that he can’t tell you who he really is?")
        print("Finally you believe him and tell him that you want to be a superhero in real life.")
        print("He asks you what kind of superhero you want to be ?")
        print("He gives you two options:-")
        print("a) Superman")
        print("b) Spiderman")
        ans3 = input("Your answer: ").lower().strip()
        
        if ans3 == "a":
            print("A golden light surrounds you. Heat surges through your chest. You scream—not in pain, but in awakening.")
            print("When you open your eyes, you’re floating inches off the ground.")
            print("You find a small envelope tucked under the door of your secret hideout. Inside is a crumpled letter from a little girl named Sara:-")
            print("\"Dear Superman,My mommy hasn’t come home in three days. I’m scared. Please help her. I believe you can\".")
            print("Your super hearing picks up faint whispers coming from the old subway tunnels beneath the city. Sara’s mother might still be alive.")
            print("What do you want to do?")
            print("a) Go in quietly to gather evidence and call the police for backup.")
            print("b) Break in now and rescue Sara's mom and other people immediately.")
            print("c) Use super hearing to eavesdrop and identify key criminals before making a move.")
            ans4 = input("Your answer: ").lower().strip()
            
            if ans4 == "a":
                print("You move carefully, trying to stay unseen. But the bad guys notice you before you can finish. They surround you and attack suddenly. You get hurt badly, and it takes a long time for the police to arrive.")
                print("Because of the delay, some people don’t make it out safely. You feel terrible for not acting faster, and it weighs on your heart.")
                print("After sometime,a bomb blasts and many people die including Sara’s mom.")
                
            elif ans4 == "b":
                print("You don’t hesitate. Time is running out. With a burst of super strength, you smash through the tunnel entrance and rush inside.")
                print("Explosions shake the walls, and smoke fills the air. You shield the hostages from debris and carry them out one by one.")
                print("Though you feel the sting of pain from the blast, your heart swells knowing you saved lives today. The grateful faces of those you rescued remind you why you chose this path.")
                print("To find Sara’s mom,you look for her but still you can’t find her, then after a moment you figure out she is sitting in a corner.")
                print("Now what question do you ask her?")
                print("a) What are you doing here?")
                print("b) Are you Sara’s mom ?")
                ans5 = input("Your answer: ").lower().strip()

                

