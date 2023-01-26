print("Welcome to my computer quiz!")
playing = input("Do you want to play?\n")

def game():
    if playing != "yes":
        quit()
    print("Ok! Let's play :)")

    score = 0

    answer = input("What is the color of sun?\n")
    if answer.lower() == "yellow":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("Which one is faster? A tiger or a dog?\n")
    if answer.lower() == "tiger":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What currency we use in Europe? Dollar, euro or yen?\n")
    if answer.lower() == "euro":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("How many wheels does a car have?\n")
    if answer.lower() == "four" or answer.lower() == "4":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print(f"You got {score} questions corrects, {(score / 5) * 100:.0f}% of quiz.")

    keep_playing = input("Do you wanna play again?\n")

    if keep_playing == "yes":
        game()
    else:
        quit()
game()
