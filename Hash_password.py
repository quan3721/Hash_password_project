# ------- PASSWORD HASHING ------- #

# -- import library -- #
import bcrypt

# -- create a password -- #
password = b"thisismypassword" # b : to convert into byte

# -- generate password to salt -- #
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print(hashed)

# -- Create an input data for password -- #
entered_password = input('Enter password to login: ')
entered_password = bytes(entered_password, encoding='utf-8') # -- convert password above into byte

# -- check the value of password have just entered with the value password hashed -- #
if bcrypt.checkpw(entered_password, hashed):
    print('Login successful')
else:
    print('Invalid password')
