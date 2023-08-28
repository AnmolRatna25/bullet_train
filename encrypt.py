from cryptography.fernet import Fernet
import json
import os

encryption_key = b'your-32-byte-encryption-key'

def encrypt_data(data):
    cipher_suite = Fernet(encryption_key)
    encrypted_data = cipher_suite.encrypt(data.encode())
    return encrypted_data

# Assuming your JSON files are in a directory named 'json_files'
json_files_directory = 'json_files'
encrypted_files_directory = 'encrypted_files'

if not os.path.exists(encrypted_files_directory):
    os.makedirs(encrypted_files_directory)

for filename in os.listdir(json_files_directory):
    if filename.endswith('.json'):
        with open(os.path.join(json_files_directory, filename), 'r') as file:
            json_data = json.load(file)
            encrypted_data = encrypt_data(json.dumps(json_data))
            encrypted_filename = os.path.join(encrypted_files_directory, filename.replace('.json', '.bin'))
            with open(encrypted_filename, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)
