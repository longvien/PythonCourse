#def greeting(name):               # <--- The function definition
#    print('Hello', name)

# Main program
#input_name = input('Pls enter your name.\n')      # <--- The programm starts running here,
#greeting(input_name)                              # it's called the main body of the program 

#Global Scope
#def greeting():
#    print('Hi ' + str(name))
#name = input('Enter your name:\n')
#greeting()

#Local Scope
#def greeting(name):
#    print('Hi', name)

#name1 = input('Enter your name:\n')
#greeting(name1)
#name2 = input('Enter another name:\n')
#greeting(name2)


def addition(a, b):
    return a - b

def main():
    F_num = float(input('Enter the 1st number:\n'))
    S_num = float(input('Enter the 2nd number:\n'))

    result = addition(F_num, S_num)
    print('The result is:', result)
main()