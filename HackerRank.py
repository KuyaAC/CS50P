# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
#ANSWER:
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 0 and n >= 6 and n <= 20:
        print("Weird")
    elif n % 2 != 0:
        print("Weird")
    else:
        print("Not Weird")

# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
#ANSWER:
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(f"{a + b}")
    print(f"{a - b}")
    print(f"{a * b}")
