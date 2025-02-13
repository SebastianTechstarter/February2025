# Ask the user for a string and print out whether this string is a palindrome or not.

palindrome = input("Bitte gib ein Wort ein: ").lower()
reverse = palindrome[::-1]
print(reverse)

if reverse == palindrome:
    print("Das Wort ist ein Palindrom")

else:
    print("Das Wort ist kein Palindrom.")
