# do not change the method name
def main():
    pass # replace this line with your code

email_address = input("Enter an email address:")

if "@" not in email_address:
    print("Email must contain an @ symbol")
elif email_address.count("@") > 1:
    print("Email must contain only one @ symbol")
elif email_address[0] == "@":
    print("Email must have characters before the @ symbol")
elif "." not in email_address[email_address.find("@"):]:
    print("Email must have a domain with a period after the @ symbol")
elif " " in email_address:
    print("Email cannot contain spaces")
else: 
    print("Valid email address!")


# do not change the following lines:
main()