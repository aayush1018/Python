# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 11:57:47 2024

@author: Aayush
"""

''' Maximum Values of an Arithmetic Experssion
Parenthesize an arithmetic expression to maximize the value.
Input: An arithmatic expression consisting of digits as well as plus, minus and multiplication signs
Output: Add parenthesis to the expression in order to max the value'''

def evaluate(a, b, op):
    """
    Evaluate the expression a op b based on the operator.
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def maximize_expression(s):
    """
    Maximize the value of the arithmetic expression provided in string format.
    
    :param s: A string representation of the arithmetic expression.
    :return: The maximum value obtainable from the expression.
    """
    # Extract numbers and operators from the input string
    numbers = []
    operators = []
    
    for i in range(len(s)):
        if i % 2 == 0:  # even index -> digit
            numbers.append(int(s[i]))  # Convert to integer and add to numbers list
        else:  # odd index -> operator
            operators.append(s[i])  # Add operator to the operators list
    
    n = len(numbers)  # Number of digits in the expression
    
    # Create DP tables for maximum and minimum values
    max_values = [[0] * n for _ in range(n)]
    min_values = [[0] * n for _ in range(n)]
    
    # Initialize the DP tables with the numbers
    for i in range(n):
        max_values[i][i] = numbers[i]  # Single number max is the number itself
        min_values[i][i] = numbers[i]  # Single number min is the number itself

    # Fill the DP tables for all subexpressions
    for length in range(2, n + 1):  # length of the subexpression
        for i in range(n - length + 1):
            j = i + length - 1  # Ending index of the subexpression
            max_result = float('-inf')  # Initialize max result for this subexpression
            min_result = float('inf')    # Initialize min result for this subexpression
            
            # Iterate through all operators in the current subexpression
            for k in range(i, j):  # k is the index of the operator
                op = operators[k]
                
                # Calculate all possible values with this operator
                a = evaluate(max_values[i][k], max_values[k + 1][j], op)
                b = evaluate(max_values[i][k], min_values[k + 1][j], op)
                c = evaluate(min_values[i][k], max_values[k + 1][j], op)
                d = evaluate(min_values[i][k], min_values[k + 1][j], op)
                
                # Update the max and min results for the current subexpression
                max_result = max(max_result, a, b, c, d)
                min_result = min(min_result, a, b, c, d)
            
            # Store the results in the DP tables
            max_values[i][j] = max_result
            min_values[i][j] = min_result

    # The maximum value of the entire expression is in the first row and last column
    return max_values[0][n - 1]

def main():
    """
    Main function to read input and output the maximum value of the expression.
    """
    # Input format: a single line containing the arithmetic expression
    s = input().strip()
    
    # Calculate the maximum value of the expression
    max_value = maximize_expression(s)
    
    # Output format: print the maximum value
    print(max_value)

if __name__ == "__main__":
    main()
