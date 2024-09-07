import sys

try:
    x  = int(input("X :"))
    y  = int(input("Y :"))
except ValueError:
    print("Invalid data")
    sys.exit(1)

try:
    result = x/y

except ZeroDivisionError:
    print("Error")
    sys.exit(1)
    
print(result)
