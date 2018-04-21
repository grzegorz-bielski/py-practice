#!/usr/bin/env python

import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

run = True
stateStack = []


def evaluate(chars, oldStack):
    stack = list(oldStack)
    for char in chars:
        if set(char).issubset(set('0123456789.')):
            stack.append(float(char))
        elif char in operators:
            if len(stack) < 2:
                raise ValueError('There must be at least 2 parameters')
            currentOperator = operators[char]
            stack.append(currentOperator(stack.pop(), stack.pop()))
        else:
            raise ValueError('Unknown char %s' % char)
    return stack


def main():
    global run
    global stateStack

    exp = input('> ')
    if exp in ['quit', 'q', 'exit', 'esc']:
        run = False
    elif exp in ['clear', 'empty', 'clr', 'ac']:
        stateStack = []
    else:
        stateStack = evaluate(exp.split(), stateStack)
        print(stateStack)


while run:
    main()
