def countDownAndUp(number):
    print(number)
    if number == 0:
        # Base Case
        print("Reached the base case.")
        return
    else:
        # Recursive Case
        countDownAndUp(number - 1)
        print(number, "returning")
        return


countDownAndUp(3)
