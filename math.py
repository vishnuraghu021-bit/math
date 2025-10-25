#math.py
try:
  a=float(input("enter first number:"))
  b=float(input("enter second number:"))
  print(f"addition: {a+b}")
  print(f"addition: {a-b}")
except ValueError:
  print("Please enter valid numbers.")
  
