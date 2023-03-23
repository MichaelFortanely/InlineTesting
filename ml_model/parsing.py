import numpy as np
import os
import pandas as pd


def create_set():
    lines = []
    lines.append(["line_number", "line", "isLOI"])

    # print(os.getcwd())
    # print(os.listdir())

    file_path=os.getcwd() + "/test_classification"
    dir_list= os.listdir(file_path)
    for file_name in dir_list:
        current_path=file_path + "\\" + file_name
        file_list = os.listdir(current_path)
        for file in file_list:
            lines=process_lines(current_path + "\\" + file, lines)
    arr=np.array(lines)
    pd.DataFrame(arr).to_csv("inline_test_set.csv")



def process_user_file(file_name, lines) -> list:
    file = open(file_name, 'r')
    x = file.readlines()
    for i in range(0, len(x)-1):
        current_line = x[i].strip()
        current_line, skip=process_comment(current_line)

        if not skip and "Here()." not in current_line:
            lines.append([i, current_line, 0])
    file.close()
    return lines

def process_lines(file_name, lines) -> list:
    file = open(file_name, 'r')
    x = file.readlines()
    for i in range(0, len(x)-2):
        current_line = x[i].strip()
        next_line = x[i+1]
        current_line, skip=process_comment(current_line)

        if not skip and "Here()." in next_line and not "Here()." in current_line:
            lines.append([i, current_line, 1])
        elif not skip and "Here()." in current_line:
            pass
        elif not skip:
            lines.append([i, current_line, 0])
    if len(x) > 0:
        current_line, skip=process_comment(x[len(x)-1])
        if not "Here()." in current_line and not skip:
            lines.append([len(x) - 1, current_line, 0])
    file.close()
    return lines
    
def process_comment(current_line) -> bool:
    skip=False
    if current_line.rfind("#") != -1:
        if current_line.rfind("#") != 0:
             y=current_line.split('#')
             current_line=y[0]
        else:
            skip=True
    return current_line, skip


create_set()