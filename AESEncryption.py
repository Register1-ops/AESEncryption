from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)  # Create AES cipher in ECB mode
    padded_text = pad(plaintext.encode(), AES.block_size)  # Pad to multiple of block size
    encrypted = cipher.encrypt(padded_text)
    return base64.b64encode(encrypted).decode('utf-8')  # Return encrypted as base64 string

def aes_decrypt(encrypted, key):
    cipher = AES.new(key, AES.MODE_ECB)  # Create AES cipher in ECB mode
    encrypted_bytes = base64.b64decode(encrypted)  # Decode base64 string
    decrypted = unpad(cipher.decrypt(encrypted_bytes), AES.block_size).decode('utf-8')  # Unpad and decode
    return decrypted

# Example usage:
key = b'Sixteen byte key'  # Key must be 16, 24, or 32 bytes long
message = "Hello, World!"
encrypted = aes_encrypt(message, key)
print(f"Encrypted (AES): {encrypted}")
decrypted = aes_decrypt(encrypted, key)
print(f"Decrypted (AES): {decrypted}")
