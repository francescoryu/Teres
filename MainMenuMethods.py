import webbrowser
from datetime import datetime
from random import randint
import time

__author__ = "Francesco Ryu"
__date__ = "2022/09/21"
__Version__ = "0.1"

def sleep_after_interaction(x=float):
    time.sleep(x)


def start_selected_progress():
    selection_number = int
    while selection_number != 4:
        print("-----------------------------------")
        sleep_after_interaction(0.2)
        print("|Choose from an option you like")
        sleep_after_interaction(0.2)
        print("___________________________________")
        sleep_after_interaction(0.2)
        print("|1 for random number\n"
              "|2 for current date and time\n"
              "|3 to open google\n"
              "|4 to exit")
        sleep_after_interaction(0.2)
        print("-----------------------------------")

        selection_number = int(input())

        if selection_number == 1:
            print("minimum Number: ")
            min_num = int(input())
            print(min_num)
            print("maximum Number: ")
            max_num = int(input())
            print(max_num)
            ran_num = randint(min_num, max_num)
            print("-------------------------------------")
            print("Your Number is: " + str(ran_num))
            print("-------------------------------------")
            sleep_after_interaction(0.2)

        if selection_number == 2:
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Currently: ", dt_string)
            sleep_after_interaction(0.2)

        if selection_number == 3:
            webbrowser.open("https://google.com")
            print("Link opened")

        if selection_number == 4:
            print("Bye, have a great day!")
            break
