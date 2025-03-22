import re

class Regex_Checker:
    def __init__(self, pattern: str):
        # re.compile() is meant to convert a string into an RE object
        self.pattern = re.compile(pattern)

    def check_input(self, user_input: str):
        if self.pattern.fullmatch(user_input):
            print("Match Successful")
        else:
            print("No Match!!")

if __name__ == "__main__":
    pattern: str = r"a?b?"  # String of the RE format
    checker = Regex_Checker(pattern)
    user_input: str = input("Enter a string to check: ")
    checker.check_input(user_input)

# Quantifier Explanation
# . -> Any letter (a-zA-Z), digit (0-9), or symbol, but just one
# ? -> Means ZERO or EXACTLY one occurrence
# * -> Means ZERO or the same input AT MOST any number of times
# + -> Means AT LEAST one or AT MOST any number of times