#while loop
i = 3
while i != 0:
    print("meow")
    i -= 1

# for loop
for i in [0 , 1 , 2]: #[LIST] Print meow 3 times
    print("meow")

#for improvement
for i in range(100000): #(Can be change with desired number)
    print("meow")

#simple
print("meow\n" * 3, end="")

#Meet input wants
while True:
    n = int(input("what is n?"))
    if n < 0:
        continue
    else:
        break

for i in range(n):
    print("meow")

#OR
while True:
    n = int(input("what is n?"))
    if n > 0:
       break

for i in range(n):
    print("meow")


#using MAIN in for
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if in > 0:
            return n #or break here

    #then "return n"" here

def meow(n):
    for i in range(n):
        print("meow")

#print inside the list using for loop
students = ["ac", "allen", "carl"]

for student in students:
    print(student)
