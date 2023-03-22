

import numpy as np

filename = ""

lines = []
lines.append("line_number", "line", "isLOI")




def process_lines(file_name) -> list:
    lines = []
    file = open(filename, 'r')
    x = file.readlines()
    for i in range(0, len(x)-2):
        next_line = x[i+1]
        if "Here()." in next_line and not "Here()." in x[i]:
            lines.append(i, x[i], 1)
            skip_next = True
        elif "Here()." in x[i]:
            pass
        else:
            lines.append(i, x[i], 0)

    if not "Here()." in x[len(x)-1]:
        lines.append(len(x) - 1, x[len(x)-1], 0)
    
    return lines
    
        


