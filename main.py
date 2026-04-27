import sys
from fuck_world import VirtualMachine, Assembler

def main(argv):
    vm = VirtualMachine()
    asm = Assembler()
    
    asm.run(None, None)
    vm.run(None, None)

if __name__ == "__main__":
    main(sys.argv)