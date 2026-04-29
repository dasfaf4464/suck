import riscv

class Assembler:
    def __init__(self):
        self.file_reader = riscv.FileReader()
        self.lexer = riscv.Lexer()

    def run(self, file_path):
        print("run Assembler")
        
        lines = self.file_reader.read(file_path)
        tokenized_lines = self.lexer.tokenize(lines)