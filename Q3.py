# Decryption function to decrypt the encrypted code
def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key  # Reverse the encryption
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                elif shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                elif shifted > ord('Z'):
                    shifted -= 26
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

# Set the key for decryption
key = 13  # Example key; replace with the correct one if known

# Encrypted code
encrypted_code = "tybony_inevnoyr = 100 z1_qvpg = {'xr11': 'inyhr1', 'xr12': 'inyhr2', 'xr13': 'inyhr3'] qrs cebprff_ahzoref(): tybony tybony_inevnoyr ybpny inevnoyr = 5 ahzoref= [1, 2, 3, 4, 5] juvyr ybpny_inevnoyr > 0: vs ybpny inevnoyr % 2 == 0: ahzoref.erzbir(ybpny_inevnoyr) ybpny inevnoyr -- 1 erghea ahzoref zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1} erfhyg = cebprff_ahzoref(ahzoref=zl_frg) qrs zbqvsl_qvpg(): ybpny_inevnoyr = 10 zl_qvpg['xr14'] = ybpny_inevnoyr zbqvs1_qvpg(5) qrs hcqngr_tybony(): tybony tybony_inevnoyr tybony inevnoyr += 10 sbe v va enatr(5): cevag(v) V += 1 vs zl_frg vf abg Abar naq zl_qvpg['xr14'] == 10: cevag('Pbaqvgvba zrg!') vs 5 abg va zl_qvpg: cevag('5 abg sbhaq va gur qvpgvbanel!') cevag(tybony_inevnoyr) cevag(zl_qvpg) cevag(z1_frg)"

# Decrypt the code
decrypted_code = decrypt(encrypted_code, key)
print(decrypted_code)

# Global variable declaration
global_variable = 100  # Global variable for the program

def process_numbers():
    global global_variable  # Declare global variable for modification
    local_variable = 5  # Local variable for loop control
    numbers = [1, 2, 3, 4, 5]  # List of numbers
    while local_variable > 0:  # Loop until local_variable is 0
        if local_variable % 2 == 0:  # Check if local_variable is even
            numbers.remove(local_variable)  # Remove even numbers from list
        local_variable -= 1  # Decrement local_variable
    return numbers  # Return modified list

my_set = {1, 2, 3, 4, 5}  # Set of numbers (fixed duplicate entries)
result = process_numbers()  # Call the function

def modify_dict():
    local_variable = 10  # Local variable for modification
    my_dict['ke14'] = local_variable  # Modify dictionary with new key-value pair

# Initialize the dictionary
my_dict = {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'} 

# Call the modify_dict function
modify_dict()

def update_global():
    global global_variable  # Declare the global variable
    global_variable += 10  # Increment the global variable
    for i in range(5):  # Loop from 0 to 4
        print(i)  # Print current loop index
    if my_set is not None and my_dict['ke14'] == 10:  # Check condition
        print('Condition met!')  # Print message if condition is met
    if 5 not in my_dict:  # Check if 5 is not a key in the dictionary
        print('5 not found in the dictionary!')  # Print message if not found
    print(global_variable)  # Print the global variable
    print(my_dict)  # Print the dictionary
    print(my_set)  # Print the set

# Call the functions to execute the program
update_global()

