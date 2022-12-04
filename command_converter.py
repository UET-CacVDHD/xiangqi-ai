from collections import defaultdict
from typing import Optional
import re
from constants import META_COMMAND_TEXT_TO_SYMBOL
from constants import TEXT_TO_TYPES, TYPE_TO_TOKENS, STRUCT_TO_COMMAND_TYPE, TOKEN_TO_TEXT_TO_SYMBOL

# TODO: fuzzy matching


def convert_text_to_elements(text: str):
    tokens = text.split()
    dp = [[] for i in range(len(tokens))]
    for i in range(0, len(tokens)):
        for j in range(i, -1, -1):
            if j == 0:
                sub_text = ' '.join(tokens[j: i + 1])
                if sub_text in TEXT_TO_TYPES:
                    for tp in TEXT_TO_TYPES[sub_text]:
                        dp[i].append([(TYPE_TO_TOKENS[tp], sub_text)])
            else:
                sub_text = ' '.join(tokens[j: i + 1])
                if sub_text in TEXT_TO_TYPES:
                    for prefix_types in dp[j - 1]:
                        for tp in TEXT_TO_TYPES[sub_text]:
                            dp[i].append(prefix_types + [(TYPE_TO_TOKENS[tp], sub_text)])
    return [tuple(parsed_text) for parsed_text in dp[-1]]


def convert_text_to_command(text: str):
    try:
        list_parsed_text = convert_text_to_elements(text)
    except:
        return "undefined"
    for parsed_text in list_parsed_text:
        tokens = tuple([elem[0] for elem in parsed_text])
        if tokens in STRUCT_TO_COMMAND_TYPE:
            texts = [elem[1] for elem in parsed_text]
            command = [TOKEN_TO_TEXT_TO_SYMBOL[tokens[i]][texts[i]] for i in range(len(texts))]
            return ''.join(command)
        else:
            continue
    return "undefined"


if __name__ == "__main__":
    # print(convert_text_to_elements("xe trước giữa một tiến hai"))
    print(convert_text_to_command("xe trước giữa một tiến hai"))
    # print(convert_text_to_elements("xe một tiến hai"))
    # print(convert_text_to_elements("xe tiến hai"))
    print(convert_text_to_command("đầu hàng"))
    # print(convert_text_to_elements("tốt trước giữa một sang sông"))
    # print(convert_text_to_elements("xe trước một chiếu tướng năm"))
    # print(convert_text_to_elements("xe ăn tượng"))
