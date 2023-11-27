def arithmagic():
    try:
        step_1 = input("Enter a 3-digit number where the first and last "
                       "digits differ by 2 or more: ")
        if int(step_1) <= 100 or int(step_1) >= 999:
            raise ValueError("The number must be 3 digits long.")
        elif abs(int(step_1[0]) - int(step_1[-1])) < 2:
            raise ValueError("The first number’s first and last digits differ by less than 2.")

        step_2 = input("Enter the reverse of the first number, obtained "
                       "by reading it backwards: ")
        if step_1 != step_2[::-1]:
            raise ValueError("The second number must be the reverse of the first number.")

        step_3 = input("Enter the positive difference of these numbers: ")
        if int(step_3) != abs(int(step_1) - int(step_2)):
            raise ValueError("The third number must be the positive difference of the first two numbers.")

        step_4 = input("Enter the reverse of the previous result: ")
        if step_4 != step_3[::-1]:
            raise ValueError("The fourth number must be the reverse of the third number.")

        print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")
    except ValueError as e:
        print(e)


arithmagic()
