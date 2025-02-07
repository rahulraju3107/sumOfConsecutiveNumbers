limit = int(input("Limit: "))
sum_numbers = 0
number = 1
calculation = ""

while sum_numbers < limit:
    sum_numbers += number
    if calculation:
        calculation += " + "
    calculation += str(number)
    number += 1

print(f"The consecutive sum: {calculation} = {sum_numbers}")

"""
Please write a program which asks the user to type in a limit. 
The program then calculates the sum of consecutive numbers (1 + 2 + 3 + ...) 
until the sum is at least equal to the limit set by the user. 
In addition to the result it should also print out the calculation performed:

Sample output
Limit: 2
The consecutive sum: 1 + 2 = 3

Sample output
Limit: 10
The consecutive sum: 1 + 2 + 3 + 4 = 10
"""