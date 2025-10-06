num = int(input("Enter a number:"))
a ,b = 0,1
count = 0
print("Fibonacci series:")
while count < num:
   print(a, end=" ")
   next_num = a+b
   a = b
   b = next_num
   count = count+1