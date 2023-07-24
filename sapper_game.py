import random
import sys

def startGame(size, mines):
    rows = int(size)
    print("\033[34m      Добро пожаловать в игру 'Cапер'               Давайте взорвем всех врагов\033[0m")

    player_field = []
    for _ in range(rows):
        row = ['\033[32m*\033[0m'] * rows
        player_field.append(row)

    mines_field = []
    for _ in range(rows):
        row = ['\033[32m \033[0m'] * rows
        mines_field.append(row)

    mines = 0
    while mines < rows-1:
        x = random.randint(0, rows-1)
        y = random.randint(0, rows-1)
    if mines_field[x][y] != '\033[32m&\033[0m':
        mines_field[x][y] = '\033[32m&\033[0m'
        mines += 1
        print('\033[32m   ' + '   '.join([str(i + 1) for i in range(rows)]) + '         ' + '   ' + '   '.join([str(i + 1) for i in range(rows)]) + '\033[0m')
        print('\033[32m  ' + '─' * 37 + '      ' + '  ' + '─' * 37 + '\033[0m')

    for i in range(len(player_field)):
        row_player = chr(65 + i) + ' \033[32m│\033[0m ' + ' \033[32m│\033[0m '.join(['\033[32m' + cell + '\033[0m' for cell in player_field[i]]) + ' \033[32m│\033[0m'
        row_mines = chr(65 + i) + ' \033[32m│\033[0m ' + ' \033[32m│\033[0m '.join(['\033[32m' + cell + '\033[0m' for cell in mines_field[i]]) + ' \033[32m│\033[0m'
        print('\033[32m' + row_player + row_mines + '\033[0m')
        print('\033[32m' + '  ' + '─' * 37 + '      ' + '  ' + '─' * 37 + '\033[0m')

    while True:
        user_input = input("\033[34m  Введите координаты (например, A1): \033[0m")
        if len(user_input) != 2:
            print("Ошибка.")
            continue

        column = int(user_input[1]) - 1
        row = ord(user_input[0].upper()) - 65

        if column < 0 or column >= rows or row < 0 or row >= rows:
            print("Ошибка.")
            continue

        if player_field[row][column] != '\033[32m*\033[0m':
            print("Эта ячейка уже открыта!")
            continue

        if mines_field[row][column] == '\033[32m\033[0m':
            player_field[row][column] = '\033[31m!\033[0m'
            print('\033[31mВЗРЫВ! Игра окончена.\033[0m')
            sys.exit()
        else:
            count = countAdjacentMines(mines_field, row, column)
            player_field[row][column] = str(count) if count > 0 else ' '

        closed_cells = sum(row.count('\033[35m*\033[0m') for row in player_field)
        if closed_cells == mines:
            print("Поздравляем! Вы открыли все ячейки без мин. Вы победили!")
            sys.exit()
            print('\033[32m   ' + '   '.join([str(i + 1) for i in range(rows)]) + '         ' + '   ' + '   '.join([str(i + 1) for i in range(rows)]) + '\033[0m')
            print('\033[32m  ' + '─' * 37 + '      ' + '  ' + '─' * 37 + '\033[0m')
        for i in range(rows):
            row_player = chr(65 + i) + ' \033[32m│\033[0m ' + ' \033[32m│\033[0m '.join(['\033[32m' + cell + '\033[0m' for cell in player_field[i]]) + ' \033[32m│\033[0m'
            row_mines = chr(65 + i) + ' \033[32m│\033[0m ' + ' \033[32m│\033[0m '.join(['\033[32m' + cell + '\033[0m' for cell in mines_field[i]]) + ' \033[32m│\033[0m'
            print('\033[32m' + row_player + row_mines + '\033[0m')
            print('\033[32m' + '  ' + '─' * 37 + '      ' + '  ' + '─' * 37 + '\033[0m')


def getparams(size, mines):
    startGame(size, mines)

# def open_empty_cells(row, col):
#     if 0 <= row < rows and 0 <= col < cols and player_field[row][col] == '\033[32m*\033[0m':
#         count = countAdjacentMines(mines_field, row, col)
#         player_field[row][col] = str(count) if count > 0 else ' '
#
#         if count == 0:
#             for x in range(-1, 2):
#                 for y in range(-1, 2):
#                     open_empty_cells(row + x, col + y)
#     while True:
#         user_input = input("\033[34m  Введите координаты (например, A1): \033[0m")
#         if len(user_input) != 2:
#             print("Ошибка.")
#             continue
#
#         column = int(user_input[1]) - 1
#         row = ord(user_input[0].upper()) - 65
#
#         if column < 0 or column >= 9 or row < 0 or row >= 9:
#             print("Ошибка.")
#             continue
#
#         if player_field[row][column] != '\033[32m*\033[0m':
#             print("Эта ячейка уже открыта!")
#             continue
#
#         if mines_field[row][column] == '\033[32m\033[0m':
#             player_field[row][column] = '\033[31m!\033[0m'
#             print('\033[31mВЗРЫВ! Игра окончена.\033[0m')
#             sys.exit()
#         else:
#             open_empty_cells(row, column)
#
# def countAdjacentMines(field, row, column):
#     count = 0
#     for i in range(max(0, row - 1), min(row + 2, len(field))):
#         for j in range(max(0, column - 1), min(column + 2, len(field[0]))):
#             if field[i][j] == '\033[32m-1\033[0m':
#                 count += 1
#     return count

# def countAdjacentMines(field, row, column):
#     count = 0
#     for i in range(max(0, row - 1), min(row + 2, 9)):
#         for j in range(max(0, column - 1), min(column + 2, 9)):
#             if field[i][j] == '\033[32m&\033[0m':
#                 count += 1
#     return count



# if __name__ == "__main__":
#     from menu import main
#     size, mines = main()
#     startGame(size, mines)