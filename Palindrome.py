def is_palindrome(s):
    """
    Check if a given string is a palindrome.
    """
    # Convert string to lowercase for comparison
    s = s.lower()
    # Compare a string with its reverse string
    return s == s[::-1]

def main():
    while True:
        user_input = input("Enter a string (or 'exit' to quit): ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        if is_palindrome(user_input):
            print("True")
        else:
            print("False")
        print()

# Chạy chương trình chính
if __name__ == "__main__":
    main()
