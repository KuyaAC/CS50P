#outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

if x == "42" or x == "forty two" or x == "forty-two":
    print("Yes")
else:
    print("No")

#If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.
greet = input("Greeting: ").lower()
words = greet.split()
first_word = words[0]

if first_word.startswith("hello"):
    print("$0")

elif greet[0] == "h":
    print("$20")

else:
    print("$100")

#Check selected file type
type = input("File Type: ").lower()
file = type.rsplit('.', 1)[-1]
file = file.strip()

match file:
    case "gif" | "png":
        print("image/" + file)
    case "jpeg" | "jpg":
        print("image/jpeg")
    case "txt":
        print("text/plain")
    case "pdf" | "zip":
        print("application/" + file)
    case _:
        print("application/octet-stream")

#level up expression using conditions
expression = input("Expression: ")
value = expression.split()
x = float(value[0])
y = value[1]
z = float(value[2])

if y == '/':
    div = f"{x} {y} {z}"
    result = eval(div)
    print(result)

elif y == '*':
    mul = f"{x} {y} {z}"
    result = eval(mul)
    print(result)

elif y == '+':
    add = f"{x} {y} {z}"
    result = eval(add)
    print(result)
else:
    sub = f"{x} {y} {z}"
    result = eval(sub)
    print(result)

#Eating Time conditional
def main():
    timer = input("What time is it? ")
    NewTime = convert(timer)
    if NewTime >= 6 and NewTime <= 9:
        print("breakfast time")
    elif NewTime >= 11 and NewTime <= 13:
        print("lunch time")
    elif NewTime >= 17 and NewTime <= 21:
        print("dinner time")
    else:
        return


def convert(time):
    Stime = time.split(":")
    hr = int(Stime[0])
    min = float(Stime[1])
    NewMin = min / 60
    return hr + NewMin


if __name__ == "__main__":
    main()
