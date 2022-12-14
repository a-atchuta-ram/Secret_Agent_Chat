import tkinter as tk
from tkinter import *
from tkinter import messagebox
from random import randint
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog

##k=r"C:\Users\atchu\Documents\Jupyter_nb\otp-tk19.txt"
key_file_name=""
otps=[]

def open_Kyes_file():
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
        
    keysFile.insert('1.0',otps)
    keysFile.config(state=DISABLED)
    
    encryptMessage(otps)
def encryptMessage(otps):
    
    ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #data=keysFile.get('1.0','end')
    #print(data)
    
    otps_loc = otps[0].split(',')
    #print(otps_loc[0])
    #print(otps_loc[1])
    
    
    try:
        ciphertext = ''
        plaintext = plain.get('1.0',tk.END)
        
        for position, character in enumerate(plaintext):
            print (position)
            print(character)
            print(otps_loc[position])
            if character not in ALPHABET:
                ciphertext += character
            else:
                encrypted = (ALPHABET.index(character) + int(otps_loc[position])) % 52
                ciphertext += ALPHABET[encrypted]
                
        enceditor.insert('1.0',ciphertext)
        enceditor.config(state=DISABLED)
        
    except Exception as e:
        print(e)
        pass

def saveEncryptedDataFile():
    myFile=filedialog.asksaveasfile(mode="w",defaultextension='.txt')
    if myFile is None:
        return
    data=enceditor.get('1.0',tk.END)
    myFile.write(data)
    myFile.close()

root = tk.Tk()
width = root.winfo_screenwidth() #1
height = root.winfo_screenheight() # 2
root.geometry("%dx%d" % (width, height))
root.title("Encryption Window")



# In[6]:


tk.Label(root, text="Enter Message to Encrypt").grid(column=1, row=1)
plain=tk.Text(root,height=6,width=24)
plain.focus()
plain.grid(column=2, row=1)

tk.Button(root, text="Select Keys File to Encrypt",command=open_Kyes_file).grid(column=1, row=2)
keysFile=tk.Text(root,height=6,width=24)
keysFile.grid(column=2, row=2)

tk.Label(root, text="Encrypted Data").grid(column=1, row=3)
enceditor=tk.Text(root,height=12,width=24)
enceditor.grid(column=2, row=3)

#tk.Button(root, text="Encrypt", command=encryptMessage).grid(column=1, row=5)

tk.Button(root, text="Save to file", command=saveEncryptedDataFile).place(x=220,y=450)
               
root.mainloop()


# In[ ]:




