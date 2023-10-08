def shortestWithBaseCase(makeRecursiveCall):
    print("shortestWithBaseCase(%s) called." % makeRecursiveCall)
    if not makeRecursiveCall:
        # Base Case
        print("Returning from base case.")
        return
    else:
        # Recursive Case
        shortestWithBaseCase(False)
        print("Returning from recursive case.")
        return


print("Calling shortestWithBaseCase(False):")
shortestWithBaseCase(False)
print()
print("Calling shortestWithBase(True):")
shortestWithBaseCase(True)
