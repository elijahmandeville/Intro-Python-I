"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"

print("X is %d, Y is %d, Z is %s" % (x, y, z))

# Use the 'format' string method to print the same thing

txt = "X is {a}, Y is {b}, Z is {c}"

print(txt.format(a=10, b=2.25, c="I like turtles!"))

# Finally, print the same thing using an f-string

print(f"X is {x}, Y is {y}, Z is {z}")
