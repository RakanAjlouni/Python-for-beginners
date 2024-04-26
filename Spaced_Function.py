def right_justify(s):
    """
    Right-justifies the input string by adding leading spaces.
    
    Args:
    - s (str): The input string to be right-justified
    
    Prints the right-jutified string.

    """

#Calculating the number of spaces needed to reach column 70
    spaces_to_add = 70 - len(s)

#Printing the string with leading spaces to reach column 70
    print(' ' * spaces_to_add + s)

    
#Using it in an example:

right_justify("Hello, World!")