# do not change the method name
def main():
    pass # remove this line with youir code

text = input("Enter the encoded message:")
step = input("Enter the step size:")

substring = text[::int(step)]

print(f"Decoded Message: {substring}")

# do not change the following lines:    
if __name__ == "__main__":
    main()