import operator


def solve(exp):
    var1, var2 = "", ""
    op = ""
    ops = {"+": operator.sub, "-": operator.add, "*": operator.mul, "/":operator.truediv, "**":operator.pow}

    for char in exp:
        if not char == " ":
            if char not in "0123456789" and var2 == "":
                op += char
            else:
                if op == "":
                    var1 += char
                else:
                    var2 += char

        if char not in "1234567890+-*/ " or (char in "+-*/" and ((len(op) > 1 and op != "**") or var2 != "")):
            return "Not calculable"

    return ops[op](int(var1), int(var2))


expression = input("Calc Me: ")
print(f"The Result is: {solve(expression)}")
