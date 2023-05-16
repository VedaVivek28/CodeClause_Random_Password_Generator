import random
import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a label for the password length
label_length = tk.Label(root, text="Password Length")
label_length.pack()

# Create an entry box for the password length
entry_length = tk.Entry(root)
entry_length.pack()

# Create a button to generate the password
button_generate = tk.Button(root, text="Generate Password")
button_generate.pack()

# Create a label to display the generated password
label_password = tk.Label(root, text="Password")
label_password.pack()

# Create a function to generate the password
def generate_password():
    # Get the length of the password from the entry box
    length = int(entry_length.get())

    # Create a list of characters to use for the password
    characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
                  'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                  '0','1','2','3','4','5','6','7','8','9',
                  '!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']',';',',','.','<','>','/','?', ]

    # Generate a random password
    password = ''
    for i in range(length):
        password += random.choice(characters)

    # Display the password
    label_password.config(text=password)

# Bind the generate button to the generate_password function
button_generate.config(command=generate_password)

# Start the main loop
root.mainloop()