# privacy_guard_app/utils.py

from cryptography.fernet import Fernet

# Generate a new encryption key
def generate_key():
    return Fernet.generate_key()

# Initialize the Fernet cipher
def initialize_cipher(key):
    return Fernet(key)

# Encrypt data
def encrypt_data(cipher, data):
    return cipher.encrypt(data.encode())

# Decrypt data
def decrypt_data(cipher, encrypted_data):
    return cipher.decrypt(encrypted_data).decode()
