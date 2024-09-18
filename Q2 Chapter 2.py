# Sample string (your input string)
s = "56aAww1984sktr235270aYmn145ss785fSq31D0"

# Separate numbers and letters
numbers = ''.join([char for char in s if char.isdigit()])
letters = ''.join([char for char in s if char.isalpha()])

# Convert even numbers to ASCII decimal values
even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]
even_numbers_ascii = [ord(str(num)) for num in even_numbers]

# Convert uppercase letters to ASCII decimal values
uppercase_letters = [char for char in letters if char.isupper()]
uppercase_ascii = [ord(char) for char in uppercase_letters]

# Output the results
print(f"Even Numbers: {even_numbers}")
print(f"ASCII Code of Even Numbers: {even_numbers_ascii}")
print(f"Upper-case Letters: {uppercase_letters}")
print(f"ASCII Code of Upper-case Letters: {uppercase_ascii}")

