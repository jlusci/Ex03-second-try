"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""
import arithmetic 
#import re 

possible_operators = ["+", "-", "*", "/", "pow", "cube", "square", "mod"] 

def invalid_input(user_input):
    if not user_input[0] in possible_operators:
        print "Unrecognized operator"
        return True


def main():
    # Your code goes here
    quit_calculator = False
    while quit_calculator == False:
        user_input = raw_input('> ')
        calculator_input = user_input.split(" ")
        user_math_operator = calculator_input[0]

        if user_math_operator == 'q':
            quit_calculator = True
            return
        elif invalid_input(calculator_input):
            pass
        
        if calculator_input[1].isdigit() == True:
            first_num = int(calculator_input[1])
        else:
            print "Please enter a number"
            continue

        if calculator_input[2].isdigit() == True:
            second_num = int(calculator_input[2])
        else:
            print "Please enter a number"
            continue

        # if user_math_operator == 'q':
        #     quit_calculator = True
        #     return
        if user_math_operator == "+":
            result = arithmetic.add(first_num, second_num)
            print result
            # continue
        elif user_math_operator == "-":
            result = arithmetic.subtract(first_num, second_num)
            print result
        elif user_math_operator == "/":
            result = arithmetic.divide(first_num, second_num)
            print result
        elif user_math_operator == "mod":
            result = arithmetic.mod(first_num, second_num)
            print result
        elif user_math_operator == "pow":
            result = arithmetic.power(first_num, second_num)
            print result
        elif user_math_operator == "*":
            result = arithmetic.multiply(first_num, second_num)
            print result
        elif user_math_operator == "square":
            result = arithmetic.square(first_num, second_num)
            print result
        elif user_math_operator == "cube":
            result = arithmetic.cube(first_num, second_num)
            print result

        # elif user_math_operator == "q":
        #     quit_calculator = True
        #     return 0

        else:
            return 0

#    pass


if __name__ == '__main__':
    main()



    '''
    possible_operators= ["+", "-", "*", "/", "pow", "cube", "square", "mod"] 

    the above array we'll come back to and use dictionary something or other to match
    arrays 
'''