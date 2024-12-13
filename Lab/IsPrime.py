"""
We want a program that asks the user for a number and indicates if that number is prime (remember, a number is prime only if it is divisible by 1 or by itself).
"""


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    try:
        num = int(input("Please enter a number: "))
        if is_prime(num):
            print(f"The number {num} is prime.")
        else:
            print(f"The number {num} is not prime.")
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main
