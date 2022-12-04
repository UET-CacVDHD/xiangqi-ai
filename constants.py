from collections import defaultdict

NORM_OP_TEXT_TO_SYMBOL = {
    "tiến": '.',
    "tấn": '.',
    "bình": '-',
    "lùi": '/',
    "thoái": '/'
}
PIECE_TEXT_TO_SYMBOL = {
    'tướng': 'G',
    'soái': 'G',
    'sĩ': 'S',
    'tượng': 'T',
    'tịnh': 'T',
    'bồ': 'T',
    'xe': 'X',
    'mã': 'M',
    'pháo': 'P',
    'tốt': 'B',
    'binh': 'B',
    'chốt': 'B',
}

VRP_TEXT_TO_SYMBOL = {
    "trước": "t",
    "trên": "t",
    "trước giữa": "tg",
    "trên giữa": "tg",
    "sau giữa": "sg",
    "dưới giữa": "sg",
    "giữa": "g",
    "sau": "s",
    "dưới": "s",
}

# TODO: complete extend position
EXTEND_POSITION_TEXT_TO_SYMBOL = {
    'trước': 't',
    'trên': 't',
    'trước giữa': 'tg',
    'trên giữa': 'tg',
    'sau giữa': 'sg',
    'dưới giữa': 'sg',
    'giữa': 'g',
    'sau': 's',
    'dưới': 's',
    'trái': '-t',
    'phải': '-p',
    'trái giữa': '-tg',
    'phải giữa': '-pg'
}

META_COMMAND_TEXT_TO_SYMBOL = {
    "chấp nhận": "ok",
    "xác nhận": "ok",
    "đồng ý": "ok",
    "ô kê": "ok",
    "hủy bỏ": "ko",
    "từ chối": "ko",
    "đầu hàng": "$",
    "xin hòa": "=",
    "đổi phe": "<>",
    "xin chơi lại": "^",
    "đi lại": "<"
}

NUMBER_TEXT_TO_SYMBOL = {
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

PIECE_SYMBOL_TO_TEXTS = {
    "G": ['tướng', 'soái'],
    'S': ['sĩ'],
    'T': ['tượng', 'tịnh', 'bộ'],
    'X': ['xe'],
    'M': ['mã'],
    'P': ['pháo'],
    'B': ['tốt', 'binh', 'chốt']
}

NORM_OP_SYMBOL_TO_TEXTS = {
    '.': ['tiến', 'tấn'],
    '-': ['bình'],
    '/': ['thoái', 'lùi']
}


NUMBER_TO_TEXT = {int(v): k for k, v in NUMBER_TEXT_TO_SYMBOL.items()}

NORM_OPERATION_LIST = list(NORM_OP_TEXT_TO_SYMBOL.keys())

PIECE_LIST = list(PIECE_TEXT_TO_SYMBOL.keys())

VRP_LIST = list(VRP_TEXT_TO_SYMBOL.keys())

NUMBER_LIST = list(NUMBER_TEXT_TO_SYMBOL.keys())

EXTEND_POSITION_LIST = list(EXTEND_POSITION_TEXT_TO_SYMBOL.keys())

META_COMMAND_LIST = list(META_COMMAND_TEXT_TO_SYMBOL.keys())

NORM_OP_TOKEN = "<NORM_OP>"
PIECE_TOKEN = "<PIECE>"
VRP_TOKEN = "<VRP>"
NUMBER_TOKEN = "<NUM>"
CHECKMATE_TOKEN = "<CHECKMATE>"
BEAT_TOKEN = "<BEAT>"
PASS_RIVER_TOKEN = "<PASS_RIVER>"
META_TOKEN = "<META>"
EXTEND_POSITION_TOKEN = "<EXT_POS>"

TYPE_TO_TOKENS = {
    "NORM_OPERATION": NORM_OP_TOKEN,
    "PIECE": PIECE_TOKEN,
    "VRP": VRP_TOKEN,
    "NUMBER": NUMBER_TOKEN,
    "CHECKMATE": CHECKMATE_TOKEN,
    "BEAT": BEAT_TOKEN,
    "PASS_RIVER": PASS_RIVER_TOKEN,
    "META": META_TOKEN,
    "EXTEND_POSITION": EXTEND_POSITION_TOKEN
}

TYPE_TO_TEXTS = {
    "NORM_OPERATION": NORM_OPERATION_LIST,
    "PIECE": PIECE_LIST,
    "VRP": VRP_LIST,
    "NUMBER": NUMBER_LIST,
    "CHECKMATE": ["chiếu tướng"],
    "BEAT": ["ăn", "bắt"],
    "PASS_RIVER": ["qua sông", "sang sông"],
    "META": META_COMMAND_LIST,
    "EXTEND_POSITION": EXTEND_POSITION_LIST
}

TEXT_TO_TYPES = defaultdict(lambda: [])

for tp in TYPE_TO_TEXTS:
    for text in TYPE_TO_TEXTS[tp]:
        TEXT_TO_TYPES[text].append(tp)

COMMAND_TYPE_TO_STRUCTS = {
    "NORM_COMMAND": [(PIECE_TOKEN, VRP_TOKEN, NUMBER_TOKEN, NORM_OP_TOKEN, NUMBER_TOKEN),
                     (PIECE_TOKEN, NUMBER_TOKEN, NORM_OP_TOKEN, NUMBER_TOKEN),
                     (PIECE_TOKEN, EXTEND_POSITION_TOKEN, NORM_OP_TOKEN, NUMBER_TOKEN),
                     (PIECE_TOKEN, NORM_OP_TOKEN, NUMBER_TOKEN)],
    "BEAT_COMMAND": [(PIECE_TOKEN, VRP_TOKEN, NUMBER_TOKEN, BEAT_TOKEN, PIECE_TOKEN, VRP_TOKEN, NUMBER_TOKEN),
                     (PIECE_TOKEN, VRP_TOKEN, NUMBER_TOKEN, BEAT_TOKEN, PIECE_TOKEN, NUMBER_TOKEN),
                     (PIECE_TOKEN, VRP_TOKEN, NUMBER_TOKEN, BEAT_TOKEN, PIECE_TOKEN, EXTEND_POSITION_TOKEN),
                     (PIECE_TOKEN, VRP_TOKEN, NUMBER_TOKEN, BEAT_TOKEN, PIECE_TOKEN),
                     (PIECE_TOKEN, NUMBER_TOKEN, BEAT_TOKEN, PIECE_TOKEN, VRP_TOKEN, NUMBER_TOKEN),
                     (PIECE_TOKEN, NUMBER_TOKEN, BEAT_TOKEN, PIECE_TOKEN, NUMBER_TOKEN),
                     (PIECE_TOKEN, NUMBER_TOKEN, BEAT_TOKEN, PIECE_TOKEN, EXTEND_POSITION_TOKEN),
                     (PIECE_TOKEN, NUMBER_TOKEN, BEAT_TOKEN, PIECE_TOKEN),
                     (PIECE_TOKEN, EXTEND_POSITION_TOKEN, BEAT_TOKEN, PIECE_TOKEN, VRP_TOKEN, NUMBER_TOKEN),
                     (PIECE_TOKEN, EXTEND_POSITION_TOKEN, BEAT_TOKEN, PIECE_TOKEN, NUMBER_TOKEN),
                     (PIECE_TOKEN, EXTEND_POSITION_TOKEN, BEAT_TOKEN, PIECE_TOKEN, EXTEND_POSITION_TOKEN),
                     (PIECE_TOKEN, EXTEND_POSITION_TOKEN, BEAT_TOKEN, PIECE_TOKEN),
                     (PIECE_TOKEN, BEAT_TOKEN, PIECE_TOKEN, VRP_TOKEN, NUMBER_TOKEN),
                     (PIECE_TOKEN, BEAT_TOKEN, PIECE_TOKEN, NUMBER_TOKEN),
                     (PIECE_TOKEN, BEAT_TOKEN, PIECE_TOKEN, EXTEND_POSITION_TOKEN),
                     (PIECE_TOKEN, BEAT_TOKEN, PIECE_TOKEN)],
    "META_COMMAND": [(META_TOKEN,)],
    "CHECKMATE_COMMAND": [(PIECE_TOKEN, VRP_TOKEN, NUMBER_TOKEN, CHECKMATE_TOKEN),
                          (PIECE_TOKEN, NUMBER_TOKEN, CHECKMATE_TOKEN),
                          (PIECE_TOKEN, EXTEND_POSITION_TOKEN, CHECKMATE_TOKEN),
                          (PIECE_TOKEN, CHECKMATE_TOKEN)],
    "PASS_RIVER_COMMAND": [(PIECE_TOKEN, VRP_TOKEN, NUMBER_TOKEN, PASS_RIVER_TOKEN),
                           (PIECE_TOKEN, NUMBER_TOKEN, PASS_RIVER_TOKEN),
                           (PIECE_TOKEN, EXTEND_POSITION_TOKEN, PASS_RIVER_TOKEN),
                           (PIECE_TOKEN, PASS_RIVER_TOKEN),
                           ]
}

STRUCT_TO_COMMAND_TYPE = dict()

for command_type in COMMAND_TYPE_TO_STRUCTS:
    for struct in COMMAND_TYPE_TO_STRUCTS[command_type]:
        STRUCT_TO_COMMAND_TYPE[struct] = command_type

BEAT_TEXT_TO_SYMBOL = {
    'ăn': 'x',
    'bắt': 'x'
}

PASS_RIVER_TEXT_TO_SYMBOL = {
    'qua sông': '.s',
    'sang sông': '.s'
}

CHECKMATE_TEXT_TO_SYMBOL = {
    'chiếu': '+',
    'chiếu tướng': '+'
}

TOKEN_TO_TEXT_TO_SYMBOL = {
    PIECE_TOKEN: PIECE_TEXT_TO_SYMBOL,
    NUMBER_TOKEN: NUMBER_TEXT_TO_SYMBOL,
    BEAT_TOKEN: BEAT_TEXT_TO_SYMBOL,
    VRP_TOKEN: VRP_TEXT_TO_SYMBOL,
    EXTEND_POSITION_TOKEN: EXTEND_POSITION_TEXT_TO_SYMBOL,
    PASS_RIVER_TOKEN: PASS_RIVER_TEXT_TO_SYMBOL,
    CHECKMATE_TOKEN: CHECKMATE_TEXT_TO_SYMBOL,
    META_TOKEN: META_COMMAND_TEXT_TO_SYMBOL,
    NORM_OP_TOKEN: NORM_OP_TEXT_TO_SYMBOL,
}