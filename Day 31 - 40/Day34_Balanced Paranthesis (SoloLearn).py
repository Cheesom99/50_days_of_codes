# BALANCED PARENTHESES SOLOLEARN
def balanced(expression):
    stack = []
    try:
        for i in expression:
            if i == '(':
                stack.append(i)
            elif i == ')':
                stack.pop()
        if len(stack) == 0:
            print("True")
        else:
            print("False")
    except IndexError:
        print("False")


print(balanced(input()))

