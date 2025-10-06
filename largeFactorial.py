import sys
sys.set_int_max_str_digits(0)
def mohan(n):
    if n<0:
        return "Factorial is not defined for negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        fact = 1
        for i in range (2, n+1):
            fact = fact * i
        return fact
print(mohan(11910))  # Output: factorial of 11910
  # Output: 1