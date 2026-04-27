"""
RISC-V RV32I
operation map
"""

# type
R="r", I="i", U="u", B="b", J="j", S="s"

# category
SHIFTS="shifts", ARITHMETIC="arithmatic", LOGICAL="logical", COMPARE="compare",
BRANCHES="branches", JUMPLINK="jumpandlink", SYNCH="synch", ENVIRONMENT="environment",
CSR="csr", LOADS="loads", STORES="stores"

OPCODE = {
    R: {SHIFTS: ["SLL", "SRL", "SRA"], ARITHMETIC: ["ADD", "SUB"], LOGICAL:["XOR", "OR", "AND"], COMPARE:["SLT", "SLTU"]},
    I: {
        SHIFTS: ["SLLI", "SRLI", "SRAI"], ARITHMETIC: ["ADDI"], LOGICAL:["XORI", "ORI", "ANDI"], COMPARE:["SLTI", "SLTIU"],
        JUMPLINK:["JALR"], SYNCH: {"FENCE", "FENCE.I"}, ENVIRONMENT:["ECALL", "EBREAK"], CSR:["SCRRW", "CSRRS", "SCRRC", "CSRRWI", "CSRRSI", "CSRRCI"],
        LOADS:["LB", "LH", "LBU", "LHU", "LW"]
        },
    U: {ARITHMETIC: ["LUI", "AUIPC"]},
    B: {BRANCHES: ["BEQ", "BNE", "BLT", "BGE", "BLTU", "BGEU"]},
    J: {JUMPLINK: "JAL"},
    S: {STORES:["SB", "SH", "SW"]}
}