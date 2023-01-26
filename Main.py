print("Welcome to my computer quiz!")

playing = input("Do you want to play?\n")
def game():

    if playing != "yes":
        quit()
    print("Ok! Let's play :)")

    answer = input("What is the color of sun?\n")
    if answer.lower() == "yellow":
        print("Correct!")
    else:
        print("Incorrect!")

    answer = input("Which one is faster? A tiger or a dog?\n")
    if answer.lower() == "tiger":
        print("Correct!")
    else:
        print("Incorrect!")

    answer = input("What currency we use in Europe? Dollar, euro or yen?\n")
    if answer.lower() == "euro":
        print("Correct!")
    else:
        print("Incorrect!")

    answer = input("How many wheels does a car have?\n")
    if answer.lower() == "four" or answer.lower() == "4":
        print("Correct!")
    else:
        print("Incorrect!")

    keep_playing = input("Do you wanna play again?\n")
    if keep_playing == "yes":
        game()
    else:
        quit()

game()