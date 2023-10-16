n = int(input("Enter the Year:"))
if (n == 0):
  print("Please Enter the correct year")
elif (n % 4 == 0):
  print(n, " Is Leap Year")
else:
  print(n, "Is Not Leap Year")
  