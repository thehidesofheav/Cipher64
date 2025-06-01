import base64

def caesar_cipher(text, shift):
		result = ""
    for char in text:
    		if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def encrypt_to_base64(text):
    return base64.b64encode(text.encode()).decode()

def encrypt_name(name, shift=3):
    caesar_encrypted = caesar_cipher(name, shift)
    final_encrypted = encrypt_to_base64(caesar_encrypted)
    return final_encrypted

name = "Heav"
encrypted_result = encrypt_name(name)

print(f"Original name: {name}")
print(f"Encrypted result: {encrypted_result}")
