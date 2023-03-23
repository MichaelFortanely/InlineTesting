def is_keyword(line):
    if line.contains('if' or 'elif' or 'else' or 'for' or 'while' or 'break' or
    'continue' or 'else' or 'def' or 'pass' or 'lambda' or 'return' or 'yield' or 
    'import' or 'from' or 'as' or 'try' or 'except' or 'raise' or 'finally' or 'else'
    or 'assert' or 'async' or 'await' or 'del' or 'global' or 'nonlocal'):
        return 0
    else:
        return 1

def length(line):
    return line.length()

def is_regular_expression(line):
    if line.contains('re.'):
        return 1
    else:
        return 0

def is_mathematical_calculation(line):
    if line.contains('-' or '+' or '*' or '/' or 'math.'):
        return 1
    else:
        return 0 

def is_collection_manipulation(line):
    if line.contains('append ' or 'clear' or 'copy' or 'extend' or 
                    'insert' or 'pop' or 'remove' or 'reverse' or
                    'sort'):
        return 1
    else:
        return 0

def is_string_manipulation(line):
    if line.contains('capitalize' or 'casefold' or 'center' or 'encode'
                    or 'format' or 'join' or 'lower' or 'replace'):
        return 1
    else:
        return 0

def is_bit_manipulation(line):
    if line.contains('&' or '|' or '^' or '~' or '<<' or '>>'):
        return 1
    else:
        return 0

def is_variable_assignment(line):
    if line.count('=') == 1:
        return 1
    else: 
        return 0
