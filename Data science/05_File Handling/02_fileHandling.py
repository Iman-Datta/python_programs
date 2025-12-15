# Reading from a file
with open("text.txt", "r", encoding="utf-8") as f:
    print(f.read())
# File is automatically closed here


# Writing to a file
s = "I am Iman"
with open("iman.txt", "w", encoding="utf-8") as f:
    f.write(s)
# File is automatically closed here
