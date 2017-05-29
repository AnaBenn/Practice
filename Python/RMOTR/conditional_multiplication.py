def conditional_multiplication(a_condition, number):
    if a_condition == True:
        print(number * 10)
    elif a_condition == False:
        print(number * 1)
    else:
        print('You did not enter a condition and/or number')

#conditional_multiplication(True, 5)