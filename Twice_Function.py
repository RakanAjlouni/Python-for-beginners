#Task 1
#Define a function called do_twice that takes another function 'f' as an argumentand calls 'f' twice.

def do_twice(f):
    f() #Calls function 'f' once
    f() #Call function 'f' again

#Define a function named print_spam that prints the word 'spam'
def print_spam():
    print('spam')

#Call the do_twice function with print_spam as the argument, which will print 'spam' twice.
def print_spam():
    print('spam')

# Call the do_twice function with print_spam as the argument, which will print 'spam' twice.
do_twice(print_spam)

#Task 2
# Modify the do_twice function so that it takes two arguments: a function 'f' and a value, and calls the function twice, passing the value as an argument.

def do_twice_modified(f,value):
    f(value) #Call function 'f' with the provided value as an argument.
    f(value) #Call function 'f' again with the same value

#Task 3 
#Define a function named print_twice that prints the given value twice.

def print_twice(value):
    print(value) #Print the value
    print(value) #Print the value again

#Task 4
#Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument.
do_twice_modified(print_twice, 'spam')

#Task 5
#Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter.
def do_four(f, value):
    #Call the modified do_twice function twice, passing the prodvided function 'f' and the value as arguments.
    do_twice_modified(f, value)
    do_twice_modified(f, value)

#Testing Task 5
#Call the do_four function with print_twice and 'spam' as arguments, which will print 'spam' four times.
do_four(print_twice, 'spam')
