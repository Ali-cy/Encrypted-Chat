"""
Coding Encrypted Chat in Python
"""

import socket 
import threading
import rsa

# Generate public and private keys for encryption
publicKey, privateKey = rsa.newkeys(1024)
publicPartner = None  # Initialize public key of the communication partner

# Ask the user if they want to host or connect
choice = input('Do you want to host (1) or to connect (2): ')

# If the user chooses to host
if choice == '1': 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9999))  # Bind the server to a specific IP address and port, IP address is added to ''
    server.listen()

    client, _ = server.accept()  # Accept incoming connections
    client.send(publicKey.save_pkcs1("PEM"))  # Send own public key to the client
    publicPartner = rsa.PublicKey.load_pkcs1(client.recv(1024))  # Receive public key from the client
# If the user chooses to connect
elif choice == '2':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('', 9999))  # Connect to the server, IP address is added to ''
    publicPartner = rsa.PublicKey.load_pkcs1(client.recv(1024))  # Receive public key from the server
    client.send(publicKey.save_pkcs1("PEM"))  # Send own public key to the server
else:
    exit()  # Exit the program if an invalid choice is made

# Function for sending messages to the communication partner
def sendingMessages(c):
    while True:
        message = input("")  # Get user input for the message
        encrypted_message = rsa.encrypt(message.encode(), publicPartner)  # Encrypt the message
        c.send(encrypted_message)  # Send the encrypted message to the partner
        print('You: ' + message)  # Print the sent message

# Function for receiving messages from the communication partner
def receivingMessages(c):
    while True:
        encrypted_message = c.recv(1024)  # Receive encrypted message from the partner
        decrypted_message = rsa.decrypt(encrypted_message, privateKey).decode()  # Decrypt the message
        print('Partner: ' + decrypted_message)  # Print the received message

# Start threads for sending and receiving messages simultaneously
threading.Thread(target=sendingMessages, args=(client,)).start()
threading.Thread(target=receivingMessages, args=(client,)).start()
