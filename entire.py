result = ''
message = ''
choice = ''
 
while choice != '-1':
    choice = input("\nDo you want to encrypt or decrypt the message?\nEnter 1 to Encrypt, 2 to Decrypt, -1 to Exit Program: ")
 
    if choice == '1':
        message = input("\nEnter the message to encrypt: ")
 
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 2)
 
        print (result + '\n\n')
        result = ''
 
    elif choice == '2':
        message = input("\nEnter the message to decrypt: ")
 
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 2)
 
        print (result + '\n\n')
        result = ''
 
    elif choice != '-1':
        print ("You have entered an invalid choice. Please try again.\n\n")

