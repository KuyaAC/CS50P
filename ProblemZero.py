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
