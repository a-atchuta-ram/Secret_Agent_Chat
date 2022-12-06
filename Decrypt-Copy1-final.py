#!/usr/bin/env python
# coding: utf-8

# In[6]:


import tkinter as tk
from tkinter import *
from tkinter import messagebox
from random import randint
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import filedialog as fd


# In[7]:


def open_Keys_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    key_file_name= filedialog.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    
    if key_file_name is None:  # askopenfile() returns `None` if dialog closed with "cancel".
        return
    else:
        otps = key_file_name.read().splitlines()
        
    keysFile.set(otps)
    
    decryptMessage(otps)


# In[8]:


def decryptMessage(otps):
    
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #data=keysFile.get('1.0','end')
    #print(data)
    
    otps_loc = otps[0].split(',')
    print(otps_loc[0])
    print(otps_loc[1])
    
    try:
        plaintext = ''
        ciphertext = cipher.get()
        print(ciphertext)
        for position, character in enumerate(ciphertext):
            if character not in ALPHABET:
                plaintext += character
            else:
                decrypted = (ALPHABET.index(character) - int(otps_loc[position])) % 52
                plaintext += ALPHABET[decrypted]
        deceditor.set(plaintext)
    except ValueError:
        print()
        pass


# In[9]:


def open_text_file():
    # file type
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    # show the open file dialog
    f = filedialog.askopenfile(filetypes=filetypes)
    # read the text file and show its content on the Text
    
    encText = f.read()
    
    cipher.set(encText)


# In[10]:


root = tk.Tk()
root.title("Decryption Window")
root.resizable(False, False)
root.geometry('750x750')

cipher = StringVar()
keysFile = StringVar()
deceditor = StringVar()

#tk.Button(root,text="Choose file to be decrypted").grid(column=1, row=3)

open_button = tk.Button(root,text='Open encrypted Data File',command=open_text_file)
open_button.grid(column=1, row=1,padx=10, pady=10)

tk.Entry(root,textvariable=cipher).grid(column=2, row=1)
#open_button.grid(column=1, row=2, sticky='w', padx=10, pady=10)

tk.Button(root, text="Select Keys File to Decrypt",command=open_Keys_file).grid(column=1, row=2)
tk.Entry(root,textvariable=keysFile).grid(column=3, row=2)


tk.Label(root, text="Decrypted Content").grid(column=1, row=3)
tk.Entry(root,textvariable=deceditor).grid(column=4, row=3)

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




