def main(game_template):
    game_template = [
        ['0', '0', 'x'],
        ['x', 'x', '0'],
        ['x', 'x', '0'],
        [0, -1]  # 0 - сколько ходов "x", 1 - "0"; если -1 то игрок не определен
        # [1,0] - ходит нолик
        # [1,1] - ходит крестик
    ]
    winner = ""
    # проверяем строки
    for i in range(3):
        count_x = 0
        count_0 = 0
        for j in range(3):
            if game_template[i][j] == "x":
                count_x += 1
            if game_template[i][j] == "0":
                count_0 += 1
            if count_x == 3:
                winner = "х"
            if count_0 == 3:
                winner = "0"
    # проверяем столбцы
    for i in range(3):
        count_x = 0
        count_0 = 0
        for j in range(3):
            if game_template[j][i] == "x":
                count_x += 1
            if game_template[j][i] == "0":
                count_0 += 1
            if count_x == 3:
                winner = "х"
            if count_0 == 3:
                winner = "0"
    # проверка главной диагонали
    count_x = 0
    count_0 = 0
    for i in range(3):
        if game_template[i][i] == "x":
            count_x += 1
        if game_template[i][i] == "0":
            count_0 += 1
        if count_x == 3:
            winner = "х"
        if count_0 == 3:
            winner = "0"
    # проверка побочной диагонали
    count_x = 0
    count_0 = 0
    for i in range(3):
        if game_template[i][2-i] == "x":
            count_x += 1
        if game_template[i][2-i] == "0":
            count_0 += 1
        if count_x == 3:
            winner = "х"
        if count_0 == 3:
            winner = "0"
    return(winner)

if __name__ == '__main__':
    print(main("d"))
