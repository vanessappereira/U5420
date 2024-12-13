"""
Problem Definition: 
Guessing game program. The user must guess a number and has several attempts to do so.

Problem Description: 
The program starts by generating a random number between 0 and 20. Then it asks the user to try to guess. If the user guesses correctly, the program ends. If not, the program indicates the proximity of the attempt and asks for a new attempt.

Input Data:
    num_magico -> random number between 0 and 20, int obtained with random.randint
    num -> number entered by the user (attempt), int

Output Data: Displays the following on the standard output:
    Correct -> if the user guessed correctly
    Close -> if within 3 values of the "distance"
    Very close -> if within 1 value of the "distance"
"""

from random import randint


def magicCube1():
    magic_number = randint(0, 20)
    distance = -1
    while distance != 0:
        num = int(input("Guess a number between 0 and 20: "))
        distance = abs(magic_number - num)
        if distance == 0:
            print("Correct!")
        elif distance <= 1:
            print("Very close!")
        elif distance <= 3:
            print("Close!")
        else:
            print("Far away!")
            print("Do you want to play again? (yes/no): ")
            if input() == "yes":
                magicCube1()
            else:
                break


def magicCube2():
    magic_number = randint(0, 30)
    DIFF_CLOSE = 2
    DIFF_VERYCLOSE = 1
    while True:
        num = int(input("Guess a number between 0 and 30: "))
        distance = abs(magic_number - num)
        if distance == 0:
            print("Correct!")
        elif distance <= DIFF_VERYCLOSE:
            print("Missed, but you are _very_ close!")
        elif distance <= DIFF_CLOSE:
            print("Missed, but you are close!")
        else:
            print("Missed.")
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again == "yes":
                magicCube2()
            else:
                break


def main():
    magicCube1()


if __name__ == "__main__":
    main()
