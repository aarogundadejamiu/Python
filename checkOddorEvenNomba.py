number = int(input("Which number do you want to check? "))

number = number % 2
if number == 0:
  print("This is an even number")
else:
  print("This is an odd number")