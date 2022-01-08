import random

operators = ['-2', '-1', '0', '1', '2']
operations = ['+', '-', '·', ':']

expressions = []

for operator1 in operators:
    for operation in operations:
        for operator2 in operators:
            expressions.append('{} {} {} = ___'.format(operator1, operation, operator2))
random.shuffle(expressions)

for expression in expressions:
    print(expression)
