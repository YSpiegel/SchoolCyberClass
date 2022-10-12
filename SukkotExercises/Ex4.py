from collections import defaultdict


def find_program(file_name):
    programs_list = [("py", "Python Pycharm"), ("pdf", "Acrobat Reader"),
                     ("docx", "Microsoft Word"), ("jpg", "Picture Viewer")]
    program_dict = defaultdict(lambda: "Other program")
    for program in programs_list:
        program_dict[program[0]] = program[1]

    ending = ""

    for i in range(len(file_name) - 1, 0, -1):
        if file_name[i] == '.':
            break
        ending = file_name[i] + ending

    return program_dict[ending]


file = input("Enter a file name: ")
print(f"You need {find_program(file)} to open it")
