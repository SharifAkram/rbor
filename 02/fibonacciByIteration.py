def fibonacci(nthNumber):
    a, b = 1, 1
    print("a = %s, b = %s" % (a, b))
    for i in range(1, nthNumber):
        a, b = b, a + b
        print("a = %s, b = %s" % (a, b))
    return a


print(fibonacci(100))
