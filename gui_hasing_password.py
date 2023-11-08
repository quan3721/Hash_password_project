# -- Giao diện for hasing password -- #

# -- Import library -- #
from tkinter import *
import bcrypt

# -- Create a function -- #
def validate(password):
    hash_password = b'$2b$12$Ql7sgr0JqU58BVPeXk7NN./aDS7Y0fhhUgQWJyc1DdOxsCt1LSC.W'
    password = bytes(password, encoding='utf-8')  # -- convert password above into byte

    # -- check the value of password have just entered with the value password hashed -- #
    if bcrypt.checkpw(password, hash_password):
        print('Login successful')
    else:
        print('Invalid password')

# -- Create a new window -- #
root = Tk()
root.geometry("300x300") # -- Size of window : 300x300 ( width x height )

# -- Create an entry for entering data input -- #
password_entry = Entry(root)
password_entry.pack()

# -- Create a button -- #
button = Button(text="validate", command=lambda :validate(password_entry.get()))
button.pack()

# -- Create a loop to show the window -- #
root.mainloop()