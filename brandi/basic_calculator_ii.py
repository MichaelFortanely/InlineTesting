from inline import Here

from collections import deque 

def calculate(self, s):
    def precedence(c):
        return c == '*' or c == '/'
    def toPostfix(s):
        op, post = deque(), ''
        for c in s:
            if c == ' ': continue
            elif c.isdigit(): post += c
            else:
                post += '|'
                while op and precedence(c) <= precedence(op[-1]):
                    post += op.pop()
                op.append(c)
                
        return post + '|' + ''.join(reversed(op))
    
    s, num, i = toPostfix(s), deque(), 0
    while i < len(s):
        if s[i].isdigit():
            j = s.find('|', i+1)
            # inline test here
            Here().given(s, "5|6").given(i, 1).check_eq(j, -1)
            num.append(int(s[i:j]))
            i = j
        else:
            num1, num2 = num.pop(), num.pop()
            if   s[i] == '*': num.append(num2 * num1)
            elif s[i] == '/': num.append(num2 // num1)
            elif s[i] == '+': num.append(num2 + num1)
            elif s[i] == '-': num.append(num2 - num1)
        i += 1

    return num.pop()