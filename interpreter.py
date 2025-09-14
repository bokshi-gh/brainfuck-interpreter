import sys
import array

if len(sys.argv) != 2:
    print("Usage: python interpreter.py <filepath>")
    sys.exit(1)

filepath = sys.argv[1]
with open(filepath, "r") as f:
    file_content = f.read()
    file_content = file_content.replace('\n', '').replace('\r', '')
    file_content_length = len(file_content)

tape_size = 300000
tape = array.array('B', [0] * tape_size)
cell_pointer = 0

user_input = []

instruction_pointer = 0
while instruction_pointer < file_content_length:
    instruction = file_content[instruction_pointer]

    if instruction == '+':
        tape[cell_pointer] = (tape[cell_pointer] + 1) % 256
    elif instruction == '-':
        tape[cell_pointer] = (tape[cell_pointer] - 1) % 256
    elif instruction == '>':
        if cell_pointer < tape_size - 1:
            cell_pointer +=1
    elif instruction == '<':
        if cell_pointer >= 0:
            cell_pointer -=1
    elif instruction == '.':
        ascii_character = chr(tape[cell_pointer])
        print(ascii_character, end='')
    elif instruction == ',':
        if user_input == []:
            user_input = list(input() + '\n')
        tape[cell_pointer] = ord(user_input.pop(0))
    elif instruction == '[':
        if tape[cell_pointer] == 0:
            open_bracket_count = 1
            while open_bracket_count != 0:
                instruction_pointer +=1
                if file_content[instruction_pointer] == '[':
                    open_bracket_count +=1
                elif file_content[instruction_pointer] == ']':
                    open_bracket_count -=1
    elif instruction == ']':
        if tape[cell_pointer] != 0:
            close_bracket_count = 1
            while close_bracket_count != 0:
                instruction_pointer -=1
                if file_content[instruction_pointer] == ']':
                    close_bracket_count +=1
                elif file_content[instruction_pointer] == '[':
                    close_bracket_count -=1

    instruction_pointer +=1
