import math

# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    maximum = max(num1,num2,num3)
    return maximum

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    minimum = min(num1,num2,num3)
    return minimum

# print(built_in_functions_max(-1,-2,-3))
# print(built_in_functions_min(-1,-2,-3))



# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number <0:
        result = 'Negative'
    elif number>0:
        result ='Positive'
    elif number == 0:
        result = 'Zero'
    return result

print(check_number(-23))
    






# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
#    ```
#    *
#    **
#    ***
#    ****
#    *****
#    ```

def star_shape(rows):
    result = ''
    for i in range(rows+1):
        for j in range(i):
            result += '*'
        result += '\n'
    return result.lstrip().rstrip()
            
print(star_shape(5))
print('\n')
print("*\n**\n***\n****\n*****")



# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    result = ''
    for i in range(1, limit+1):
        if i % 3 == 0:
            result += 'Multiple of 3' + '\n'
        else:
            result += str(i) + '\n'
    return result.rstrip()
print(count_multiples_of_3(5))
    #i % 3 != 0

print("1\n2\nMultiple of 3\n4\n5\nMultiple of 3\n7\n8\nMultiple of 3\n10\n11")





# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    result = 0
    for i in range(start, end + 1) :
        if i % 2 == 0:
            result += i
    return result

print(sum_of_even_numbers(1,10))