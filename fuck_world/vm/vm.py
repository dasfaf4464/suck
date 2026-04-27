from .module import CPU, Memory, storage

class VirtualMachine:
    def __init__(self):
        self.memory = Memory(64)  # main memory
        self.cpu = CPU()

        print("vm ready")

    def run(self):
        print("run VM")

        runnig = True
        while runnig:
            self.cpu.run_cpu()

    def broadcast(self):
        pass
