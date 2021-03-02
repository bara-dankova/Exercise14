# import modules
from random import randint

# define function with no parameters
def rps():
    # ask user for input and make sure they enter one of the three options
    human = input("Please enter R for ROCK, P for PAPER or S for SCISSORS: ")
    while not human in ["R", "P", "S"]:
        human = input("Please enter R for ROCK, P for PAPER or S for SCISSORS: ")
    # initialize a variable for the computer's choice
    computer = ""
    # generate a random number between 0 and 2 (both limits are inclusive)
    n = randint(0,2)
    # translate generated number into a string to correspond to human choices
    if n == 0:
        computer = "R"
    if n == 1:
        computer = "P"
    if n == 2:
        computer = "S"
    # use if-statements to define when user wins or loses according to the logic of the game
    if computer == "R" and human == "P":
        print("The computer chose ROCK, you WIN!")
    if computer == "R" and human == "S":
        print("The computer chose ROCK, you LOSE!")
    if computer == "P" and human == "S":
        print("The computer chose PAPER, you WIN!")
    if computer == "P" and human == "R":
        print("The computer chose PAPER, you LOSE!")
    if computer == "S" and human == "R":
        print("The computer chose SCISSORS, you WIN!")
    if computer == "S" and human == "P":
        print("The computer chose SCISSORS, you LOSE!")
    # if both the user and the computer pick the same option, it is a draw
    if computer == human:
        print("Both you and the computer chose the same, it's a draw!")

# call the function
rps()

# this is just to make sure that the program doesn't close immediately when run in a proper command line (not PyCharm)
input()




