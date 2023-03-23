def is_keyword(line):
    if ('if' or 'elif' or 'else' or 'for' or 'while' or 'break' or
    'continue' or 'else' or 'def' or 'pass' or 'lambda' or 'return' or 'yield' or 
    'import' or 'from' or 'as' or 'try' or 'except' or 'raise' or 'finally' or 'else'
    or 'assert' or 'async' or 'await' or 'del' or 'global' or 'nonlocal' in line):
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
    if '-' or '+' or '*' or '/' or 'math.' in line:
        return 1
    else:
        return 0 

def is_collection_manipulation(line):
    if 'append ' or 'clear' or 'copy' or 'extend' or 'insert' or 'pop' or 'remove' or 'reverse' or 'sort' in line:
        return 1
    else:
        return 0

def is_string_manipulation(line):
    if 'capitalize' or 'casefold' or 'center' or 'encode' or 'format' or 'join' or 'lower' or 'replace' in line:
        return 1
    else:
        return 0

def is_bit_manipulation(line):
    if '&' or '|' or '^' or '~' or '<<' or '>>' in line:
        return 1
    else:
        return 0

def is_variable_assignment(line):
    if line.count('=') == 1:
        return 1
    else: 
        return 0
