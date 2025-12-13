num = int(input("Enter any number: "))
def fact(num):
    factorial = 1
    for i in range (num,1,-1):
         factorial *= i
    return factorial
print(f"Factorial of {num} is: {fact(num)}")


    



       


