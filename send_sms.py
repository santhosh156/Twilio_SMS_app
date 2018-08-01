from twilio.rest import Client
import credentials

client = Client(credentials.account_sid, credentials.auth_token)

choice = input("Do you want to send a message to Santhosh(y/n): ")
while (choice == 'Y') or (choice == 'y'):
    my_msg = input("Enter your message to send: ")
    message = client.messages.create(to=credentials.my_cell, from_=credentials.my_twilio, body=my_msg)
    choice = input("Do you want to send a message to Santhosh(y/n): ")


