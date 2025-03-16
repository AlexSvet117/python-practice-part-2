# do not change the method name
def main():
    # your solution goes here
    # your solution goes here
    pass # remove this line with your code, this is here just to have the IDE not complaining

phone_number = input("Enter a 10-digit phone number, no spaces, special characters or spaces:")

correct = len(phone_number) == 10 and phone_number.isdigit()
correct or print("Error: Please enter exactly 10 digits. No spaces, special characters and alphabetical characters.") or exit()

print(f"Formatted Phone Number: ({phone_number[:3]}) {phone_number[3:6]}-{phone_number[6:]}")
# do not change the code below
if __name__ == "__main__":
    main()