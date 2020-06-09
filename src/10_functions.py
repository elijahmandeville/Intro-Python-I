# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(n):
    if n % 2 == 0:
        print("True")
        return True
    else:
        print("False")
        return False


is_even(8)

# Read a number from the keyboard
num = int(input("Enter a number: "))
# num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

if num % 2 == 0:
    print("Even!")
else:
    print("Odd")
