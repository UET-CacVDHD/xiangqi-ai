piece_names = {
    "G": ['tướng', 'soái'],
    'S': ['sĩ'],
    'T': ['tượng', 'tịnh', 'bộ'],
    'X': ['xe'],
    'M': ['mã'],
    'P': ['pháo'],
    'B': ['tốt', 'binh', 'chốt']
}

move_names = {
    '.': ['tiến', 'tấn'],
    '-': ['bình'],
    '/': ['thoái', 'lùi']
}

number_dict = {
    'một': '1',
    'hai': '2',
    'ba': '3',
    'bốn': '4',
    'năm': '5',
    'sáu': '6',
    'bẩy': '7',
    'bảy': '7',
    'tám': '8',
    'chín': '9'
}

number_to_text = {v: k for k, v in number_dict.items()}

corpus = []

# Xe
name = 'X'
moves = ['.', '-', '/']
columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
positions = ['trước', 'sau', 'trái', 'phải']
confuse_positions = ['trước', 'sau']
for piece_name in piece_names[name]:
    for column in columns:
        for move in moves:
            for move_name in move_names[move]:
                if move in ['.', '/']:
                    for num_step in range(1, 10):
                        sent = f"{piece_name} {number_to_text[column]} {move_name} {number_to_text[str(num_step)]}"
                        corpus.append(sent)
                        for confuse_position in confuse_positions:
                            sent = f"{piece_name} {confuse_position} {number_to_text[column]} {move_name} {number_to_text[str(num_step)]}"
                            corpus.append(sent)
                else:
                    for des_column in columns:
                        if des_column != column:
                            sent = f"{piece_name} {number_to_text[column]} {move_name} {number_to_text[des_column]}"
                            corpus.append(sent)
                            for confuse_position in confuse_positions:
                                sent = f"{piece_name} {confuse_position} {number_to_text[column]} {move_name} {number_to_text[des_column]}"
                                corpus.append(sent)

    for position in positions:
        for move in moves:
            for move_name in move_names[move]:
                if move in ['.', '/']:
                    for num_step in range(1, 10):
                        sent = f"{piece_name} {position} {move_name} {number_to_text[str(num_step)]}"
                        corpus.append(sent)
                else:
                    for des_column in columns:
                        if des_column != column:
                            sent = f"{piece_name} {position} {move_name} {number_to_text[des_column]}"
                            corpus.append(sent)

    for move in moves:
        for move_name in move_names[move]:
            if move in ['.', '/']:
                for num_step in range(1, 10):
                    sent = f"{piece_name} {move_name} {number_to_text[str(num_step)]}"
                    corpus.append(sent)
            else:
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {number_to_text[des_column]}"
                    corpus.append(sent)

# Tượng
name = 'T'
moves = ['.', '/']
columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
positions = ['trước', 'sau', 'trái', 'phải']
confuse_positions = ['trước', 'sau']

for piece_name in piece_names[name]:
    for column in columns:
        for move in moves:
            for move_name in move_names[move]:
                for des_column in columns:
                    if des_column != column:
                        sent = f"{piece_name} {number_to_text[column]} {move_name} {number_to_text[des_column]}"
                        corpus.append(sent)
                        for confuse_position in confuse_positions:
                            sent = f"{piece_name} {confuse_position} {number_to_text[column]} {move_name} {number_to_text[des_column]}"

    for position in positions:
        for move in moves:
            for move_name in move_names[move]:
                for des_column in columns:
                    sent = f"{piece_name} {position} {move_name} {number_to_text[des_column]}"
                    corpus.append(sent)

    for move in moves:
        for move_name in move_names[move]:
            for des_column in columns:
                sent = f"{piece_name} {move_name} {number_to_text[des_column]}"
                corpus.append(sent)

# Pháo
name = 'P'
moves = ['.', '/', '-']
columns = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
positions = ['trước', 'sau', 'trái', 'phải']
confuse_positions = ['trước', 'sau']

for piece_name in piece_names[name]:
    for column in columns:
        for move in moves:
            for move_name in move_names[move]:
                if move in ['.', '/']:
                    for num_step in range(1, 10):
                        sent = f"{piece_name} {number_to_text[column]} {move_name} {number_to_text[str(num_step)]}"
                        corpus.append(sent)
                        for confuse_position in confuse_positions:
                            sent = f"{piece_name} {confuse_position} {number_to_text[column]} {move_name} {number_to_text[str(num_step)]}"
                            corpus.append(sent)
                else:
                    for des_column in columns:
                        if des_column != column:
                            sent = f"{piece_name} {number_to_text[column]} {move_name} {number_to_text[des_column]}"
                            corpus.append(sent)
                            for confuse_position in confuse_positions:
                                sent = f"{piece_name} {confuse_position} {number_to_text[column]} {move_name} {number_to_text[des_column]}"
                                corpus.append(sent)

    for position in positions:
        for move in moves:
            for move_name in move_names[move]:
                if move in ['.', '/']:
                    for num_step in range(1, 10):
                        sent = f"{piece_name} {position} {move_name} {number_to_text[str(num_step)]}"
                        corpus.append(sent)
                else:
                    for des_column in columns:
                        sent = f"{piece_name} {position} {move_name} {number_to_text[des_column]}"
                        corpus.append(sent)

    for move in moves:
        for move_name in move_names[move]:
            if move in ['.', '/']:
                for num_step in range(1, 10):
                    sent = f"{piece_name} {move_name} {number_to_text[str(num_step)]}"
                    corpus.append(sent)
            else:
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {number_to_text[des_column]}"
                    corpus.append(sent)

# Mã
name = 'M'
moves = ['.', '/']
columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]
positions = ['trước', 'sau', 'trái', 'phải']
confuse_positions = ['trước', 'sau']
column_changes = [-2, -1, 1, 2]

for piece_name in piece_names[name]:
    for column in columns:
        for move in moves:
            for move_name in move_names[move]:
                for column_change in column_changes:
                    des_column = column + column_change
                    if des_column not in columns:
                        continue
                    sent = f'{piece_name} {number_to_text[str(column)]} {move_name} {number_to_text[str(des_column)]}'
                    corpus.append(sent)
                    for confuse_position in confuse_positions:
                        sent = f"{piece_name} {confuse_position} {number_to_text[str(column)]} {move_name} {number_to_text[str(des_column)]}"
                        corpus.append(sent)

    for position in positions:
        for move in moves:
            for move_name in move_names[move]:
                for des_column in columns:
                    sent = f"{piece_name} {position} {move_name} {number_to_text[str(des_column)]}"
                    corpus.append(sent)

    for move in moves:
        for move_name in move_names[move]:
            for des_column in columns:
                sent = f"{piece_name} {move_name} {number_to_text[str(des_column)]}"
                corpus.append(sent)

# Sĩ
name = 'S'
moves = ['.', '/']
columns = [4, 5, 6]
positions = ['trước', 'sau', 'trái', 'phải']
confuse_positions = ['trước', 'sau']
column_changes = [-1, 1]
for piece_name in piece_names[name]:
    for column in columns:
        for move in moves:
            for move_name in move_names[move]:
                for column_change in column_changes:
                    des_column = column + column_change
                    if des_column not in columns:
                        continue
                    sent = f"{piece_name} {number_to_text[str(column)]} {move_name} {number_to_text[str(des_column)]}"
                    corpus.append(sent)
                    if column in [4, 6]:
                        for confuse_position in confuse_positions:
                            #                             if move == '.' and confuse_position == "trước":
                            #                                 continue
                            #                             if move == '/' and confuse_position == "sau":
                            #                                 continue
                            sent = f"{piece_name} {confuse_position} {number_to_text[str(column)]} {move_name} {number_to_text[str(des_column)]}"
                            corpus.append(sent)
    for position in positions:
        for move in moves:
            for move_name in move_names[move]:
                for des_column in columns:
                    sent = f"{piece_name} {position} {move_name} {number_to_text[str(des_column)]}"
                    corpus.append(sent)

    for move in moves:
        for move_name in move_names[move]:
            for des_column in columns:
                sent = f"{piece_name} {move_name} {number_to_text[str(des_column)]}"
                corpus.append(sent)

# Tượng
name = 'T'
moves = ['.', '/']
columns = [1, 2, 3, 4, 5, 6, 7, 8, 9]
positions = ['trước', 'sau', 'trái', 'phải']
confuse_positions = ['trước', 'sau']
column_changes = [-2, 2]

for piece_name in piece_names[name]:
    for column in columns:
        for move in moves:
            for move_name in move_names[move]:
                for column_change in column_changes:
                    des_column = column + column_change
                    if des_column not in columns:
                        continue
                    sent = f"{piece_name} {number_to_text[str(column)]} {move_name} {number_to_text[str(des_column)]}"
                    corpus.append(sent)
                    for confuse_position in confuse_positions:
                        sent = f"{piece_name} {confuse_position} {number_to_text[str(column)]} {move_name} {number_to_text[str(des_column)]}"
                        corpus.append(sent)
    for position in positions:
        for move in moves:
            for move_name in move_names[move]:
                for des_column in columns:
                    sent = f"{piece_name} {position} {move_name} {number_to_text[str(des_column)]}"
                    corpus.append(sent)

    for move in moves:
        for move_name in move_names[move]:
            for des_column in columns:
                sent = f"{piece_name} {move_name} {number_to_text[str(des_column)]}"
                corpus.append(sent)

# Tướng
name = 'G'
moves = ['.', '-', '/']
columns = [4, 5, 6]
column_changes = [-1, 1]

for piece_name in piece_names[name]:
    for column in columns:
        for move in moves:
            for move_name in move_names[move]:
                if move == '-':
                    for column_change in column_changes:
                        des_column = column + column_change
                        if des_column not in columns:
                            continue
                        sent = f"{piece_name} {number_to_text[str(column)]} {move_name} {number_to_text[str(des_column)]}"
                        corpus.append(sent)
                else:
                    num_step = 1
                    sent = f"{piece_name} {number_to_text[str(column)]} {move_name} {number_to_text[str(num_step)]}"
                    corpus.append(sent)
    for move in moves:
        for move_name in move_names[move]:
            if move == '-':
                for des_column in columns:
                    sent = f"{piece_name} {move_name} {number_to_text[str(des_column)]}"
                    corpus.append(sent)
            else:
                num_step = 1
                sent = f"{piece_name} {move_name} {number_to_text[str(num_step)]}"
                corpus.append(sent)

# Tốt
name = 'B'
moves = ['.', '-']
columns = list(range(1, 10))
column_changes = [1, -1]
positions = []
confuse_positions = ['trước', 'trước giữa', 'giữa', 'sau giữa', 'sau']
for piece_name in piece_names[name]:
    for column in columns:
        for move in moves:
            for move_name in move_names[move]:
                if move == '.':
                    num_step = 1
                    sent = f"{piece_name} {number_to_text[str(column)]} {move_name} {number_to_text[str(num_step)]}"
                    corpus.append(sent)
                    for confuse_position in confuse_positions:
                        sent = f"{piece_name} {confuse_position} {number_to_text[str(column)]} {move_name} {number_to_text[str(num_step)]}"
                        corpus.append(sent)
                else:
                    for column_change in column_changes:
                        des_column = column + column_change
                        if des_column not in columns:
                            continue
                        sent = f"{piece_name} {number_to_text[str(column)]} {move_name} {number_to_text[str(des_column)]}"
                        corpus.append(sent)
                        for confuse_position in confuse_positions:
                            sent = f"{piece_name} {confuse_position} {number_to_text[str(column)]} {move_name} {number_to_text[str(des_column)]}"
                            corpus.append(sent)

    for column in columns:
        sent = f"{piece_name} {number_to_text[str(column)]} qua sông"
        corpus.append(sent)
        sent = f"{piece_name} {number_to_text[str(column)]} sang sông"
        corpus.append(sent)

with open("commands.txt", "w") as outfile:
    for command in corpus:
        outfile.write(command + '\n')