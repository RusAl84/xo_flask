from flask import Flask, request, jsonify
from flask_cors import CORS
from rules import check_winer

app = Flask(__name__)
CORS(app)

seeds = []
games = {}
game_template = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [0, -1]  # 0 - сколько ходов "x", 1 - "0"; если -1 то игрок не определен
    # [1,0] - ходит нолик
    # [1,1] - ходит крестик
]


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/set_seed', methods=['POST'])
def set_seed():  # put application's code here
    json_data = request.json
    str1 = json_data
    result = "unknown"
    if str1 in games:
        print("seed {str1} уже зарегистрирован, вы добавлены как второй игрок ""0""")
        if games[str1][3][1] == -1:
            games[str1][3][1] = 0
            result = "0"
        else:
            print(f"для {str1} seed  уже определены оба игрока")
    else:
        print(f"Добавлен seed: {str1}")
        games[str1] = game_template
        result = "x"
    print(games)
    return result


@app.route('/api/make_turn', methods=['POST'])
def make_turn():  # put application's code here
    json_data = request.json
    print(json_data)
    # {
    #     "seed": "rusal",
    #     "who": "x",
    #     "turn": [0, 0]
    # }
    seed_str = json_data["seed"]
    if seed_str in games:
        # [1,0] - ходит нолик
        # [1,1] - ходит крестик
        current_turn = ""
        if games[seed_str][3][0] == games[seed_str][3][1]:  # тот ли игрок ходит?
            current_turn = "x"  # ходит креcтик
        else:
            current_turn = "0"  # ходит нолик
        if current_turn == json_data["who"] or True:  # !!!!!!!!!!!!!!!!11
            x = json_data["turn"][0]
            y = json_data["turn"][1]
            if games[seed_str][x][y] == ' ':  # проверяем можно ли в эту клетку ходить?
                games[seed_str][x][y] = json_data["who"]  # делаем ход
                if json_data["who"] == "x":
                    games[seed_str][3][0] += 1
                    print(games)
                else:
                    games[seed_str][3][1] += 1
                    print(games)
                winer = check_winer(games[seed_str])
                if len(winer) > 0:
                    str1 = "Победил " + winer
                    print(str1)
                    del games[seed_str]
                    return (str1)

                return jsonify(games[seed_str])
            else:
                str1 = "в эту клетку ходить нельзя"
                print(str1)
                return str1
        else:
            str1 = f"сейчас ходит игрок \"{current_turn}\""
            print(str1)
            return str1
    else:
        str1 = f"такого seed не зарегистрировано {seed_str}"
        print(str1)
        return str1


if __name__ == '__main__':
    app.run()
