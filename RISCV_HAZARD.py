import random
import sys

def generate_riscv_instructions(num_instructions):
    riscv_instructions = []

    registers = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10', 'x11']
    load_store_instructions = ['lw', 'sw']
    arithmetic_instructions = ['add', 'sub', 'mul', 'div']

    for i in range(num_instructions):
        instr_type = random.choice(['arithmetic', 'load_store'])
        if instr_type == 'arithmetic':
            instr = random.choice(arithmetic_instructions)
            rd = random.choice(registers)
            rs1 = random.choice(registers)
            rs2 = random.choice(registers)
            riscv_instructions.append(f"{instr} {rd}, {rs1}, {rs2}")
        elif instr_type == 'load_store':
            instr = random.choice(load_store_instructions)
            rd = random.choice(registers)
            rs1 = random.choice(registers)
            offset = random.randint(0, 100)
            riscv_instructions.append(f"{instr} {rd}, {offset}({rs1})")

    return riscv_instructions

def generate_dependent_instructions(instructions):
    dependent_instructions = []
    num_instructions = len(instructions)

    for i in range(num_instructions):
        instr = instructions[i]
        tokens = instr.split()
        instr_type = tokens[0]
        if instr_type in ['lw', 'add', 'sub']:
            # For RAW and WAR hazards, we can use the same register for both source and destination
            rd = tokens[1]
            rs1 = rd
            rs2 = random.choice(tokens[2:])
            dependent_instructions.append(f"{instr_type} {rd}, {rs1}, {rs2}")
        elif instr_type in ['sw']:
            # For WAW hazard, we need to ensure different destination registers for the same instruction type
            rd = f"x{i+10}"
            rs1 = random.choice(tokens[2:])
            rs2 = random.choice(tokens[2:])
            dependent_instructions.append(f"{instr_type} {rd}, {rs1}, {rs2}")

    return dependent_instructions

if __name__ == "__main__":
    num_instructions = int(sys.argv[1])
    original_instructions = generate_riscv_instructions(num_instructions)
    print("Original Instructions:")
    for instr in original_instructions:
        print(instr)

    dependent_instructions = generate_dependent_instructions(original_instructions)
    print("\nDependent Instructions (Hazards):")
    for instr in dependent_instructions:
        print(instr)

