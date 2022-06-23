"""
I create three rows to solve this project :
    dashes row, first_operands_row, second_operands_row and answers_row
"""


def arithmetic_arranger(problems, show_answer=False):
    """
    To raise errors I create errors dictionary.
    When an error occurs program gets 1 to that specific error otherwise it gets 0
    """
    # Errors
    # 1-if number of problems are more than 5 program will rais Error
    errors = dict()
    if len(problems) > 5:
        errors[f'problem_nums'] = 1
    else:
        errors[f'problem_nums'] = 0

    # 2-only addition and subtraction are allowed otherwise program will rais Error
    for i in problems:
        if '*' in i:
            errors[f'operation'] = 1
            break
        elif '/' in i:
            errors[f'operation'] = 1
            break
        else:
            errors[f'operation'] = 0

    # 3- operands must be digits otherwise program will raise Error
    for i in problems:
        if '+' in i:
            p = i.split('+')
        else:
            p = i.split('-')
        try:
            int(p[0])
            int(p[1])
            errors[f'digits'] = 0
        except:
            errors[f'digits'] = 1
            break

    # 4- Numbers cannot be more than four digits otherwise program will raise Error
    for i in problems:
        if '+' in i:
            p = i.split('+')
            p[0] = p[0].strip()
            p[1] = p[1].strip()
        elif '-' in i:
            p = i.split('-')
            p[0] = p[0].strip()
            p[1] = p[1].strip()

        if len(p[0]) > 4 or len(p[1]) > 4:
            errors[f'operand_length'] = 1
            break
        else:
            errors[f'operand_length'] = 0

    if errors['problem_nums'] == 1:
        return "Error: Too many problems."

    elif errors['operation'] == 1:
        return "Error: Operator must be '+' or '-'."

    elif errors['digits'] == 1:
        return "Error: Numbers must only contain digits."

    elif errors['operand_length'] == 1:
        return "Error: Numbers cannot be more than four digits."
    else:
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
        dashes_row = dashes_row.rstrip()

        first_operands = []
        second_operands = []
        for i in primary:
            first_operands.append(i[0])
            second_operands.append(i[1])

        # creating first operands row
        d = dashes_row.split()
        first_operands_row = ''
        index = 0
        for num in first_operands:
            fr_space_num = (len(d[index]) - len(num)) * ' '  # fr stands for first row
            first_operands_row = first_operands_row + f"{fr_space_num}{num}{four_spaces}"
            index = index + 1
        first_operands_row = first_operands_row.rstrip()

        # creating second operands row
        index = 0
        second_operands_row = ''
        for num in second_operands:
            if '+' in problems[second_operands.index(num)]:
                sign = '+'
            else:
                sign = '-'
            sr_space_num = (len(d[index]) - len(num) - 1) * ' '  # sr stands for second row
            second_operands_row = second_operands_row + f"{sign}{sr_space_num}{num}{four_spaces}"
            index = index + 1
        second_operands_row = second_operands_row.rstrip()

        # creating answers row
        index = 0
        answers_row = ''
        for num in answers:
            ar_space_num = (len(d[index]) - len(str((num)))) * ' '  # ar stands for answers row
            answers_row = answers_row + f"{ar_space_num}{str(num)}{four_spaces}"
            index = index + 1
        answers_row = answers_row.rstrip()

        if show_answer == True:
            arranged_problems = f"{first_operands_row}\n{second_operands_row}\n{dashes_row}\n{answers_row}"
        else:
            arranged_problems = f"{first_operands_row}\n{second_operands_row}\n{dashes_row}"

        return arranged_problems


