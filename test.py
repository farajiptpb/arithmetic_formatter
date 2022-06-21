primary = list()
problems = ['33+44224', '22222+   99', '23423  - 3122']

for problem in problems:
    if '+' in problem:
        p = problem.split('+')
        p[0] = p[0].strip()
        p[1] = p[1].strip()
    else:
        p = problem.split('-')
        p[0] = p[0].strip()
        p[1] = p[1].strip()

    primary.append(p)

dashes = {}
for pair in primary:

    dash_nums = max(len(pair[0]), len(pair[1])) + 2
    dashes[f'd{primary.index(pair)}'] = dash_nums * '-'


four_spaces = '    '
dashes_row = ''
for i in dashes.values():

    dashes_row = dashes_row + f"{i}{four_spaces}"


first_operands = []
second_operands = []
for i in primary:
    first_operands.append(i[0])
    second_operands.append(i[1])


d = dashes_row.split()
first_operands_row = ''
for num in first_operands:
    fr_space_num = (len(d[first_operands.index(num)]) - len(num))*' '
    first_operands_row = first_operands_row + f"{fr_space_num}{num}{four_spaces}"


second_operands_row = ''
for num in second_operands:
    sr_space_num = (len(d[second_operands.index(num)]) - len(num) - 1)*' '
    second_operands_row = second_operands_row + f"+{sr_space_num}{num}{four_spaces}"

print(f"{first_operands_row}\n{second_operands_row}\n{dashes_row}")