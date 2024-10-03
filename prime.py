import math

def main():
    number = int(input("Enter your number: "))

    while number <= 0:
        print("Invalid number, please enter a positive integer.")
        number = int(input("Enter your number: "))

    if number == 1:
        print("1 is not a prime number.")
    else:
        is_prime = True
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

if __name__ == "__main__":
    main()
