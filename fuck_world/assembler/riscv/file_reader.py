class FileReader:
    def __init__(self):
        self.raw_lines = []
        self.processed_lines = []

    def read(self, file_path):
        self.read_file(file_path)
        self.preprocess()

        return self.processed_lines

    def read_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.raw_lines = f.readlines()
        except FileNotFoundError:
            print(f"에러: {file_path} 파일을 찾을 수 없습니다.")

    def preprocess(self):
        """
        remove comment(#) line
        remove carriage return(\r)
        remove space(\t, ' ')
        """
        lines = self.raw_lines
        for line in lines:
            comment = line.split("#")[0]
            carriage = comment.replace("\r", "").replace("\\r", "")
            space = carriage.strip(" ")
            tab = space.strip("\t")
            if tab and tab != "\n":
                self.processed_lines.append(tab)


if __name__ == "__main__":
    fr = FileReader()
    fr.read_file(r"C:\Data\suck\test\preprocess_test.txt")
    fr.preprocess()
    print(fr.raw_lines)
    print(fr.processed_lines)
