# Convert :) to Emoji
def replace_emoticons(text):
    emoticons = {':)': '🙂', ':(': '🙁'}
    for emoticon, emoji in emoticons.items():
        text = text.replace(emoticon, emoji)
    return text

def main():
    user_input = input(" ")
    output = replace_emoticons(user_input)
    print(output)

if __name__ == "__main__":
    main()


#All CAPS to normal size text
def main():
    x = input("")
    print(lowerCase(x))

def lowerCase(str):
    return str.lower()

main()

#Change spaces to "..."
def main():
    x = input("").replace(" ", "...")
    print(x)

main()

#Einstein E=mc2
def main():
    x = input("m: ")
    x = int(x)
    c = 300000000
    c = c**2
    e = x * c
    print("E:", e)

main()

#Tip Calculator
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    amount = float(d.replace('$', ''))
    return amount

def percent_to_float(p):
    # TODO
    percent = float(p.replace('%', ''))
    return percent/100


main()
