file = open("input.txt")
contents = file.read()
games = contents.split("\n")

LOSS = 0
TIE = 3
WIN = 6


def get_score(opponent_move: str, my_move: str) -> int:
    if my_move == "X":
        move_point = 1
        if opponent_move == "B":
            return move_point + LOSS
        elif opponent_move == "C":
            return move_point + WIN
        else:
            return move_point + TIE
    elif my_move == "Y":
        move_point = 2
        if opponent_move == "A":
            return move_point + WIN
        elif opponent_move == "C":
            return move_point + LOSS
        else:
            return move_point + TIE
    else:
        move_point = 3
        if opponent_move == "A":
            return move_point + LOSS
        elif opponent_move == "B":
            return move_point + WIN
        else:
            return move_point + TIE


total_score = 0

for game in games:
    game = game.split()
    if len(game) != 2:
        continue
    opponent_move, my_move = game

    total_score += get_score(opponent_move, my_move)

print(total_score)
