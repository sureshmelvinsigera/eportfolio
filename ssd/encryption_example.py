"""A basic example of encryption using Fernet."""

from cryptography.fernet import Fernet

data = "Text 123 testing testing"

key = Fernet.generate_key()
f = Fernet(key)

encrypted_data = f.encrypt(data.encode()).decode('utf-8')

decrypted_data = f.decrypt(encrypted_data.encode()).decode('utf-8')

print(data)
print(encrypted_data)
print(decrypted_data)
