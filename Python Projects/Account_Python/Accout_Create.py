import re
import hashlib
import pickle
from getpass import getpass


def createAccount():
    username = input("Enter Your Username: ")
    return username

def createPassword():
    password = getpass("Enter Your Password: ")
    repeat_pass = getpass("Repeat Your Password: ")
    checkPassword(password)
    if password != repeat_pass:
        raise ValueError("Passwords do not match")
    return password

def checkPassword(password):
    if len(password) > 16 or len(password) < 8:
        raise ValueError("Password must be between 8 and 16 characters")

    uppercase = lowercase = number = symbol = False
    special_characters = "!@#$%^&*()-+?_=,<>'\""
    special_characters = list(special_characters)

    for x in password:
        if x.isupper():
            uppercase = True
        if x.islower():
            lowercase = True
        if x.isnumeric():
            number = True
        if x in special_characters:
            symbol = True
    if not uppercase:
        raise ValueError("Password must contain uppercase letter")
    if not lowercase:
        raise ValueError("Password must contain lowercase letter")
    if not number:
        raise ValueError("Password must contain a number")
    
    if not symbol:
        raise ValueError("Password must contain a symbol")
    
    print("\nGreat! I am satisfied with your password. Lets Create Your email.\n")
                


def CreateEmail():
    email = input("Enter your email: ")
    match = re.match(r"[^@]+@[^@]+\.[^@]+", email)
    if not match:
        raise ValueError("Invalid email address")
    return email


def fl_name():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    full_name = "%s %s" % (first_name, last_name)
    if not first_name or not last_name:
        raise ValueError("Both first and last name are required")
    return full_name


def password_hash(pass_hash):
    pass_hash = hashlib.sha256(pass_hash.encode())
    return pass_hash.hexdigest()




def binary_file(data):
    with open('binary', 'wb') as f:
        pickle.dump(data, f)


username = createAccount()
password = createPassword()
hashed_password = password_hash(password)
email = CreateEmail()
full_name = fl_name()

binary_file({
    'username': username,
    'password': hashed_password,
    'email': email,
    'name': full_name
})

print("Account Created!")





# Open the binary file to read
# with open('binary', 'rb') as f:
#     # Deserialize the data and store it in a new variable
#     data_loaded = pickle.load(f)
#     print(data_loaded)