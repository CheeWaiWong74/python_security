from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

token = f.encrypt(b'A really secret message. Not for prying eyes.')
print(token)

dcrypt = f.decrypt(token)
print(dcrypt)