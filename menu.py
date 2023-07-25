import os
import sapper_game


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu(menu_items, selected_item):
    clear_screen()
    print("Добро пожаловать в игру 'Cапер'. Давайте взорвем всех врагов.")


    while True:
        for i, item in enumerate(menu_items):
            if i == selected_item:
                print("\033[33m>", item, "\033[0m")
            else:
                print(" ", item)

        key = input()
        if key == "w":
            selected_item = (selected_item - 1)
        elif key == "s":
            selected_item = (selected_item + 1)
        elif key == " ":
            size, mines = menu_items[selected_item].split(" ")[0].split("x")
            size = int(size)
            mines = int(mines)
            sapper_game.getparams(size, mines)

def mainMenu():
    menu_items = ["5x5 (5 mines)", "10x10 (10 mines)", "15x15 (15 mines)"]
    selected_item = 0

    while True:
         print_menu(menu_items, selected_item)
         key = input()

         if key == "w":
             selected_item = (selected_item - 1)
         elif key == "s":
             selected_item = (selected_item + 1)
         elif key == " ":
             size, mines = menu_items[selected_item].split(" ")[0].split("x")
             size = int(size)
             mines = int(mines)
             sapper_game.getparams(size, mines)
