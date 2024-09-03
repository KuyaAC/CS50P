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
