import json
import random
import sys

def startGame(size, mines):
    rows = int(size)
    print(size)
    print("\033[34m      Добро пожаловать в игру 'Сапер'  \033[0m")
    player_field = []
    for _ in range(rows):
        row = ['\033[32m*\033[0m'] * rows
        player_field.append(row)

    mines_field = []
    for _ in range(rows):
        row = ['\033[32m \033[0m'] * rows
        mines_field.append(row)

    count_mines = 0
    while count_mines < (rows):
        x = random.randint(0, (rows-1))
        y = random.randint(0, (rows-1))
        if mines_field[x][y] != '\033[32m@\033[0m':
            mines_field[x][y] = '\033[32m@\033[0m'
            count_mines += 1

    print('\033[32m    ' + '   '.join([str(i + 1) for i in range(rows)]) +     '     ' + '   ' + '   '.join(
        [str(i + 1) for i in range(rows)]) + '\033[0m')
    print('\033[32m    ' + ' ' * 37 + '      ' + '  ' + ' ' * 37 + '\033[0m')
    for i in range(len(player_field)):
        row_player = chr(65 + i) + ' \033[32m│\033[0m ' + ' \033[32m│\033[0m '.join(
            ['\033[32m' + cell + '\033[0m' for cell in player_field[i]]) + ' \033[32m│\033[0m     '
        row_mines = chr(65 + i) + ' \033[32m│\033[0m ' + ' \033[32m│\033[0m '.join(
            ['\033[32m' + cell + '\033[0m' for cell in mines_field[i]]) + ' \033[32m│\033[0m'
        print('\033[32m' + row_player + row_mines + '\033[0m')
        print('\033[32m' + '  ' + ' ' * 37 + '      ' + '  ' + ' ' * 37 + '\033[0m')

    medals = loadMedals()

    while True:
        user_input = input("\033[34mВведите координаты (например, A1): \033[0m")
        if len(user_input) < 2:
            print("Ошибка.")
            continue

        if user_input[0].isalpha() and user_input[1:].isdigit():
            column = int(user_input[1:]) - 1
        row = ord(user_input[0].upper()) - 65

        if column < 0 or column >= rows or row < 0 or row >= rows:
            print("Ошибка.")
            continue

        if player_field[row][column] != '\033[32m*\033[0m':
            print("Эта ячейка уже открыта!")
            continue

        if mines_field[row][column] == '\033[32m@\033[0m':
            player_field[row][column] = '\033[31m!\033[0m'
            print('\033[31mВзрыв! Игра окончена.\033[0m')

            sys.exit()
        else:
            count = countAdjacentMines(mines_field, row, column, rows)
            player_field[row][column] = str(count) if count > 0 else ' '

        closed_cells = sum(row.count('\033[32m*\033[0m') for row in player_field)


        if closed_cells == mines:
            print("Поздравляю! Вы открыли все ячейки без мин. Вы награждаетесь первой медалью!")
            medals["victory_count"] += 1

            if medals["victory_count"] == 1:
                medals["medals"].append("Первая победа!")
            for count in [5, 12]:
                if medals["victory_count"] == count and f"{count} побед!" not in medals["medals"]:
                    medals["medals"].append(f"{count} побед!")

            saveMedals(medals)
            print("Поздравляю! Вы одержали множество побед и награждаетесь медалями!")
            sys.exit()


        print('\033[32m    ' + '   '.join([str(i + 1) for i in range(rows)]) +     '     ' + '   ' + '   '.join(
            [str(i + 1) for i in range(rows)]) + '\033[0m')
        print('\033[32m ' + ' ' * 37 + '      ' + '  ' + ' ' * 37 + '\033[0m')
        for i in range(rows):
            row_player = chr(65 + i) + ' \033[32m│\033[0m ' + ' \033[32m│\033[0m '.join(
                ['\033[32m' + cell + '\033[0m' for cell in player_field[i]]) + ' \033[32m│\033[0m     '
            row_mines = chr(65 + i) + ' \033[32m│\033[0m ' + ' \033[32m│\033[0m '.join(
                ['\033[32m' + cell + '\033[0m' for cell in mines_field[i]]) + ' \033[32m│\033[0m'
            print('\033[32m' + row_player + row_mines + '\033[0m')
            print('\033[32m ' + '  ' + ' ' * 37 + '      ' + '  ' + ' ' * 37 + '\033[0m')

def countAdjacentMines(field, row, column, rows):
    count = 0
    for i in range(max(0, row - 1), min(row + 2, rows)):
        for j in range(max(0, column - 1), min(column + 2, rows)):
            if field[i][j] == '\033[32m@\033[0m':
                count += 1
    return count

def loadMedals():
    try:
        with open("medals.json", "r") as file:
            data = json.load(file)
        return data

    except FileNotFoundError:
        return {"victory_count": 0, "medals": []}

def saveMedals(medals_data):
    with open("medals.json", "w") as file:
        json.dump(medals_data, file, ensure_ascii=False, indent=4)

def getparams(size, mines):
    startGame(size, mines)
