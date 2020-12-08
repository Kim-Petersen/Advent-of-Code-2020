with open('./boot code.txt') as f:
    boot_code = f.readlines()
    boot_code = [instruction.strip() for instruction in boot_code]


def read_instruction(instruction):
    operation, argument = instruction.split(' ')
    argument = int(argument)

    return operation, argument


def acc(argument, accumulator, position):
    accumulator += argument
    position += 1
    return accumulator, position


def jmp(argument, position):
    position += argument
    return position


def nop(argument, position):
    position += 1
    return position


def execute_boot_code(accumulator, position, instructions_performed, b_c):
    instruction = b_c[position]
    operation, argument = read_instruction(instruction)
    instructions_performed.append(position)
    if 'acc' in operation:
        accumulator, position = acc(argument, accumulator, position)
    elif 'jmp' in operation:
        position = jmp(argument, position)
    elif 'nop' in operation:
        position = nop(argument, position)

    if position in instructions_performed:
        return accumulator, instructions_performed, False
    elif position == len(b_c) - 1:
        return accumulator, instructions_performed, True

    return execute_boot_code(accumulator, position, instructions_performed, b_c)


a, i, t = execute_boot_code(0, 0, [], boot_code)
print(a)

"""
for x in range(0, len(boot_code)):
    boot_code_copy = boot_code.copy()
    if 'jmp' in boot_code[x]:
        boot_code_copy[x] = boot_code_copy[x].replace('jmp', 'nop')
        a, _, t = execute_boot_code(0, 0, [], boot_code_copy)
        if t:
            print(a)
            print(t)
            break
    elif 'nop' in boot_code[x]:
        boot_code_copy[x] = boot_code_copy[x].replace('nop', 'jmp')
        a, _, t = execute_boot_code(0, 0, [], boot_code_copy)
        if t:
            print(a)
            print(t)
            break
"""

while i:
    last_instruction = i.pop()
    boot_code_copy = boot_code.copy()
    if 'jmp' in read_instruction(boot_code[last_instruction]):
        boot_code_copy[last_instruction] = boot_code_copy[last_instruction].replace('jmp', 'nop')
        a, _, t = execute_boot_code(0, 0, [], boot_code_copy)
        if t:
            print(a)
            break
    elif 'nop' in read_instruction(boot_code[last_instruction]):
        boot_code_copy[last_instruction] = boot_code_copy[last_instruction].replace('nop', 'jmp')
        a, _, t = execute_boot_code(0,0, [], boot_code_copy)
        if t:
            print(a)
            break
