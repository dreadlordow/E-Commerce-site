n = int(input())
commands = int(input())
matrix = [[x for x in input()] for _ in range(n)]

steps = {
    'right': [0, 1],
    'left': [0, -1],
    'up': [-1, 0],
    'down': [1, 0],
}
player_row = None
player_col = None
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'f':
            player_row = i
            player_col = j


def make_step(row, col, step):
    row_to_move = row + steps[step][0]
    col_to_move = col + steps[step][1]
    return (row_to_move, col_to_move)


is_won = False
is_lost = True
for _ in range(commands):
    command = input()
    row_to_go, col_to_go = make_step(player_row, player_col, command)
    if row_to_go >= n:
        row_to_go = 0
    if col_to_go >= n:
        col_to_go = 0
    to_move = matrix[row_to_go][col_to_go]

    if to_move == 'T':
        continue

    elif to_move == '-':
        matrix[player_row][player_col] = '-'
        matrix[row_to_go][col_to_go] = 'f'
        player_row = row_to_go
        player_col = col_to_go

    elif to_move == 'B':
        matrix[player_row][player_col] = '-'
        row_to_go += steps[command][0]
        col_to_go += steps[command][1]
        if matrix[row_to_go][col_to_go] == 'F':
            matrix[row_to_go][col_to_go] = 'f'
            is_won = True
            break
        matrix[row_to_go][col_to_go] = 'f'
        player_row = row_to_go
        player_col = col_to_go

    if to_move == 'F':
        matrix[player_row][player_col] = '-'
        matrix[row_to_go][col_to_go] = 'f'
        is_won = True
        break

if is_won:
    print(f'Player won!')


elif is_lost:
    print(f'Player lost!')

for row in matrix:
    print(''.join(row))