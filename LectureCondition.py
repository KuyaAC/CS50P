#Compare program using Conditions
x = int(input("Whats x?"))
y = int(input("Whats y?"))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
else:
    print("x is equal to y")


#Using OR in condition statement
x = int(input("Whats x?"))
y = int(input("Whats y?"))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

#Use Not Equal in condition
x = int(input("Whats x?"))
y = int(input("Whats y?"))

if x != y: #OR you can use "==" and just change the output
    print("x is not equal to y")
else:
    print("x is equal to y")

#And Conditions
score = int(input("Score:""))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

#Modulo demo
x = int(input("Whats x?:"))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

#Example of module in def main
def main():
    x = int(input("Whats x?:"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if x % 2 == 0:
        return True
    else:
        return False

    #can use one liner: (Exclusive to python)
    return True if n % 2 == 0 else False

    #bool return True or False so you can use this code too:
    return n % 2 == 0

main()
