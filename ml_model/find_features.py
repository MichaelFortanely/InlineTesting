def is_keyword(line):
    
    keyword_list = ['if', 'elif', 'else', 'for', 'while', 'break',
    'continue', 'else', 'def', 'pass', 'lambda', 'return', 'yield',  
    'import', 'from', 'as', 'try', 'except', 'raise', 'finally', 'else',
    'assert', 'async', 'await', 'del', 'global', 'nonlocal']
    
    if any (m in line for m in keyword_list):
        return 1
    else:
        return 0

def length(line):
    return len(line)

def is_regular_expression(line):
    if ('re.') in line:
        return 1
    else:
        return 0

def is_mathematical_calculation(line):
    
    math_list = ['-', '+', '*', '/', 'math.']
    
    if any (m in line for m in math_list):
        return 1
    else:
        return 0 

def is_collection_manipulation(line):
    
    collection_list = ['append', 'clear', 'copy', 'extend', 'insert', 'pop', 'remove', 'reverse', 'sort'] 
    
    if any (c in line for c in collection_list):
        return 1
    else:
        return 0

def is_string_manipulation(line):
    
    string_list = ['capitalize', 'casefold', 'center', 'encode', 'format', 'join', 'lower', 'replace']
    
    if any (s in line for s in string_list): 
        return 1
    else:
        return 0

def is_bit_manipulation(line):
    
    bit_list = ['&', '|', '^', '~', '<<', '>>']
    
    if any (b in line for b in bit_list):
        return 1
    else:
        return 0

def is_variable_assignment(line):
    if line.count('=') == 1:
        return 1
    else: 
        return 0
