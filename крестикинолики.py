map = [1,2,3,
       4,5,6,
       7,8,9]

victory_var = [[0,1,2],
                   [3,4,5],
                   [6,7,8],
                   [0,4,8],
                   [2,5,6],
                   [0,3,6],
                   [1,4,7],
                   [2,5,8]]

def map_print():
    print(map[0],end=" ")
    print(map[1],end=" ")
    print(map[2])

    print(map[3],end=" ")
    print(map[4],end=" ")
    print(map[5])

    print(map[6],end=" ")
    print(map[7],end=" ")
    print(map[8])

def step_map(step,symb):
    ind = map.index(step)
    map[ind] = symb


def res_game():
    win = ""

    for i in victory_var:
        if map[i[0]] == "X" and map[i[1]] == "X" and map[i[2]] == "X":
            win = "X"
        if map[i[0]] == "O" and map[i[1]] == "O" and map[i[2]] == "O":
            win = "O"

    return win

game_over = False
player1 = True

while game_over == False:

    map_print()

    if player1 == True:
        symbol = "X"
        step = int(input("Человек X, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Человек O, ваш ход: "))

    step_map(step, symbol)  # делаем ход в указанную ячейку
    win = res_game()  # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

map_print()

print("Победил", win)
