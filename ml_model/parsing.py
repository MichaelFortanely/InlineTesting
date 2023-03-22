import numpy as np


lines = []
lines.append("line_number", "line", "isLOI")


def process_user_file(file_name) -> list:
    lines = []
    file = open(file_name, 'r')
    x = file.readlines()
    for i in range(0, len(x)-1):
        current_line = x[i].strip()
        current_line, skip=process_comment(current_line)

        if not skip and "Here()." not in current_line:
            lines.append(i, current_line, 0)
    file.close()
    return lines

def process_lines(file_name) -> list:
    lines = []
    file = open(file_name, 'r')
    x = file.readlines()
    for i in range(0, len(x)-2):
        current_line = x[i].strip()
        next_line = x[i+1]
        current_line, skip=process_comment(current_line)

        if not skip and "Here()." in next_line and not "Here()." in current_line:
            lines.append(i, current_line, 1)
        elif not skip and "Here()." in current_line:
            pass
        elif not skip:
            lines.append(i, current_line, 0)

    current_line, skip=process_comment(x[len(x)-1])
    if not "Here()." in current_line and not skip:
        lines.append(len(x) - 1, current_line, 0)
    file.close()
    return lines
    
def process_comment(current_line) -> bool:
    if current_line.rfind("#") == -1:
        if current_line.rfind("#") != 0:
             y=current_line.split('#')
             current_line=y[0]
        else:
            skip=True
    return current_line, skip


