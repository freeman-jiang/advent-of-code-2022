file = open("input.txt")
contents = file.read()
games = contents.split("\n")

LOSS_POINT = 0
TIE_POINT = 3
WIN_POINT = 6

ROCK_POINT = 1
PAPER_POINT = 2
SCISSOR_POINT = 3


def get_score(opponent_move: str, my_move: str) -> int:
    if my_move == "X":
        if opponent_move == "B":
            return LOSS_POINT + ROCK_POINT
        elif opponent_move == "C":
            return LOSS_POINT + PAPER_POINT
        else:
            return LOSS_POINT + SCISSOR_POINT
    elif my_move == "Y":
        if opponent_move == "A":
            return TIE_POINT + ROCK_POINT
        elif opponent_move == "C":
            return TIE_POINT + SCISSOR_POINT
        else:
            return TIE_POINT + PAPER_POINT
    else:
        if opponent_move == "A":
            return WIN_POINT + PAPER_POINT
        elif opponent_move == "B":
            return WIN_POINT + SCISSOR_POINT
        else:
            return WIN_POINT + ROCK_POINT


total = 0

for game in games:
    game = game.split()
    if len(game) != 2:
        continue
    opponent_move, my_move = game

    total += get_score(opponent_move, my_move)
    
print(total)
