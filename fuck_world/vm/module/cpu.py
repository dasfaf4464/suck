class Register:
    def __init__(self, number:int, byte: int):
        self.id = number # register number
        self.byte = byte # register memorize capacity
        self.memory = [0] * (byte * 8) # Little endian

    def read(self):
        value = ""
        for cell in self.memory:
            value+=str(cell)
        return value
    
    def write(self, value:str):
        self.memory = list(value)


class ControlUnit:
    def __init__(self):
        pass
    
    def fetch():
        pass

    def decode() -> tuple:
        pass

    def excute(command: tuple):
        pass


class ALU:
    def __init__(self):
        pass


class CPU:
    def __init__(self):
        REGI_CAPA = 4    
        self.MDR = Register(None, REGI_CAPA),
        self.MAR = Register(None, REGI_CAPA),
        self.PC = Register(0x1F, REGI_CAPA),
        self.IR = Register()
        self.GPRs = { # General Perpose Registers
            "ZERO": Register(0x00, REGI_CAPA),
            "RA": Register(0x01, REGI_CAPA),
            "SP": Register(0x02, REGI_CAPA),
            "GP": Register(0x03, REGI_CAPA),
            "TP": Register(0x04, REGI_CAPA),
            "T0": Register(0x05, REGI_CAPA),
            "T1": Register(0x06, REGI_CAPA),
            "T2": Register(0x07, REGI_CAPA),
            "FP": Register(0x08, REGI_CAPA),
            "S1": Register(0x09, REGI_CAPA),
            "A1": Register(0x0A, REGI_CAPA),
            "A2": Register(0x0B, REGI_CAPA),
            "A3": Register(0x0C, REGI_CAPA),
            "A4": Register(0x0D, REGI_CAPA),
            "A5": Register(0x0E, REGI_CAPA),
            "A6": Register(0x0F, REGI_CAPA),
            "A7": Register(0x10, REGI_CAPA),
            "S2": Register(0x11, REGI_CAPA),
            "S3": Register(0x12, REGI_CAPA),
            "S4": Register(0x13, REGI_CAPA),
            "S5": Register(0x14, REGI_CAPA),
            "S6": Register(0x15, REGI_CAPA),
            "S7": Register(0x16, REGI_CAPA),
            "S8": Register(0x17, REGI_CAPA),
            "S9": Register(0x18, REGI_CAPA),
            "S10": Register(0x19, REGI_CAPA),
            "S11": Register(0x1A, REGI_CAPA),
            "T3": Register(0x1B, REGI_CAPA),
            "T4": Register(0x1C, REGI_CAPA),
            "T5": Register(0x1D, REGI_CAPA),
            "T6": Register(0x1E, REGI_CAPA),
        }
        self.alu = ALU()
        self.cu = ControlUnit()

        print("cpu ready")
    
    def run_cpu(self,):
        self.cu.fetch()
        decode_operation = self.cu.decode()
        self.cu.excute(decode_operation)

    def broadcast_bus(self):
        pass

    def decode_bus(self, signal):
        pass