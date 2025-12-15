f = open("text.txt", "r", encoding="utf-8") # Open the file "text.txt" in read mode with UTF-8 encoding
print(f.read()) # Read the entire content of the file and print it
f.close() # Close the file to free system resources


s = "I am Iman" # Store a string in a variable
f = open("iman.txt", "w") # Open (or create) the file "iman.txt" in write mode
f.write(s) # Write the string into the file
f.close() # Close the file after writing