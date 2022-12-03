from typing import Optional
import re


NORM_OPERATION_LIST = [
    "tiến",
    "tấn",
    "bình",
    "lùi",
    "thoái"
]

PIECE_LIST = [
    'tướng',
    'soái',
    'sĩ',
    'tượng'
    'tịnh',
    'bồ',
    'xe',
    'mã',
    'pháo',
    'tốt',
    'binh',
    'chốt'
]

VRP_LIST = [
    "trước",
    "trước giữa",
    "sau giữa",
    "giữa",
    "sau"
]

NUMBER_LIST = [
    'một',
    'hai',
    'ba',
    'bốn',
    'năm',
    'sáu',
    'bảy',
    'tám',
    'chín'
]



def convert_text_to_elements(text: str):
    pass