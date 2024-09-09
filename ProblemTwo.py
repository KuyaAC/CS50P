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
