import sys

from factorial import factorial
from exp_root import exponentiation, root
from logarithm import logarithm

if __name__ == '__main__':
    print("Choose function to execute:")
    print("1. Factorial")
    print("2. Exponentiation of 2")
    print("3. Exponentiation of 3")
    print("4. Square root")
    print("5. Cubic root")
    print("6. Logarithm of any base")
    print("7. Natural logarithm")
    print("8. Logarithm of base 10")
    print("---------------------------------------------")

    choice = input("Make your choice: ")
    if choice not in "12345678":
        print("Wrong choice!")
        sys.exit(1)
    if choice == "1":
        num = int(input("Enter a natural number: "))
        if num <= 0:
            print("It's not a natural number!")
            sys.exit(1)
        print(f"fact({num}) = {factorial.fact(num)}")
    elif choice == "2":
        num = float(input("Enter any positive number: "))
        if num < 0:
            print("Number should be positive")
            sys.exit(1)
        print(f"exp2({num}) = {exponentiation.exp2(num)}")    
    elif choice == "3":
        num = float(input("Enter any positive number: "))     
        if num < 0:   
            print("Number should be positive: ")
            sys.exit(1)
        print(f"exp({num}) = {exponentiation.exp3(num)}")         
    elif choice == "4":
        num = float(input("Enter a positive number: "))
        if num <= 0:
             print("Number should be positive and more than zero!")
             sys.exit(1)
        print(f"root2({num}) = {root.root2(num)}")     
    elif choice == "5":
        num = float(input("Enter a positive number: "))
        if num <= 0:
            print("Number should be positive and more than zero!")
            sys.exit(1)
        print(f"root3({num}) = {root.root3(num)}")    
    elif choice == "6":
        num_a = float(input("Enter a number a: "))
        if num_a < 0 and num_a == 1:
            print("Number should be positive, except 1!")
        num_b = float(input("Enter a number b: "))  
        if num_b < 0:
            print("Number should be positive!")  
            sys.exit(1)
        print(f"log({num}) = {logarithm.log(num_a, num_b)}")     
    elif choice == "7":
        num = int(input("Enter a number b: "))
        if num < 0:
            print("Number should be positive!")
            sys.exit(1)
        print(f"log({num}) = {logarithm.ln(num)}") 
    elif choice == "8":
        num = float(input("Enter a number b: "))
        if num < 0:
            print("Number should be positive!")
            sys.exit(1)
        print(f"log({num}) = {logarithm.lg(num)}")
