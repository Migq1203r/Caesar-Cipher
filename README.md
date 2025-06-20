# Caesar Cipher Python Script
# 📜 Overview
This Python script implements a Caesar Cipher, a classical encryption technique where each letter in the plaintext is shifted a fixed number of positions in the alphabet.

You can encode (encrypt) or decode (decrypt) messages using a user-defined shift value.

# 🧠 How It Works
Alphabet List: The script uses a custom alphabet list containing lowercase letters from a to z.

**User Input:**

**Choose the action: 'encode' or 'decode'**.

Enter your **message** (text).

Provide a shift number (how many letters forward/backward the alphabet should be shifted).

**Encoding/Decoding:**

For encoding, the script shifts each alphabetical character forward by the shift number.

For decoding, it shifts them backward.

Non-alphabetical characters (numbers, punctuation, spaces, etc.) are preserved as-is.

Restart Option:

After one operation, you can choose to start again or exit.

# ▶️ How to Run
Ensure you have Python installed. Save the script in a .py file and run it from your terminal:

```python caesar_cipher.py```

Follow the prompts in the console to encode or decode your messages.

# 🔐 Example
Input:
```
python caesar_cipher.py

**Type 'encode' to encrypt, type 'decode' to decrypt:**

encode

Type your message:

hello world

Type the shift number:

5
```
Output:
```
Message Encoded:

mjqqt btwqi
```
