''' Creator: Jan C. Rubio
    Course: ECE464K
    Semester: Spring 2023
    Date: 3/22/23 '''

import pathlib
import re

# provide location of i-tests
inline_path = pathlib.Path("../jan_inline_tests/")

# iterate through all i-tests in path
for inline in inline_path.iterdir():
    if(inline.is_file()):

        # extract the absolute path of the i-test
        inline_test = f"{inline}"

        # open the i-test
        file_ptr = open(inline_test, "r")

        print(inline_test + ":")

        # find the line of interest ("Here()")
        file_lines = file_ptr.readlines()
        inline_done = False # multiple line statement
        for line in file_lines:
            line = line.strip()
            if(inline_done):
                print(line)
                inline_done = False
                if(line[len(line) - 1] != ")"):
                    inline_done = True
            elif(re.search("Here\(\)", line)):
                print(line)
                if(line[len(line) - 1] != ")"):
                    inline_done = True

        print()

        # close the i-test
        file_ptr.close()
