# Define a list with some elements
my_list = [10, 20, 30, 40]

# Index and value to insert
index = 10
value = 99

try:
    # Attempt to assign the value at the specified index
    my_list[index] = value

except IndexError:
    # Catch the IndexError and print the error message
    print("Don't try buffer overflow attacks in Python!")