DIRECTIONS = {
    "tiến": '.',
    "tấn": '.',
    "bình": '-',
    "lùi": '/',
    "thoái": '/'
}
PIECES = {
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
VRCS = {
    "trước": "t",
    "trước giữa": "tg",
    "sau giữa": "sg",
    "giữa": "g",
    "sau": "s"
}
NUMBERS = {
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

GAME_COMMANDS = {
    "chấp nhận": "ok",
    "xác nhận": "ok",
    "đồng ý": "ok",
    "ok": "ok",
    "hủy bỏ": "ko",
    "từ chối": "ko",
    "đầu hàng": "$",
    "xin hòa": "=",
    "đổi phe": "<>",
    "xin chơi lại": "^",
    "đi lại": "<"
}

PIECE_NAMES = {
    "G": ['tướng', 'soái'],
    'S': ['sĩ'],
    'T': ['tượng', 'tịnh', 'bộ'],
    'X': ['xe'],
    'M': ['mã'],
    'P': ['pháo'],
    'B': ['tốt', 'binh', 'chốt']
}

MOVE_NAMES = {
    '.': ['tiến', 'tấn'],
    '-': ['bình'],
    '/': ['thoái', 'lùi']
}

NUMBER_DICT = {
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

NUMBER_TO_TEXT = {v: k for k, v in NUMBER_DICT.items()}
