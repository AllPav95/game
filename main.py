import sapper_game
import sys
import menu

def main():
    menu.main()

if __name__ == '__main__':

     if len(sys.argv) == 3:
        size = int(sys.argv[1])
        mines = int(sys.argv[2])
        sapper_game.startGame(size, mines)
     else:
         print("Usage: python sapper_game.py <size> <mines>")