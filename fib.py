
##################################################
## Calculate nth Fibonacci number based on user input

##################################################
## Author: Allison Plourde
##################################################

def calculate_fib(n):
    """ uses Binet's formula to calculate the nth Fibonnaci number

    Keyword arguments:
    n -- nth value of the Fibonacci sequence (Int)
    
    Output:
    fib_n -- value of nth Fibonnacci number (Int)
    """
    #formula for the golden ratio
    sigma = (1 + 5**0.5) / (2)

    try:
        fib_n = (sigma**n - (-1*sigma)**(-1*n)) / (2*sigma -1)
    except OverflowError:
        print("ERROR: Number entered was too large, please try a number less than 1000")
        print("Exiting program...")
        exit()
    
    return int(fib_n)

def check_user_input(val):
    """ checks if user input is int, float or string
    all inputs that are not int or float default to string

    Keyword arguments:
    val -- user input value (String)
    
    Output:
    t(val) -- int, float, or str
    """

    types = [int, float, str]
    for typ in types:
        try:
            return typ(val), typ
        except ValueError:
            pass


if __name__=="__main__":

    #get desired n value, requires user to enter integer
    n = input('Enter the nth Fibonacci number you are looking for:  ')

    n, type_n = check_user_input(n)
    if type_n != int:
        print("ERROR: an integer value is required, not type {}".format(type(n)))
        print("Exiting program...")
        exit()
    
    #prevent large number input
    if n > 1000:
        print("WARNING! Fibonacci values greater than 1000 are not " \
                 "recommanded and may cause the program to crash.")
        x = input("Enter Y to attempt to run the program anyway, enter anything else to exit:  ")
        if x.lower() == 'y':
            print("Running program anyway...")
        else:
            print("Exiting program...")
            exit()


    #get nth Fibonacci number
    fib_n = calculate_fib(n)

    #output result to command line
    print("The Fibonacci number located at {} is: {}".format(n,fib_n))
