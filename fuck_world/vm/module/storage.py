class Memory:
    def __init__(self, byte: int):
        self.bits = [0] * (byte * 8)

    def read(self, byte_addr):
        if byte_addr > len(self.bits) / 8:
            print("raise error")

        bit_addr = byte_addr * 8
        byte_arr = self.bits[bit_addr : bit_addr + 8]

        return bin(
            byte_arr[0] * 128
            + byte_arr[1] * 64
            + byte_arr[2] * 32
            + byte_arr[3] * 16
            + byte_arr[4] * 8
            + byte_arr[5] * 4
            + byte_arr[6] * 2
            + byte_arr[7] * 1
        )

    def write(self, byte_addr, value):
        if byte_addr > len(self.bits)/8:
            print("raise error")

        
class Storage:
    def __init__(self):
        pass