#Task 1
#Define a function to print a hroizontal line of the grid
def print_horizontal_line():
    #Print the left border of the grid and four horizontal dashes with spaces in between
    print('+', '- ' * 4, end='')
    #Print the right border of the grid and another set of four hoirzontal dasheswith spaces in between
    print('+', '- ' * 4, end='')
    #Complete the horizontal line with the right border of the grid
    print('+')

#Define a function to print vertical lines of the grid
def print_vertical_lines():
    #Print a vertical bar followed by eight spaces, representing one column
    print('|', ' ' * 8, end='')
    #Print another vertical bar followed by eight spaces for thesecond column
    print('|', ' ' * 8, end='')
    #Complete the row by printing the final vertical bar
    print('|')

#Define a function to print the entire grid
def print_grid():
    #Print the first horizontal line of the grid
    print_horizontal_line()
    #Print four rows of vertical lines to form the body of the grid
    print_vertical_lines()
    print_vertical_lines()
    print_vertical_lines()
    print_vertical_lines()
    #Print the second horizontal line of the grid to separate the rows
    print_horizontal_line()
    print_vertical_lines()
    print_vertical_lines()
    print_vertical_lines()
    print_vertical_lines()
    print_horizontal_line()

#Call the function to print the grid
print_grid()

#Task 2
#Define a function to print a horizontal line of the grid with four columns
def print_horizontal_line_4():
    #Similar to print_horizontal_line, but repeated four times to accomodate four columns
    print('+', '- ' * 4, end='')
    print('+', '- ' * 4, end='')
    print('+', '- ' * 4, end='')
    print('+', '- ' * 4, end='')
    print('+')

#Define a function to print vertical lines of the grid with four columns
def print_vertical_lines_4():
    #Siilar to print_vertical_lines, but repeated four times to accomodate four columns
    print('|', ' ' * 8, end='')
    print('|', ' ' * 8, end='')
    print('|', ' ' * 8, end='')
    print('|', ' ' * 8, end='')
    print('|')

#Define a function to print the entire grid with four rows and four columns
def print_grid_4():
    #Print the first horizontal line of the grid with four columns 
    print_horizontal_line_4()
    #Print sixteen rows of vertical lines to form the body of the grid (four tows times four columns)
    print_vertical_lines_4()
    print_vertical_lines_4()
    print_vertical_lines_4()
    print_vertical_lines_4()
    #Print the second horizontal line of the grid to separate the rows
    print_horizontal_line_4()
    print_vertical_lines_4()
    print_vertical_lines_4()
    print_vertical_lines_4()
    print_vertical_lines_4()
    print_horizontal_line_4()
    print_vertical_lines_4()
    print_vertical_lines_4()
    print_vertical_lines_4()
    print_vertical_lines_4()
    print_horizontal_line_4()
    print_vertical_lines_4()
    print_vertical_lines_4()
    print_vertical_lines_4()
    print_vertical_lines_4()
    print_horizontal_line_4()

#Call the function to print the grid with four rows and four columns
print_grid_4()


