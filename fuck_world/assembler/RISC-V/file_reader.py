
class FileReader:
    def __init__(self):
        self.lines = []

    def get_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                self.lines = f.readlines()
        except FileNotFoundError:
            print(f"에러: {file_path} 파일을 찾을 수 없습니다.")
        return self.lines

    def preprocess(self):
        processed = []
        for line in self.lines:
            clean_line = line.split("#")[0].strip()

            if clean_line:
                processed.append(clean_line)

        self.lines = processed


if __name__ == "__main__":
    fr = FileReader()
    fr.get_file(r"C:\Data\suck\test\agent.txt")
    fr.preprocess()
    print(fr.lines)
