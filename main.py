"""
This program calculates an employee’s productivity bonus
"""

def CheckInput(name, numShifts, numTransactions, dollarvalue):
  
    if not numShifts.isdigit():
        return f'Error: {numShifts} is not a valid number for shifts'

    if not numTransactions.isdigit():
        return f'Error: {numTransactions} is not a valid number for transactions'

    if not dollarvalue.isdigit():
          return f'Error: {dollarvalue} is not a valid number for dollarvalue'

    Score = int(dollarvalue) / int(numTransactions) / int(numShifts)

    if Score <= 30:
      bonus = 50
    elif Score <= 69:
      bonus = 75
    elif Score <= 199:
      bonus = 100
    else:
      bonus = 200

    return f'{name} gets a bonus of ${bonus}'

name = input("Enter the name of the employee: ")
numShifts = input("Enter the number of shifts: ")
numTransactions = input("Enter the number of transactions: ")
dollarvalue = input("Enter the dollar value of transactions: ")

  # Output:
print(CheckInput(name, numShifts, numTransactions, dollarvalue))
