def check_fermat(a, b, c, n):
    """
    Check whether Fermat's Last Theorem holds for given values of a, b, c, and n.
    
    Fermat's Last Theorem states that there are no three positive integers a, b, and c
    that can satisfy the equation a^n + b^n = c^n for any integer value of n greater than 2.
    
    Parameters:
        a (int): First number.
        b (int): Second number.
        c (int): Third number.
        n (int): The exponent in the equation.
    
    Prints:
        "Holy smokes, Fermat was wrong!" if the equation holds for n > 2.
        "No, that doesn't work." otherwise.
    """
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

def input_and_check_fermat():
    """
    Prompts the user to input values for a, b, c, and n, converts them to integers,
    and checks them using the check_fermat function.
    """
    # Prompt the user for input and convert each input to an integer
    a = int(input("Enter a positive integer for a: "))
    b = int(input("Enter a positive integer for b: "))
    c = int(input("Enter a positive integer for c: "))
    n = int(input("Enter a positive integer for n: "))
    
    # Use the check_fermat function to evaluate the inputs
    check_fermat(a, b, c, n)

# Call the function to run the prompts and checks
input_and_check_fermat()
