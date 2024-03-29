from constants import META_COMMAND_TEXT_TO_SYMBOL, PIECE_SYMBOL_TO_TEXTS, \
    NORM_OP_SYMBOL_TO_TEXTS, NUMBER_TO_TEXT

# Xe
x_moves = []
x_positions = set()
name = 'X'
moves = ['.', '-', '/', "-t", "-p"]
columns = list(range(1, 10))
extend_positions = ['trước', 'sau', 'trái', 'phải',
                    'trên', 'dưới']
vrps = ['trước', 'sau',
        'trên', 'dưới']

for column in columns:
    x_positions.add(f"{NUMBER_TO_TEXT[column]}")
    for vrp in vrps:
        x_positions.add(f"{vrp} {NUMBER_TO_TEXT[column]}")
for position in extend_positions:
    x_positions.add(position)
x_positions.add("")

for piece_name in PIECE_SYMBOL_TO_TEXTS[name]:
    for column in columns:
        for move in moves:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                if move in ['.', '/', "-t", "-p"]:
                    for num_step in range(1, 10):
                        sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[num_step]}"
                        x_moves.append(sent)
                        for vrp in vrps:
                            sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[num_step]}"
                            x_moves.append(sent)
                else:
                    for des_column in columns:
                        if des_column != column:
                            sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                            x_moves.append(sent)
                            for vrp in vrps:
                                sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                                x_moves.append(sent)

    for position in extend_positions:
        for move in moves:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                if move in ['.', '/', "-t", "-p"]:
                    for num_step in range(1, 10):
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[num_step]}"
                        x_moves.append(sent)
                else:
                    for des_column in columns:
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[des_column]}"
                        x_moves.append(sent)

    for move in moves:
        for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
            if move in ['.', '/', "-t", "-p"]:
                for num_step in range(1, 10):
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[num_step]}"
                    x_moves.append(sent)
            else:
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[des_column]}"
                    x_moves.append(sent)

# Pháo
p_moves = []
p_positions = set()
name = 'P'
moves = ['.', '/', '-', "-t", "-p"]
columns = list(range(1, 10))
vrps = ['trước', 'sau',
        'trên', 'dưới']
extend_positions = ['trước', 'sau', 'trái', 'phải',
                    'trên', 'dưới']

for column in columns:
    p_positions.add(NUMBER_TO_TEXT[column])
    for vrp in vrps:
        p_positions.add(f"{vrp} {NUMBER_TO_TEXT[column]}")
for position in extend_positions:
    p_positions.add(position)
p_positions.add("")

for piece_name in PIECE_SYMBOL_TO_TEXTS[name]:
    for column in columns:
        for move in moves:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                if move in ['.', '/', "-t", "-p"]:
                    for num_step in range(1, 10):
                        sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[num_step]}"
                        p_moves.append(sent)
                        for vrp in vrps:
                            sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[num_step]}"
                            p_moves.append(sent)
                else:
                    for des_column in columns:
                        if des_column != column:
                            sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                            p_moves.append(sent)
                            for vrp in vrps:
                                sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                                p_moves.append(sent)

    for position in extend_positions:
        for move in moves:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                if move in ['.', '/', "-t", "-p"]:
                    for num_step in range(1, 10):
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[num_step]}"
                        p_moves.append(sent)
                else:
                    for des_column in columns:
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[des_column]}"
                        p_moves.append(sent)

    for move in moves:
        for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
            if move in ['.', '/', "-t", "-p"]:
                for num_step in range(1, 10):
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[num_step]}"
                    p_moves.append(sent)
            else:
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[des_column]}"
                    p_moves.append(sent)

# Mã
m_moves = []
m_positions = set()
name = 'M'
moves = ['.', '/', ".-t", ".-p", "/-t", "/-p"]
columns = list(range(1, 10))
vrps = ['trước', 'sau',
        'trên', 'dưới']
extend_positions = ['trước', 'sau', 'trái', 'phải',
                    'trên', 'dưới']
column_changes = [-2, -1, 1, 2]
num_step_left_right = [1, 2]
for column in columns:
    m_positions.add(NUMBER_TO_TEXT[column])
    for vrp in vrps:
        m_positions.add(f"{vrp} {NUMBER_TO_TEXT[column]}")
for position in extend_positions:
    m_positions.add(position)
m_positions.add("")

for piece_name in PIECE_SYMBOL_TO_TEXTS[name]:
    for column in columns:
        for move in moves:
            if move in [".", "/"]:
                for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                    for column_change in column_changes:
                        des_column = column + column_change
                        if des_column not in columns:
                            continue
                        sent = f'{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}'
                        m_moves.append(sent)
                        for vrp in vrps:
                            sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                            m_moves.append(sent)
            else:
                for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                    for num_step in num_step_left_right:
                        sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[num_step]}"
                        m_moves.append(sent)
                        for vrp in vrps:
                            sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[num_step]}"
                            m_moves.append(sent)

    for position in extend_positions:
        for move in moves:
            if move in ['.', '/']:
                for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                    for des_column in columns:
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[des_column]}"
                        m_moves.append(sent)
            else:
                for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                    for num_step in num_step_left_right:
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[num_step]}"
                        m_moves.append(sent)

    for move in moves:
        if move in ['.', '/']:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[des_column]}"
                    m_moves.append(sent)
        else:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                for num_step in num_step_left_right:
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[num_step]}"
                    m_moves.append(sent)

# Sĩ
s_moves = []
s_positions = set()
name = 'S'
moves = ['.', '/', '.-t', '.-p', '/-t', '/-p']
columns = [4, 5, 6]
extend_positions = ['trước', 'sau', 'trái', 'phải',
                    'trên', 'dưới']
vrps = ['trước', 'sau',
        'trên', 'dưới']
column_changes = [-1, 1]
for column in columns:
    s_positions.add(NUMBER_TO_TEXT[column])
    for vrp in vrps:
        s_positions.add(f"{vrp} {NUMBER_TO_TEXT[column]}")
for position in extend_positions:
    s_positions.add(position)
s_positions.add("")

for piece_name in PIECE_SYMBOL_TO_TEXTS[name]:
    for column in columns:
        for move in moves:
            if move in ['.', '/']:
                for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                    for column_change in column_changes:
                        des_column = column + column_change
                        if des_column not in columns:
                            continue
                        sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                        s_moves.append(sent)
                        if column in [4, 6]:
                            for vrp in vrps:
                                sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                                s_moves.append(sent)
            else:
                for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                    sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name}"
                    s_moves.append(sent)
                    if column in [4, 6]:
                        for vrp in vrps:
                            sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name}"
                            s_moves.append(sent)

    for position in extend_positions:
        for move in moves:
            if move in ['.', '/']:
                for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                    for des_column in columns:
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[des_column]}"
                        s_moves.append(sent)
            else:
                for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                    sent = f"{piece_name} {position} {move_name}"
                    s_moves.append(sent)


    for move in moves:
        if move in ['.', '/']:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[des_column]}"
                    s_moves.append(sent)
        else:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                sent = f"{piece_name} {move_name}"
                s_moves.append(sent)
# Tượng
t_moves = []
t_positions = set()
name = 'T'
moves = ['.', '/', '.-t', '.-p', '/-t', '/-p']
columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]
extend_positions = ['trước', 'sau', 'trái', 'phải',
                    'trên', 'dưới']
vrps = ['trước', 'sau',
        'trên', 'dưới']
column_changes = [-2, 2]

for column in columns:
    t_positions.add(NUMBER_TO_TEXT[column])
    for vrp in vrps:
        t_positions.add(f"{vrp} {NUMBER_TO_TEXT[column]}")
for position in extend_positions:
    t_positions.add(position)
t_positions.add("")

for piece_name in PIECE_SYMBOL_TO_TEXTS[name]:
    for column in columns:
        for move in moves:
            if move in ['.', '/']:
                for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                    for column_change in column_changes:
                        des_column = column + column_change
                        if des_column not in columns:
                            continue
                        sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                        t_moves.append(sent)
                        for vrp in vrps:
                            sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                            t_moves.append(sent)
            else:
                for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                    sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name}"
                    t_moves.append(sent)
                    for vrp in vrps:
                        sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name}"
                        t_moves.append(sent)

    for position in extend_positions:
        for move in moves:
            if move in ['.', '/']:
                for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                    for des_column in columns:
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[des_column]}"
                        t_moves.append(sent)
            else:
                for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                    sent = f"{piece_name} {position} {move_name}"
                    t_moves.append(sent)

    for move in moves:
        if move in ['.', '/']:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[des_column]}"
                    t_moves.append(sent)
        else:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                sent = f"{piece_name} {move_name}"
                t_moves.append(sent)

# Tướng
g_moves = []
g_positions = set()
name = 'G'
moves = ['.', '-', '/', '-t', '-p']
columns = [4, 5, 6]
column_changes = [-1, 1]

for column in columns:
    g_positions.add(NUMBER_TO_TEXT[column])
g_positions.add("")

for piece_name in PIECE_SYMBOL_TO_TEXTS[name]:
    for column in columns:
        for move in moves:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                if move == '-':
                    for column_change in column_changes:
                        des_column = column + column_change
                        if des_column not in columns:
                            continue
                        sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                        g_moves.append(sent)
                elif move in ['.', '/']:
                    num_step = 1
                    sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[num_step]}"
                    g_moves.append(sent)
                    sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name}"
                    g_moves.append(sent)
                else:
                    sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name}"
                    g_moves.append(sent)
    for move in moves:
        for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
            if move == '-':
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[des_column]}"
                    g_moves.append(sent)
            elif move in ['.', '/']:
                num_step = 1
                sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[num_step]}"
                g_moves.append(sent)
                sent = f"{piece_name} {move_name}"
                g_moves.append(sent)
            else:
                sent = f"{piece_name} {move_name}"
                g_moves.append(sent)

# Tốt
b_moves = []
b_positions = set()
name = 'B'
moves = ['.', '-', "-t", "-p"]
columns = list(range(1, 10))
column_changes = [1, -1]
extend_positions = ['trước', 'trước giữa', 'giữa', 'sau giữa', 'sau',
                    'trên', 'trên giữa', 'dưới giữa', 'dưới',
                    'trái', 'trái giữa', 'phải giữa', 'phải']
vrps = ['trước', 'trước giữa', 'giữa', 'sau giữa', 'sau',
        'trên', 'trên giữa', 'dưới giữa', 'dưới']

for column in columns:
    b_positions.add(NUMBER_TO_TEXT[column])
    for vrp in vrps:
        b_positions.add(f"{vrp} {NUMBER_TO_TEXT[column]}")
for position in extend_positions:
    b_positions.add(position)
b_positions.add("")

for piece_name in PIECE_SYMBOL_TO_TEXTS[name]:
    for column in columns:
        for move in moves:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                if move == '.':
                    num_step = 1
                    sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[num_step]}"
                    b_moves.append(sent)
                    sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name}"
                    b_moves.append(sent)
                    for vrp in vrps:
                        sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[num_step]}"
                        b_moves.append(sent)
                        sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name}"
                        b_moves.append(sent)
                elif move == '-':
                    for column_change in column_changes:
                        des_column = column + column_change
                        if des_column not in columns:
                            continue
                        sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                        b_moves.append(sent)
                        for vrp in vrps:
                            sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name} {NUMBER_TO_TEXT[des_column]}"
                            b_moves.append(sent)
                else:
                    sent = f"{piece_name} {NUMBER_TO_TEXT[column]} {move_name}"
                    b_moves.append(sent)
                    for vrp in vrps:
                        sent = f"{piece_name} {vrp} {NUMBER_TO_TEXT[column]} {move_name}"
                        b_moves.append(sent)

    for position in extend_positions:
        for move in moves:
            for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
                if move == '.':
                    num_step = 1
                    sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[num_step]}"
                    b_moves.append(sent)
                    sent = f"{piece_name} {position} {move_name}"
                    b_moves.append(sent)
                elif move == '-':
                    for des_column in columns:
                        sent = f"{piece_name} {position} {move_name} {NUMBER_TO_TEXT[des_column]}"
                        b_moves.append(sent)
                else:
                    sent = f"{piece_name} {position} {move_name}"
                    b_moves.append(sent)

    for move in moves:
        for move_name in NORM_OP_SYMBOL_TO_TEXTS[move]:
            if move == '.':
                num_step = 1
                sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[num_step]}"
                b_moves.append(sent)
                sent = f"{piece_name} {move_name}"
                b_moves.append(sent)
            elif move == '-':
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {NUMBER_TO_TEXT[des_column]}"
                    b_moves.append(sent)
            else:
                sent = f"{piece_name} {move_name}"
                b_moves.append(sent)

    for column in columns:
        sent = f"{piece_name} {NUMBER_TO_TEXT[column]} qua sông"
        b_moves.append(sent)
        sent = f"{piece_name} {NUMBER_TO_TEXT[column]} sang sông"
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

norm_commands = []
norm_commands.extend(x_moves)
norm_commands.extend(m_moves)
norm_commands.extend(t_moves)
norm_commands.extend(s_moves)
norm_commands.extend(g_moves)
norm_commands.extend(b_moves)
norm_commands.extend(p_moves)

meta_commands = []
for game_command in META_COMMAND_TEXT_TO_SYMBOL:
    meta_commands.append(game_command)


print(f"""
{len(s_positions)} vị trí quân sĩ
{len(m_positions)} vị trí quân mã
{len(b_positions)} vị trí quân tốt
{len(t_positions)} vị trí quân tượng
{len(p_positions)} vị trí quân pháo
{len(x_positions)} vị trí quân xe
""")
# Eat command
positions_dict = {
    "S": s_positions,
    "M": m_positions,
    "B": b_positions,
    "T": t_positions,
    "P": p_positions,
    "X": x_positions,
    "G": g_positions,
}
eat_commands = []
for piece_1 in PIECE_SYMBOL_TO_TEXTS:
    for name_1 in PIECE_SYMBOL_TO_TEXTS[piece_1]:
        for piece_2 in PIECE_SYMBOL_TO_TEXTS:
            if piece_2 == "G":
                continue
            for name_2 in PIECE_SYMBOL_TO_TEXTS[piece_2]:
                for position_1 in positions_dict[piece_1]:
                    for position_2 in positions_dict[piece_2]:
                        eat_commands.append(" ".join(f"{name_1} {position_1} ăn {name_2} {position_2}".split()))
                        eat_commands.append(" ".join(f"{name_1} {position_1} bắt {name_2} {position_2}".split()))
print(len(eat_commands))
print(len(norm_commands))
print(len(meta_commands))

checkmate_commands = []
columns = list(range(1, 10))
for piece in PIECE_SYMBOL_TO_TEXTS:
    if piece == "G":
        continue
    for name in PIECE_SYMBOL_TO_TEXTS[piece]:
        for position in positions_dict[piece]:
            checkmate_commands.append(f"{name} {position} chiếu tướng")
            checkmate_commands.append(f"{name} {position} chiếu")
            for des_column in columns:
                checkmate_commands.append(f"{name} {position} chiếu tướng {NUMBER_TO_TEXT[des_column]}")
                checkmate_commands.append(f"{name} {position} chiếu {NUMBER_TO_TEXT[des_column]}")
print(len(checkmate_commands))

corpus = eat_commands + norm_commands * 200 + meta_commands * 10000 + checkmate_commands * 30

with open("commands.txt", "w") as outfile:
    for command in corpus:
        outfile.write(command + '\n')
