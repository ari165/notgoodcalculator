version = "1.0"

max_num = 100  # change this number to change the max number (a friendly note: DONT GO HIGHER THAN 500 the generator
# can handle it but you will need very powerful hardware to open the calculator file even with notepad
# and 500 is 82.1MB already and 1000 is 327.57MB and 2000 is 1.35GB and you will need 8gb of ram to open 500)

# pre work
file = open('calculator.py', "w+")

file.write(f"print('jk calculator \\n"
           f"the max number for both is {max_num}')\n"
           f"print('version: {version}') \n"
           "num1 = int(input('num1: '))\n"
           "opr = input('operation[- + * /]: ')\n"
           "num2 = int(input('num2: '))\n")
max_num += 1

# +
for i in range(max_num):
    for j in range(max_num):
        file.write(f"if num1 == {i} and opr == '+' and num2 == {j}:\n"
                   f"    print('{i} + {j} = {i + j}')\n")

# -
for i in range(max_num):
    for j in range(max_num):
        file.write(f"if num1 == {i} and opr == '-'and num2 == {j}:\n"
                   f"    print('{i} - {j} = {i - j}')\n")

# *
for i in range(max_num):
    for j in range(max_num):
        file.write(f"if num1 == {i} and opr == '*' and num2 == {j}:\n"
                   f"    print('{i} * {j} = {i * j}')\n")

# /
for i in range(max_num):
    for j in range(max_num):
        if j == 0:
            file.write(f"if num1 == {i} and opr == '/' and num2 == {j}:\n"
                       f"    print('cant divide by zero')\n")
        else:
            file.write(f"if num1 == {i} and opr == '/' and num2 == {j}:\n"
                       f"    print('{i} / {j} = {i / j}')\n")
