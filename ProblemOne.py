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
