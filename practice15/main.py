import sys

from factorial import factorial

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

    choice = input("Make your choice: ")
    if choice not in "12345678":
        print("Wrong choice!")
        sys.exit(2)
    if choice == "1":
        num = int(input("Enter a natural number: "))
        if num <= 0:
            print("It's not a natural number!")
            sys.exit(2)
        print(f"fact({num}) = {factorial.fact(num)}")
    elif choice == "2":

