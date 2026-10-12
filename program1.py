password=input("enter a password:")
has_upper=False
has_lowere=False
has_special=False
special_character="!@#%^&*()_+{};:',.<>?/"
for char in password:
    if char.islower():
        has_upper=True
    elif char.isdigit():
        has_lower=True
    elif char in special_character:
        has_special=True
    if len(password)>=8 and has_upper and has_digit and has_special:
        print(" Invalid password")
        print("Rules")
        print("1.must have minimum 8 charcters ")
        print("2.must contain at least one digit and one special character")
        print("3.must contain atleast one uppercase alphabet")
