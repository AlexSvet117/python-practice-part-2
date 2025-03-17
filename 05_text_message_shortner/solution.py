# do not change the method name
def main():
    pass # replace with your code

###Enter a message: Hey, I'll meet you at the coffee shop for lunch with Sarah.
# Original message (59 chars): Hey, I'll meet you at the coffee shop for lunch with Sarah.
# Shortened message (54 chars): Hey, I'll meet you @ the coffee shop 4 lunch w/ Sarah.
# You saved 5 characters!
message = input("Enter a message:")


shortenned_message = message.replace("with", "w/")
shortenned_message = shortenned_message.replace("for", "4")
shortenned_message = shortenned_message.replace("to", "2")
shortenned_message = shortenned_message.replace("and", "&")
shortenned_message = shortenned_message.replace("at", "@")

if len(shortenned_message) > 160:
    shortenned_message = shortenned_message[0:157] + "..."

shortenned_message = shortenned_message[0].upper() + shortenned_message[1:160]

message_length = len(message)
shortenned_message_length = len(shortenned_message)
char_saved = message_length - shortenned_message_length

print(f"Original message ({message} chars): {message}")
print(f"Shortened message ({shortenned_message_length} chars): {shortenned_message}")
print(f"You saved {char_saved} characters!")
# do not change the following lines:
main()
