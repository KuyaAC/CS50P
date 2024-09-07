#Transpose Camel Case to SNake_case
# Own Answer:
name = input("camelCase: ")
print("snake_case:", end="")
for char in name:
    if char.isupper():
        x = "_" + char.lower()
        print(x ,end="")
    else:
        print(char ,end="")

print()

# AI: (practice doing this kinda code )
def camel_to_snake(name):
 # Initialize an empty result string
    snake_case = ""

# Iterate through each character in the input string
    for char in name:
# Check if the character is uppercase
        if char.isupper():
# Append an underscore and the lowercase version of the character
            snake_case += "_" + char.lower()
        else:
# Append the character as it is
            snake_case += char

    return snake_case

    # Get input from user
name = input("camelCase: ")
    # Convert camelCase to snake_case and print the result
print("snake_case:", camel_to_snake(name))
