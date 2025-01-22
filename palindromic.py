def check_palindrome(word):
    # Convert the word to lowercase to ensure case-insensitivity
    word = word.lower()
    
    # Initialize two pointers: one at the beginning and the other at the end of the word
    left = 0
    right = len(word) - 1
    
    # Check characters from both ends towards the middle
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Take user input
user_word = input("Enter a word: ")

# Check if the word is a palindrome
if check_palindrome(user_word):
    print(f"{user_word} is a palindrome.")
else:
    print(f"{user_word} is not a palindrome.")
