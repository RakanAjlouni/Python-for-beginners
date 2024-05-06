def is_triangle(a, b, c):
    """
    Function to check if three sticks lengths can form a triangle.

    Parameters:
    a (int): Length of the first stick.
    b (int): Length of the second stick.
    c (int): Length of the third stick.

Returns:
    bool: True if the lengths can form a triangle, False otherwise.
    """
    return (a + b > c) and (a + c > b) and (b + c > a)
    
    
def check_triangle():
    """
    Finction to prompt user for stick lengths and check if they can form a triangle.
    """
    print("Enter the lengths of the sticks to check if they form a triangle:")
    #Prompt the user for sticks lengths
    a = int(input("Enter the length of the first stick: "))
    b = int(input("Enter the length of the second stick: "))
    c = int(input("Enter the length of the third stick: "))

    if is_triangle(a, b, c):
        print("Yes, you can form a triangle with these lengths.")
    else:
        print("No, you cannot form a triangle with these lengths.")


#Call the function to check triangle
check_triangle()
