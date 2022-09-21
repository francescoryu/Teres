import random
import sys
import webbrowser
from datetime import datetime
from random import randint
import time

__author__ = "Francesco Ryu"
__date__ = "2022/09/21"
__Version__ = "0.1"

import SoccerTicker


def sleep_after_interaction(x=float):
    time.sleep(x)


def start_selected_progress():
    SoccerTicker.soccer_ticker()


def loading_effect():
    for cntr in range(91):
        converted_cntr = str(cntr)
        sys.stdout.write("\r-----------------" + converted_cntr + "min played-----------------")
        sleep_after_interaction(0.15)
        cntr + 1


def welcome_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.20)
