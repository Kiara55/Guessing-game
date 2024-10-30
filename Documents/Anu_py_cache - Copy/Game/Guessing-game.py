import random
name = input("Input Name: ")
print("Hi,", name , '\n', "WELCOME TO THE GUESSING GAME, LET'S PLAY :)")

print("I have a number in mind, can you guess it:")

num = random.randint(1, 100)
attempts = 0
max_attempts = 3

choice_1 = int(input("Attempt 1: "))
attempts += 1

if choice_1 < 1:
    print("The number is too low")
elif choice_1 > 100:
    print("The number is too high")
else:
    if choice_1 == num:
        print(f"CONGRATULATIONS {name}! YOU GUESSED IT ON YOUR FIRST ATTEMPT!")
        attempts = max_attempts
    else:
        print("Wrong guess!")

if attempts < max_attempts:
    choice_2 = int(input("Attempt 2: "))
    attempts += 1
    
    if choice_2 < 1:
        print("The number is too low")
    elif choice_2 > 100:
        print("The number is too high")
    else:
        if choice_2 == num:
            print(f"CONGRATULATIONS {name}! YOU GUESSED IT ON YOUR SECOND ATTEMPT!")
            attempts = max_attempts
        else:
            print("Wrong guess!")

if attempts < max_attempts:
    choice_3 = int(input("Attempt 3: "))
    attempts += 1
   

    if choice_3 < 1:
        print("The number is too low")
    elif choice_3 > 100:
        print("The number is too high")
    else:
        if choice_3 == num:
            print(f"CONGRATULATIONS {name}! YOU GUESSED IT ON YOUR THIRD ATTEMPT!")
        else:
            print(f"SORRY {name}, YOU DIDN'T GUESS IT CORRECTLY! THE NUMBER WAS {num}. TRY AGAIN NEXT TIME!!!")