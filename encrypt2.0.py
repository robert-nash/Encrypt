def main():
    ans = raw_input("Do you want to encrypt or decrypt. (e/d) ")
    
    if ans == "e":
        encode()
    elif ans == "d":
        decode()


# Encoding
def encode():
    word = raw_input("Please enter the word you want to encrypt.")
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
        alg = number + 6 * 4 / 2
        encode_char = chr(alg)        
        convert4 = encode_word +encode_char
        encode_word = convert4

    print encode_word

    raw_input("Press any key to exit")

def decode():
    word = raw_input("Please enter the word you want to decrypt.")
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
        alg = number * 2 / 4 - 6
        encode_char = chr(alg)        
        convert4 = encode_word +encode_char
        encode_word = convert4

    print encode_word

    raw_input("Press any key to exit")

    

main()        


