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

#other way of for loop using LEN and RANGE
students = ["ac", "allen", "carl"]

for i in range(len(students)):
    print(i + 1, students[i])

#using DICT in a loop
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for student in students:
    print(student, students[student], sep=", ")

#bigger usage of dict

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}, #None if there no value to the key
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

#mario
def main():
    print_column(3)

def print_column(height):
    for i in range(height):
        print("#")

    #OR You can use this:
    print("#\n" * height, end="")

#print 3x3 square
def main():
    print_square(3)

def print_square(size):

    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#", end="")
        #for new line
        print()
main()

# or to make it short
def print_square(size):
    for i in range(size):
        print("#" * size)
main()

#for More details obstraction
def main():
    print_square(3)

def print_square(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
