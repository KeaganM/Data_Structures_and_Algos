from stack import Stack


# https://www.cs.auckland.ac.nz/compsci105s1c/resources/ProblemSolvingwithAlgorithmsandDataStructures.pdf
# section 3.4.8

class Con:
    def __init__(self, name, pos):
        self.name = name
        self.pos = pos

    def __le__(self, other):
        return self.pos <= other.pos



logical_ops = {
    'NOT': Con('NOT', 0),
    'AND': Con('AND', 1),
    'OR': Con('OR', 2)
}

cal_ops = {
    '*': Con('*', 0),
    '+': Con('+', 1)
}

multi = Con('*', 0)
add = Con('+', 1)



# we convert the structure from an infix format to a postfix format
# ie: a + b * c -> abc*+ (which just says we take bc and multiple them together (bc*) then we take the results and add to a (a<bc* = result>+)
# in this case there are some operators that take precedence
# the same can occur with logical operators; the following are in order of precendence: NOT, AND, OR
# for this situation we may want to utilize a custom structure (priorty stack?)

def infix_to_postfix(tokens, ops, con_ops: dict):
    op_stack = Stack()
    output = []

    for item in tokens:
        if item in ops:
            con = con_ops[item]
            for _ in range(len(op_stack.items())):
                op = op_stack.peek()
                if op in ['(', ')']:
                    break
                stk_con = con_ops[op]
                if stk_con <= con:
                    output.append(op_stack.pop())
            op_stack.push(item)
        elif item == '(':
            op_stack.push(item)
        elif item == ')':
            while op_stack.items():
                op = op_stack.peek()
                if op != '(':
                    output.append(op_stack.pop())
                else:
                    op_stack.pop()
                    break
        else:
            output.append(item)

    while op_stack.items():
        output.append(op_stack.pop())

    return output


def infix_to_postfix_logical_ops(tokens, ops, con_ops: dict):
    op_stack = Stack()
    output = []

    for item in tokens:
        if item in ops:
            con = con_ops[item]
            for _ in range(len(op_stack.items())):
                op = op_stack.peek()
                stk_con = con_ops[op]
                if stk_con <= con:
                    output.append(op_stack.pop())
            op_stack.push(item)
            continue
        if isinstance(item, list):
            output.extend(infix_to_postfix_logical_ops(item, ops, con_ops))
        else:
            output.append(item)

    while op_stack.items():
        output.append(op_stack.pop())

    return output


if __name__ == '__main__':
    t = {
        'database': 'django',
        'table': 'table',
        'columns': ['name', 'age'],
        'conditionals': [
            {'name': 'keagan'}, 'AND', {'color': 'red'}, 'OR', {'color': 'blue'},
            # (({},AND,{}),OR, {}) # to allow for nesting
        ]
    }

    # conditionals = [{'name': 'keagan'}, 'AND', {'color': 'red'}, 'OR', {'color': 'blue'}]
    # output = infix_to_postfix_logical_ops(conditionals, list(logical_ops.keys()), logical_ops)
    # print(output)

    conditionals2 = [[[{'name': 'keagan'}, 'AND', {'name': 'eric'}], 'OR', {'color': 'red'}], 'OR',
                     [{'color': 'blue'}, 'AND', {'color': 'green'}]]
    output6 = infix_to_postfix_logical_ops(conditionals2, list(logical_ops.keys()), logical_ops)
    print(output6)

    # output2 = infix_to_postfix(['A', '*', 'B', '+', 'C', '*', 'D'], ['*', '+'], cal_ops)
    # print(''.join(['A', '*', 'B', '+', 'C', '*', 'D']), ''.join(output2))
    #
    # output3 = infix_to_postfix(['A', '+', 'B', '*', 'C', '+', 'D'], ['*', '+'], cal_ops)
    # print(''.join(['A', '+', 'B', '*', 'C', '+', 'D']), ''.join(output3))
    #
    # output4 = infix_to_postfix(['A', '+', 'B', '+', 'C', '+', 'D'], ['*', '+'], cal_ops)
    # print(''.join(['A', '+', 'B', '+', 'C', '+', 'D']), ''.join(output4))
    #
    output5 = infix_to_postfix(['(', 'A', '+', 'B', ')', '*', '(', 'C', '+', 'D', ')'], ['*', '+'], cal_ops)
    print(''.join(['(', 'A', '+', 'B', ')', '*', '(', 'C', '+', 'D', ')']), ''.join(output5))

    quit()
