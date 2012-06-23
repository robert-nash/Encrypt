from Tkinter import *

root = Tk()

def main():
    ans = raw_input("Do you want to encrypt or decrypt. (e/d) ")
    
    if ans == "e":
        encode()
    elif ans == "d":
        decode()


# Encoding
def encode():
    word = text.get()
    #Find length of the word
    length = len(word)
    start = 0
    a = 0
    length

    #Generate encrypted word
    while start < length:
        letter = word[start]
        convert1 = start
        start = convert1 +1

        #Give encode_word a value if it is first run.
        if a < 1:
            encode_word = ""
            
        convert2 = a +1
        a = convert2
        number = ord(letter)
        alg = number *2
        encode_char = chr(alg)        
        convert4 = encode_word +encode_char
        encode_word = convert4

    text2.delete(0, END)
    text2.insert(0,encode_word)

    

def decode():
    word = text2.get()
    #Find length of the word
    length = len(word)
    start = 0
    a = 0
    length

    #Generate encrypted word
    while start < length:
        letter = word[start]
        convert1 = start
        start = convert1 +1

        #Give encode_word a value if it is first run.
        if a < 1:
            encode_word = ""
            
        convert2 = a +1
        a = convert2
        number = ord(letter)
        alg = number /2
        encode_char = chr(alg)        
        convert4 = encode_word +encode_char
        encode_word = convert4

    text.delete(0, END)
    text.insert(0, encode_word)


label = Label(root, text="Plain Text:", justify=LEFT)
label.grid(column=1, row=1)

label2 = Label(root, text="Encrypted \nText:", justify=LEFT)
label2.grid(column=1, row=2)

text = Entry(root)
text.grid(column=2, row=1, columnspan=2)

text2 = Entry(root)
text2.grid(column=2, row=2, columnspan=2)


button = Button(root, text="Encrypt", command=encode)
button.grid(column=2, row=3, sticky=W)

button2 = Button(root, text="Decrypt", command=decode)
button2.grid(column=3, row=3)

root.mainloop()

