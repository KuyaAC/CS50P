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

#COKE vending machine
#AI:
    def coke_exchange():
        COST = 50
        VALID_COINS = {25, 10, 5}
        amount_due = COST
        total_inserted = 0

        while amount_due > 0:
            print(f"Amount Due: {amount_due}")
            try:
                coin = int(input("Insert Coin: "))
                if coin in VALID_COINS:
                    total_inserted += coin
                    amount_due = max(0, COST - total_inserted)
                else:
                    print("Invalid coin.")
            except ValueError:
                print("Invalid input.")

        change = total_inserted - COST
        if change > 0:
            print(f"Change Owed: {change}")
        else:
            print("Thank you!")

    coke_exchange()

#ME:
    def coke_exchange():
        kulang = 50

        while True:
            if kulang > 0:
                print(f"Amount Due: {kulang}")
                pera = int(input("Insert Coin: "))
                while True:
                    if pera == 25 or pera == 10 or pera == 5:
                        kulang -= pera
                        break
                    else:
                        print(f"Amount Due: {kulang}")
                        pera = int(input("Insert Coin: "))
            else:
                kulang = abs(kulang)
                print(f"Change Owed: {kulang}")
                break

    coke_exchange()


#Vowel Remover:
    def v_remover(input_str):
        vowels = 'aeiouAEIOU'

        printer = ""

        for char in input_str:
            if char in vowels:
                printer += ""
            else:
                printer += char

        return printer

    input_string = input("Input: ")
    print(f"Output: {v_remover(input_string)}")

#AI:
    def remove_vowels(text):
        vowels = 'aeiouAEIOU'
        return ''.join(char for char in text if char not in vowels)

    def main():
        user_input = input("Input: ")
        result = remove_vowels(user_input)
        print(f"Output: {result}")

    if __name__ == "__main__":
        main()


#CHECK PLATES: CS50 valid/CS04 invalid...
def main(): #def main to check if valid or not
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length (2-6 characters)
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if it starts with at least two letters
    if not s[:2].isalpha(): #.isalpha to check if 2 char in (s) is string in alphabet
        return False

    # Check for invalid characters (only letters and numbers allowed)
    if not s.isalnum(): #check if in string is alpha numeric
        return False

    # Check number placement
    found_number = False #Initializes a flag to track if a number has been found.
    for char in s:
        if char.isdigit(): #Checks if the current character is a digit.
            if not found_number and char == '0': #If it’s the first digit and is '0', return False (leading zeros are not allowed).
                return False  # First number can't be '0'
            found_number = True
        elif found_number and char.isalpha(): #If a letter is found after a number, return False (letters can’t appear after numbers).
            return False  # No letters after numbers

    return True


main()

#Fruits with corresponding calories
fruits_calories = [
    {"fruit": "Apple", "calories": 130},
    {"fruit": "Avocado", "calories": 50},
    {"fruit": "Banana", "calories": 110},
    {"fruit": "Cantaloupe", "calories": 50},
    {"fruit": "Grapefruit", "calories": 60},
    {"fruit": "Grapes", "calories": 90},
    {"fruit": "Honeydew Melon", "calories": 50},
    {"fruit": "Kiwifruit", "calories": 90},
    {"fruit": "Lemon", "calories": 15},
    {"fruit": "Lime", "calories": 20},
    {"fruit": "Nectarine", "calories": 60},
    {"fruit": "Orange", "calories": 80},
    {"fruit": "Peach", "calories": 60},
    {"fruit": "Pear", "calories": 100},
    {"fruit": "Pineapple", "calories": 50},
    {"fruit": "Plums", "calories": 70},
    {"fruit": "Strawberries", "calories": 50},
    {"fruit": "Sweet Cherries", "calories": 100},
    {"fruit": "Tangerine", "calories": 50},
    {"fruit": "Watermelon", "calories": 80}
]
def get_fruit_calories(fruit_name): #get fruits from dict usign for loop
    for fruit in fruits_calories:
        if fruit["fruit"].lower() == fruit_name.lower():
            return fruit["calories"] #get the calories of chosen fruit
    return None

while True: #output the fruit calorie if the input is correct
    user_input = input("Item: ").strip()

    calories = get_fruit_calories(user_input)

    if calories is not None:
        print(f"Calories: {calories}")
        break
    else:
        break
