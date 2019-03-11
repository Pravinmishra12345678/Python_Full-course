error=True
while error:
 try:
  a=int(input("Enter Number:"))
  b=int(input("Enter Another Number:"))
  c=a/b
  print("Result:",c)
  error=False
 except ZeroDivisionError as e:
  print("Error:",e)
  error=True
 except ValueError as e:
  print("Pls Input Integers Only...")
  error = True
 except Exception as e:
  print("Error:",e,type(e))
  error = True
print('End of Program')



