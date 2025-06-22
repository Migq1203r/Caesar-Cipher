
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = ""
text = ""
shift = int()
def start():
    global direction
    global text
    global shift
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n ").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    power()
def encrypt():
    cipher_text = ""
    for letter in text:
        if letter in [" ","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","¨","&","*","(",")","[","]","{","}","á","ç","é","í","ó","ú","â","ê","î","ô","û","\\","|",",",".","<",">",":","?","°","/","^","´","`","à","ì","º","-","_","\"","'","+","¹","²","³","£","¢","¬","=","ã","õ","~"]:
            cipher_text += letter
        else:
            index = alphabet.index(letter) + shift # Detecta o index da letra original e soma o shift (avanço)
            index %= len(alphabet)
            cipher_text += alphabet[index] # Pega o alphabet coloca o index de cima e soma na variavel
    print("Message Encoded:")
    print(cipher_text)
    restart()
def decrypt():
    cipher_text = ""
    for letter in text:
        if letter in [" ","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","¨","&","*","(",")","[","]","{","}","á","ç","é","í","ó","ú","â","ê","î","ô","û","\\","|",",",".","<",">",":","?","°","/","^","´","`","à","ì","º","-","_","\"","'","+","¹","²","³","£","¢","¬","=","ã","õ","~"]:
            cipher_text += letter
        else:
            index = alphabet.index(letter) - shift # Detecta o index da letra original e soma o shift (avanço)
            index %= len(alphabet)
            cipher_text += alphabet[index] # Pega o alphabet coloca o index de cima e soma na variavel
    print("Message Decoded:")
    print(cipher_text)
    restart()
def restart():
    print("\nDo you want restart the Caesar Cipher? Type 'Y' for yes and 'N' for no: ")
    restart_input = input(">>> ").lower()
    if restart_input == "y":
        start()
    else:
        print("\nExiting...\n")
def power():
    if direction == "encode":
        encrypt()
    else:
        decrypt()
start()