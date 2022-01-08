import random

arguments = ['-2', '-1', '0', '1', '2']
operations = ['+', '-', '·', ':', '^']

expressions = []

for argument1 in arguments:
    for operation in operations:
        for argument2 in arguments:
            expressions.append('{} {} {} = ___'.format(argument1, operation, argument2))
random.shuffle(expressions)

for expression in expressions:
    print(expression)
