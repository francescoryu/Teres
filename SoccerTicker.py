from __future__ import print_function

import random
import sys
import time
from random import randint
import MainMenuMethods

__author__ = "Francesco Ryu"
__date__ = "2022/09/21"
__Version__ = "0.1"


def soccer_ticker():
    team1_result = randint(1, 5)
    team2_result = randint(1, 5)

    print("----------------------------------------")
    print("Soccer Simulator")
    print("----------------------------------------")

    print("Teamname 1: ")
    teamname1_input = input()

    print("Teamname 2: ")
    teamname2_input = input()
    print("----------------------------------------")
    print("type 's' to start or 'c' to change teamnames: ")
    selection_input = str(input())

    while selection_input == "c":
        print("----------------------------------------")

        print("Teamname 1: ")
        teamname1_input = input()

        print("Teamname 2: ")
        teamname2_input = input()

        print("----------------------------------------")
        print("type 's' to start or 'c' to change teamnames: ")
        selection_input = str(input())
        print("----------------------------------------")
    MainMenuMethods.loading_effect()

    converted_team1_result = str(team1_result)
    converted_team2_result = str(team2_result)

    score = (teamname1_input) + " " + converted_team1_result + " : " + converted_team2_result + " " + teamname2_input + "\n"

    MainMenuMethods.sleep_after_interaction(0.5)
    print("----------------------------------------")
    print(score + "\n")
    print("----------------------------------------")
