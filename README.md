# Password Decryption

A simple Python project that showcases how to decrypt encrypted data using the Fernet symmetric encryption method from the cryptography library.

## Features

- Secret key acceptance from user

- Symmetric decryption using Fernet

- Encrypted password acceptance as input

- Decrypts encrypted password

- Displays decrypted password

- Exception handling for wrong keys

## Technologies

- Python

- cryptography

- Fernet

## How it works

1. User enters secret key

2. The program uses the secret key to create a Fernet object

3. The user enters the encrypted password that needs to be decrypted

4. The program now tries to decrypt the encrypted password

5. Successfull key displays decrypted password

6. Wrong key displays a decryption error

The program utilizes the cryptography library's Fernet to decrypt the given encrypted password.

The secret key provided by the user is used to create a Fernet object.

The encrypted password is decrypted using the Fernet key and exception handling is implemented to catch decryption errors.

## Example Output

Welcome to decryption Tool....

Enter the Secret Key:

Enter the Encrypted Password to Decrypt:

Decrypted Password is

For wrong key:

Decryption Failed! : Wrong Key was entered

## Concepts Practiced

- Python imports

- User input

- Symmetric encryption

- Fernet decryption

- Secret keys

- String encoding/decoding

- Exception handling

- Try-except blocks

## Installation

Install cryptography package:

pip install cryptography

## How to Run

1. Ensure Python is installed in your system.

2. Install cryptography package

3. Save the program as Decryption.py

4. Open terminal and navigate to the directory where Decryption.py is saved

5. Type 'python Decryption.py' and hit enter

6. Provide the secret key used during encryption

7. Provide the encrypted password for decryption

## Project Structure

password-decryption-python/
│
├── Decryption.py
└── README.md

## Learning Purpose

This project was created as a beginner Python practice project to showcase the basic concept of decryption and show how encrypted data can be recovered using the correct Fernet secret key.

## Future Improvements

- Create a complete encryption/decryption application

- Secure key storage

- File decryption feature

- Graphical user interface

- Better input validation

## Author

Created as a Python learning project.
