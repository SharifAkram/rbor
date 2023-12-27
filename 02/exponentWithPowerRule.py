def exponentWithPowerRule(a, n):
    # determine the operations to be performed.
    opStack = []
    while n > 1:
        if n % 2 == 0:
            opStack.append("square")
            n = n // 2
        elif n % 2 == 1:
            n -= 1
            opStack.append("multiply")

    # perform the operations in reverse order.
    result = a
    while opStack:
        op = opStack.pop()

        if op == "multiply":
            result *= a
        elif op == "square":
            result *= result
    return result


print(exponentWithPowerRule(3, 6))
print(exponentWithPowerRule(10, 3))
print(exponentWithPowerRule(17, 10))
