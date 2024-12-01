# Check If user input number or not
# Check If user input second_number is 0 or not (You can't divide by 0)
while True:
  try:
    first_number = int(input("Please enter a number"))
    second_number = int(input("Please enter a number"))
    print(first_number/second_number)
    break


  except ZeroDivisionError:
    print("You can't divide by zero")
  except ValueError:
    print("You can only enter a number")



# Stop the program from crashing (number = 0)
number = int(input("Please enter a number"))
if number == 0:
  raise Exception("Error MSG")
print(number)