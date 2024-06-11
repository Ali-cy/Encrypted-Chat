# Encrypted Chat in Python

This Python project demonstrates an encrypted chat system using RSA encryption for secure communication between two parties over a network.

## Description:

This script establishes a secure communication channel between a host and a client using RSA encryption. The program allows users to either host or connect to a chat session, providing end-to-end encryption for exchanged messages.

## Features:

- **RSA Encryption:** Utilizes the RSA encryption algorithm for secure message transmission.
- **Host or Connect:** Offers the option to either host a chat session or connect to an existing one.
- **Threading:** Utilizes threading to enable simultaneous sending and receiving of encrypted messages.

## Setup:

1. **Run the Script:**
   - Run the Python script (`encrypted_chat.py`).
   - Choose '1' to host or '2' to connect.

2. **Communication:**
   - Upon successful connection, the encrypted chat session begins.
   - Messages are encrypted using RSA encryption before transmission.

## Usage:

- Ensure Python and required libraries are installed.
- Run the script, following the on-screen prompts to host or connect.
- Input messages to communicate securely with the other party.

## Notes:

- The script is designed for practice purposes and may require network configuration adjustments for proper operation.
- The project utilizes Python's `socket`, `threading`, and `rsa` libraries.
- RSA encryption/decryption logic adapted from the `rsa` library.

