from typing import Optional
from constants import PIECES, VRCS, NUMBERS, DIRECTIONS
import re


class Command:
    def from_text(self, text: str):
        raise NotImplementedError()


class NormCommand(Command):
    def from_text(self, text: str) -> str:
        commands = ""
        found = False
        for piece in PIECES:
            match_obj = re.search(fr"\b{piece}\b", text)
            if match_obj is not None and match_obj.span()[0] == 0:
                text = text[match_obj.span()[1]:].strip()
                commands = commands + PIECES[piece]
                found = True
                break
        if not found:
            raise Exception("Not found piece")

        vrc_list = list(VRCS.keys())
        vrc_list.sort(reverse=True, key=lambda elem: len(elem))
        for vrc in vrc_list:
            match_obj = re.search(fr"\b{vrc}\b", text)
            if match_obj is not None and match_obj.span()[0] == 0:
                text = text[match_obj.span()[1]:].strip()
                commands = commands + VRCS[vrc]
                break

        for number in NUMBERS:
            match_obj = re.search(fr"\b{number}\b", text)
            if match_obj is not None and match_obj.span()[0] == 0:
                text = text[match_obj.span()[1]:].strip()
                commands = commands + NUMBERS[number]
                break

        found = False
        for direction in DIRECTIONS:
            match_obj = re.search(fr"\b{direction}\b", text)
            if match_obj is not None:
                found = True
                text = text[match_obj.span()[1]:].strip()
                commands = commands + DIRECTIONS[direction]
                break
        if not found:
            raise Exception("Not found direction")

        found = False
        for number in NUMBERS:
            match_obj = re.search(fr"\b{number}\b", text)
            if match_obj is not None and match_obj.span()[0] == 0:
                found = True
                text = text[match_obj.span()[1]:].strip()
                commands = commands + NUMBERS[number]
                break
        if not found:
            raise Exception("Not found destination columns")

        return commands

    s = "xe trước một bình hai"
    from_text(s)


class GameCommand(Command):
    def from_text(self, text: str):
        pass