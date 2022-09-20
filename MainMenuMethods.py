import time



def sleep_after_interaction(x):
    time.sleep(x)

def get_input():
    menu_selection_input = input()
    print("You selected: " + menu_selection_input)
