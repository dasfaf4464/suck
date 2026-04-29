from typing import List
from dataclasses import dataclass


@dataclass
class Token:
    type: str
    value: str
    lines: int
    column: int


class Lexer:
    def __init__(self):
        self.tokenized_line = [List]

    def tokenize(self, lines: list[str]) -> list[List[Token]]:
        for line in lines:
            line.splitlines()


if __name__ == "__main__":
    lx = Lexer()
    lines = ["addi x1, 3, x2", ".text: characters is not to be in here", ""]
    lx.tokenize(lines)
