from typing import Literal
from dataclasses import dataclass
import re
from table import OPCODE_TABLE, REGISTER_TABLE


@dataclass
class Token:
    type: Literal["mnemonic", "register", "constant", "modifier", "comma", "leftparen", "rightparen", "identifier", "directive", "label", "newline"] | None
    value: str
    lines: int

    # type constants
    MNEMONIC = "mnemonic"
    REGISTER = "register"
    CONSTANT = "constant"
    MODIFIER = "modifier"
    COMMA = "comma"
    LPAREN = "leftparen"
    RPAREN = "rightparen"
    IDENTIFIER = "identifier"

    DIRECTIVE = "directive"
    
    LABEL = "label"

    NEWLINE = "newline"
    
    def __str__(self):
        return f"type:{self.type}, value:{self.value}"


class Lexer:
    def __init__(self):
        self.token_list = [Token]

    def tokenize(self, lines: list[str]) -> list[Token]:
        for line_num, line in enumerate(lines):
            words = Lexer._split_words(line)

            for word in words:
                token = Lexer._wrap_token(word, line_num)
                self.token_list.append(token)

        return self.token_list

    def _split_words(line:str):
        # todo: if string then remain org form,
        # todo: splited by tab and space
        comma = line.replace(",", " , ")
        new_line = comma.replace("\n", " \n ")
        paren = new_line.replace("(", " ( ").replace(")", " ) ")
        
        words = re.split("\t| ", paren)

        return [word for word in words if word]

    def _wrap_token(word:str, line_number:int) -> Token:
        token = Token(None, word, line_number)

        if word in OPCODE_TABLE:
            token.type = Token.MNEMONIC
        elif word in REGISTER_TABLE:
            token.type = Token.REGISTER
        elif re.fullmatch(r"-?+(\d)*", word):
            token.type = Token.CONSTANT
        elif word.startswith('%'):
            token.type = Token.MODIFIER
        elif word == ',':
            token.type = Token.COMMA
        elif word == '(':
            token.type = Token.LPAREN
        elif word == ')':
            token.type = Token.RPAREN
        elif word.startswith('.'):
            token.type = Token.DIRECTIVE
        elif re.fullmatch(r"([a-z]+\d*)*+:", word):
            token.type = Token.LABEL
        elif word == "\n":
            token.type = Token.NEWLINE
        else:
            token.type = Token.IDENTIFIER

        return token


if __name__ == "__main__":
    lx = Lexer()
    
    test_cases = [
        # 1. 기본적인 산술 연산 (쉼표 처리 확인)
        "addi sp, sp, -16",
        
        # 2. 로드/스토어 및 오프셋 (괄호 처리 확인)
        "sw ra, 12(sp)",
        
        # 3. 모디파이어 및 섹션 지시어 (%, . 확인)
        "lui a0, %hi(string1)",
        ".section .rodata",
        
        # 4. 라벨과 함수 호출 (콜론 및 식별자 확인)
        "main:",
        "call printf",
        
        # 5. 복합적인 한 줄
        "addi a1, a1, %lo(string2) # comment test"
    ]

    print(f"{'VALUE':<15} | {'TYPE':<12} | {'LINE'}")
    print("-" * 40)

    # 각 줄별로 토큰화 실행
    tokens = lx.tokenize(test_cases)
    
    # 결과 출력 (첫 번째 요소인 [Token] 클래스 레퍼런스는 제외하고 출력)
    for token in tokens:
        if isinstance(token, Token): # 실제 토큰 객체만 출력
            print(f"{token.value:<15} | {token.type:<12} | {token.lines}")