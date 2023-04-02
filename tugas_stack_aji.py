'''
Nama    : Aji nur cahyo
NIM     : 212102001
Prodi   : Informatika
'''

# No 1
def convert_infix_to_postfix(infix):
    postfix = []
    stack = []
    operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    for token in infix:
        if token.isnumeric():
            postfix.append(token)
        elif token in operators:
            while stack and stack[-1] != '(' and operators.get(token, 0) <= operators.get(stack[-1], 0):
                postfix.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                raise ValueError('Mismatched parentheses')
    
    while stack:
        if stack[-1] == '(':
            raise ValueError('Mismatched parentheses')
        postfix.append(stack.pop())
        
    return postfix

infix = ['(', '8', '/', '2', ')', '+', '6']
postfix = convert_infix_to_postfix(infix)
print(postfix)


# No 2
def evaluate_postfix_notation(postfix):
    stack = []

    for token in postfix:
        if token.isnumeric():  
            stack.append(int(token))
        else:  
            right_operand, left_operand = stack.pop(), stack.pop()
            result = {
                '+': left_operand + right_operand,
                '-': left_operand - right_operand,
                '*': left_operand * right_operand,
                '/': left_operand / right_operand,
                '^': left_operand ** right_operand
            }[token]
            stack.append(result)

    return stack.pop()

postfix = ['7', '2', '-', '6', '*']
result = evaluate_postfix_notation(postfix)
print(result)