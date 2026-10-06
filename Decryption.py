from cryptography.fernet import Fernet

print("\nWelcome to decryption Tool....")

saved_key = input("Enter the Secret Key : ").strip()
key = Fernet(saved_key.encode())


input_get = input("\nEnter the Encrypted Password to Decrypt:").strip()

try:
    decrypt = key.decrypt(input_get.encode()).decode()
    print(f'\nDecrypted Password is {decrypt}')
    
except Exception:
    print("\nDecryption Failed! : Wrong Key was entered")