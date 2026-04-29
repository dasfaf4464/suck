from riscv import FileReader, Lexer

class Assembler:
    def __init__(self):
        self.file_reader = FileReader()
        self.lexer = Lexer()

    def run(self, file_path):
        print("run Assembler")
        
        lines = self.file_reader.read(file_path)
        tokenized_lines = self.lexer.tokenize(lines)