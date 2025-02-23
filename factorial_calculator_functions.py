# John Rey Bulfa
# ITELEC2
# Laboratory #20 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

def main():
    def factorial(n):
        if n == 0:
            return 1
        else:
            result = 1
        for i in range(1, n + 1):
            result *= i
        return result
    n = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {n} is: {factorial(n)}")
if __name__ == "__main__":
    main()