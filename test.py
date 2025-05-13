def calculator(a, b, operation):
    """
    A simple calculator function.

    Parameters:
    a (float): The first number.
    b (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float: The result of the calculation.
    """
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b != 0:
            return a / b
        else:
            raise ValueError("Division by zero is not allowed.")
    else:
        raise ValueError("Invalid operation. Choose from 'add', 'subtract', 'multiply', 'divide'.")

# Example usage:
# result = calculator(10, 5, 'add')
# print(result)  # Output: 15
print('This is a test file for the calculator function.')