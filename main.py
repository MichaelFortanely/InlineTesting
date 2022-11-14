import ast


# class Visitor(ast.NodeVisitor):

#     def visit(self, node):
#         print(node)
#         self.generic_visit(node)

bitwise_ops_classes = ['LShift', 'RShift', 'BitOr', 'BitXor', 'BitAnd', 'Invert']
                        #<<         >>       |         ^         &         ~

def main():
    with open('ast_fun.py') as x:
        code = x.read()

    node = ast.parse(code)
    all_nodes = ast.walk(node)
    for node in all_nodes:
        da_vars = vars(node)
        if node.__class__.__name__ in ['BinOp', 'UnaryOp']:
            operand_name = vars(node)['op']
            as_string = str(operand_name.__class__)
            as_string = as_string[as_string.index('\'') + 6:]
            as_string = as_string[:as_string.index('\'')]
            if as_string in bitwise_ops_classes:
                print('Found the operator ' + as_string + ' on line number ' + str(node.lineno))

    # node = ast.parse(code)
    # Visitor().visit(node)



if __name__ == '__main__':
    main()
