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
    #First, check if n is greater than 2 as the theorem only applies in this case
    if n > 2:
        #Check if a^n + b^n equals c^n
        if a**n + b**n == c**n:
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn't work.")
    else:
        #If n is not greater than 2, the theorem doesn't apply
        print("No, that doesn't work.")

#Example usage:
check_fermat(3, 2, 4, 2)