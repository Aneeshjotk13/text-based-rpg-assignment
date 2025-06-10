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
        
ans2 = input("Your answer: ").lower().strip() :
    if ans2 == "a":
        print("He grabs the food and water from you and starts eating wildly.After finishing it,he said,\"You have a good heart… because you helped me, I will grant you one wish. Anything your heart desires.\"You are amused by what the old man said and don’t know how to react?After thinking for a while you asked him\,”Are you kidding me?\”He said\,” No I am not kidding with you.It's real.\”Before making your wish, you ask\: “Who are you really?\”He smiles, and time pauses.\“Few ever ask that. Most just wish.\”He tells you that he can’t tell you who he really is.Finally you believe him and tell him that you want to be a superhero in real life.He asks you and gives you two options that what kind of superhero you want to be ?")
                