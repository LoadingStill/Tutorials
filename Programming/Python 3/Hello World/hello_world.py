# This is a simple "Hello, World!" program in Python.
# Comments in Python start with the '#' symbol.

# Define a function called "main". Functions are reusable blocks of code.
def main():
    # Inside the "main" function, we use the "print()" function to display output.
    # Here, we are printing the string "Hello, World!" to the console.
    print("Hello, World!")

# The following block of code checks whether this script is being run directly.
# When you execute this Python file, the special variable "__name__" is set to "__main__".
# This if condition ensures that the "main()" function is only executed when run directly.
if __name__ == "__main__":
    # If this script is being run directly, call the "main()" function.
    main()
