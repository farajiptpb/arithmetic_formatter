'''I create three rows to solve this project : dashes row, first_operands_row and second_operands_row
'''


def arithmetic_arranger(problems, show_answer=False):
    # primary list contains operands of each problem without operator sign.
    # answers list contains answers of each problem
    answers = list()
    primary = list()
    for problem in problems:
        if '+' in problem:
            p = problem.split('+')
            p[0] = p[0].strip()
            p[1] = p[1].strip()
            answers.append(int(p[0]) + int(p[1]))
        else:
            p = problem.split('-')
            p[0] = p[0].strip()
            p[1] = p[1].strip()
            answers.append(int(p[0]) - int(p[1]))


        primary.append(p)

    # first I create dashes row because I considered dashes row as the basis and origen for other rows.
    # dashes dictionary contains number of dashes needed for particular problem
    dashes = {}
    for pair in primary:
        dash_nums = max(len(pair[0]), len(pair[1])) + 2
        dashes[f'd{primary.index(pair)}'] = dash_nums * '-'

    # creating dashes row
    four_spaces = '    '
    dashes_row = ''
    for i in dashes.values():
        dashes_row = dashes_row + f"{i}{four_spaces}"

    first_operands = []
    second_operands = []
    for i in primary:
        first_operands.append(i[0])
        second_operands.append(i[1])

    # creating first operands row
    d = dashes_row.split()
    first_operands_row = ''
    for num in first_operands:
        index = first_operands.index(num)
        fr_space_num = (len(d[index]) - len(num)) * ' '  # fr stands for first row
        first_operands_row = first_operands_row + f"{fr_space_num}{num}{four_spaces}"

    # creating second operands row
    second_operands_row = ''
    for num in second_operands:
        index = second_operands.index(num)
        if '+' in problems[second_operands.index(num)]:
            sign = '+'
        else:
            sign = '-'
        sr_space_num = (len(d[index]) - len(num) - 1) * ' '  # sr stands for second row
        second_operands_row = second_operands_row + f"{sign}{sr_space_num}{num}{four_spaces}"

        # creating answers row

    answers_row = ''
    for num in answers:
        index = answers.index(num)
        ar_space_num = (len(d[index]) - len(str((num)))) * ' '  # ar stands for answers row
        answers_row = answers_row + f"{ar_space_num}{str(num)}{four_spaces}"

    if show_answer == True:
        print(f"{first_operands_row}\n{second_operands_row}\n{dashes_row}\n{answers_row}")
    else:
        print(f"{first_operands_row}\n{second_operands_row}\n{dashes_row}")


arithmetic_arranger(['448833+77', '44-777900', '5929 + 1', '1-555555'], show_answer=True)
