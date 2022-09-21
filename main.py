import MainMenuMethods
import SoccerTicker

if __name__ == '__main__':
    welcome = str(MainMenuMethods.welcome_print("Welcome :)"))
    print(welcome)
    print("-------------------------------------------------------")
    MainMenuMethods.sleep_after_interaction(0.2)
    print("This is my first terminal-based Python Project")
    MainMenuMethods.sleep_after_interaction(0.2)
    print("-------------------------------------------------------")
    MainMenuMethods.sleep_after_interaction(1)
    MainMenuMethods.start_selected_progress()
