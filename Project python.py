f_num = float(input("Введите первое число:"))
s_num = float(input("Введите второе число:"))
oper = input("Введите операцию:")
if oper == "+":
    print(f_num + s_num)
if oper == "-":
    print(f_num - s_num)
if oper == "*":
    print(f_num * s_num)
if oper == "/":
    print(f_num / s_num)
if oper == "^":
    print(f_num**s_num)
else:
    print("Ошибка")
input()
