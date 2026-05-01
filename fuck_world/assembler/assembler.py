import riscv

class Assembler:
    def __init__(self):
        self.file_reader = riscv.FileReader()
        self.lexer = riscv.Lexer()

    def run(self, file_path):
        print("run Assembler")
        
        lines = self.file_reader.read(file_path)
        tokenized_lines = self.lexer.tokenize(lines)
        for token in tokenized_lines:
            if isinstance(token, riscv.Token): # 실제 토큰 객체만 출력
                print(f"{token.value:<15} | {token.type:<12} | {token.lines}")

if __name__ == "__main__":
    asm = Assembler()
    asm.run(r"C:\Data\suck\test\agent.txt")