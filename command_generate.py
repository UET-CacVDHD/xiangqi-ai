from constants import GAME_COMMANDS, PIECE_NAMES, MOVE_NAMES, NUMBER_TO_TEXT


corpus = []

# Xe
x_moves = []
name = 'X'
moves = ['.', '-', '/']
columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
positions = ['trước', 'sau', 'trái', 'phải']
confuse_positions = ['trước', 'sau']
for piece_name in PIECE_NAMES[name]:
    for column in columns:
        for move in moves:
            for move_name in MOVE_NAMES[move]:
                if move in ['.', '/']:
                    for num_step in range(1, 10):
                        sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[str(num_step)]}"
                        x_moves.append(sent)
                        for confuse_position in confuse_positions:
                            sent = f"{piece_name} {confuse_position} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[str(num_step)]}"
                            x_moves.append(sent)
                else:
                    for des_column in columns:
                        if des_column != column:
                            sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                            x_moves.append(sent)
                            for confuse_position in confuse_positions:
                                sent = f"{piece_name} {confuse_position} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                                x_moves.append(sent)

    for position in positions:
        for move in moves:
            for move_name in MOVE_NAMES[move]:
                if move in ['.', '/']:
                    for num_step in range(1, 10):
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[str(num_step)]}"
                        x_moves.append(sent)
                else:
                    for des_column in columns:
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[des_column]}"
                        x_moves.append(sent)

    for move in moves:
        for move_name in MOVE_NAMES[move]:
            if move in ['.', '/']:
                for num_step in range(1, 10):
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[str(num_step)]}"
                    x_moves.append(sent)
            else:
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[des_column]}"
                    x_moves.append(sent)

# Pháo
p_moves = []
name = 'P'
moves = ['.', '/', '-']
columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
positions = ['trước', 'sau', 'trái', 'phải']
confuse_positions = ['trước', 'sau']

for piece_name in PIECE_NAMES[name]:
    for column in columns:
        for move in moves:
            for move_name in MOVE_NAMES[move]:
                if move in ['.', '/']:
                    for num_step in range(1, 10):
                        sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[str(num_step)]}"
                        p_moves.append(sent)
                        for confuse_position in confuse_positions:
                            sent = f"{piece_name} {confuse_position} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[str(num_step)]}"
                            p_moves.append(sent)
                else:
                    for des_column in columns:
                        if des_column != column:
                            sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                            p_moves.append(sent)
                            for confuse_position in confuse_positions:
                                sent = f"{piece_name} {confuse_position} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                                p_moves.append(sent)

    for position in positions:
        for move in moves:
            for move_name in MOVE_NAMES[move]:
                if move in ['.', '/']:
                    for num_step in range(1, 10):
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[str(num_step)]}"
                        p_moves.append(sent)
                else:
                    for des_column in columns:
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[des_column]}"
                        p_moves.append(sent)

    for move in moves:
        for move_name in MOVE_NAMES[move]:
            if move in ['.', '/']:
                for num_step in range(1, 10):
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[str(num_step)]}"
                    p_moves.append(sent)
            else:
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[des_column]}"
                    p_moves.append(sent)

# Mã
m_moves = []
name = 'M'
moves = ['.', '/']
columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]
positions = ['trước', 'sau', 'trái', 'phải']
confuse_positions = ['trước', 'sau']
column_changes = [-2, -1, 1, 2]

for piece_name in PIECE_NAMES[name]:
    for column in columns:
        for move in moves:
            for move_name in MOVE_NAMES[move]:
                for column_change in column_changes:
                    des_column = column + column_change
                    if des_column not in columns:
                        continue
                    sent = f'{piece_name} {NUMBER_TO_TEXT[str(column)]} {move_name} {NUMBER_TO_TEXT[str(des_column)]}'
                    m_moves.append(sent)
                    for confuse_position in confuse_positions:
                        sent = f"{piece_name} {confuse_position} {NUMBER_TO_TEXT[str(column)]} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                        m_moves.append(sent)

    for position in positions:
        for move in moves:
            for move_name in MOVE_NAMES[move]:
                for des_column in columns:
                    sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                    m_moves.append(sent)

    for move in moves:
        for move_name in MOVE_NAMES[move]:
            for des_column in columns:
                sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                m_moves.append(sent)

# Sĩ
s_moves = []
name = 'S'
moves = ['.', '/']
columns = [4, 5, 6]
positions = ['trước', 'sau', 'trái', 'phải']
confuse_positions = ['trước', 'sau']
column_changes = [-1, 1]
for piece_name in PIECE_NAMES[name]:
    for column in columns:
        for move in moves:
            for move_name in MOVE_NAMES[move]:
                for column_change in column_changes:
                    des_column = column + column_change
                    if des_column not in columns:
                        continue
                    sent = f"{piece_name} {NUMBER_TO_TEXT[str(column)]} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                    s_moves.append(sent)
                    if column in [4, 6]:
                        for confuse_position in confuse_positions:
                            #                             if move == '.' and confuse_position == "trước":
                            #                                 continue
                            #                             if move == '/' and confuse_position == "sau":
                            #                                 continue
                            sent = f"{piece_name} {confuse_position} {NUMBER_TO_TEXT[str(column)]} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                            s_moves.append(sent)
    for position in positions:
        for move in moves:
            for move_name in MOVE_NAMES[move]:
                for des_column in columns:
                    sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                    s_moves.append(sent)

    for move in moves:
        for move_name in MOVE_NAMES[move]:
            for des_column in columns:
                sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                s_moves.append(sent)

# Tượng
t_moves = []
name = 'T'
moves = ['.', '/']
columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]
positions = ['trước', 'sau', 'trái', 'phải']
confuse_positions = ['trước', 'sau']
column_changes = [-2, 2]

for piece_name in PIECE_NAMES[name]:
    for column in columns:
        for move in moves:
            for move_name in MOVE_NAMES[move]:
                for column_change in column_changes:
                    des_column = column + column_change
                    if des_column not in columns:
                        continue
                    sent = f"{piece_name} {NUMBER_TO_TEXT[str(column)]} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                    t_moves.append(sent)
                    for confuse_position in confuse_positions:
                        sent = f"{piece_name} {confuse_position} {NUMBER_TO_TEXT[str(column)]} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                        t_moves.append(sent)
    for position in positions:
        for move in moves:
            for move_name in MOVE_NAMES[move]:
                for des_column in columns:
                    sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                    t_moves.append(sent)

    for move in moves:
        for move_name in MOVE_NAMES[move]:
            for des_column in columns:
                sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                t_moves.append(sent)

# Tướng
g_moves = []
name = 'G'
moves = ['.', '-', '/']
columns = [4, 5, 6]
column_changes = [-1, 1]

for piece_name in PIECE_NAMES[name]:
    for column in columns:
        for move in moves:
            for move_name in MOVE_NAMES[move]:
                if move == '-':
                    for column_change in column_changes:
                        des_column = column + column_change
                        if des_column not in columns:
                            continue
                        sent = f"{piece_name} {NUMBER_TO_TEXT[str(column)]} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                        g_moves.append(sent)
                else:
                    num_step = 1
                    sent = f"{piece_name} {NUMBER_TO_TEXT[str(column)]} {move_name} {NUMBER_TO_TEXT[str(num_step)]}"
                    g_moves.append(sent)
    for move in moves:
        for move_name in MOVE_NAMES[move]:
            if move == '-':
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                    g_moves.append(sent)
            else:
                num_step = 1
                sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[str(num_step)]}"
                g_moves.append(sent)

# Tốt\
b_moves = []
name = 'B'
moves = ['.', '-']
columns = list(range(1, 10))
column_changes = [1, -1]
positions = []
confuse_positions = ['trước', 'trước giữa', 'giữa', 'sau giữa', 'sau']
for piece_name in PIECE_NAMES[name]:
    for column in columns:
        for move in moves:
            for move_name in MOVE_NAMES[move]:
                if move == '.':
                    num_step = 1
                    sent = f"{piece_name} {NUMBER_TO_TEXT[str(column)]} {move_name} {NUMBER_TO_TEXT[str(num_step)]}"
                    b_moves.append(sent)
                    for confuse_position in confuse_positions:
                        sent = f"{piece_name} {confuse_position} {NUMBER_TO_TEXT[str(column)]} {move_name} {NUMBER_TO_TEXT[str(num_step)]}"
                        b_moves.append(sent)
                else:
                    for column_change in column_changes:
                        des_column = column + column_change
                        if des_column not in columns:
                            continue
                        sent = f"{piece_name} {NUMBER_TO_TEXT[str(column)]} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                        b_moves.append(sent)
                        for confuse_position in confuse_positions:
                            sent = f"{piece_name} {confuse_position} {NUMBER_TO_TEXT[str(column)]} {move_name} {NUMBER_TO_TEXT[str(des_column)]}"
                            b_moves.append(sent)

    for column in columns:
        sent = f"{piece_name} {NUMBER_TO_TEXT[str(column)]} qua sông"
        b_moves.append(sent)
        sent = f"{piece_name} {NUMBER_TO_TEXT[str(column)]} sang sông"
        b_moves.append(sent)

print(f"""
Sinh {len(x_moves)} nước quân xe
Sinh {len(m_moves)} nước quân mã
Sinh {len(t_moves)} nước quân tượng
Sinh {len(s_moves)} nước quân sĩ
Sinh {len(g_moves)} nước quân tướng 
Sinh {len(b_moves)} nước quân tốt
Sinh {len(p_moves)} nước quân pháo
""")

corpus.extend(x_moves)
corpus.extend(m_moves)
corpus.extend(t_moves)
corpus.extend(s_moves)
corpus.extend(g_moves)
corpus.extend(b_moves)
corpus.extend(p_moves)

GAME_COMMAND_REPLICATION = 30
for game_command in GAME_COMMANDS:
    corpus.extend([game_command] * GAME_COMMAND_REPLICATION)

with open("commands.txt", "w") as outfile:
    for command in corpus:
        outfile.write(command + '\n')
