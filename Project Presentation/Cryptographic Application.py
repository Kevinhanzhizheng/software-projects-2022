#create cryptography module 
from cryptography.fernet import Fernet

#setup symmertric key
print("welcome to use the cryptographic apllication which use the fernet alogorithm to accomplish with")
key =Fernet.generate_key()
print("this is symmetric key",key)

#save key in the file 
with open('key.txt','w') as file:
    file.write("the symmetric key is " + str(key) +"\n")
file.close()

#load key for the file 
with open('key.txt','r') as file:
    load_key =file.read()
file.close()  
print(load_key) 


# try yo encrypt original text
fernet_msg =Fernet(key)
original_text = input("enter your message to encrtpyt or decrypt: ")
encryp_text = fernet_msg.encrypt(original_text.encode())
with open('key.txt','a') as file:
    file.write("the encrypt text is " + str(encryp_text) +"\n")
print("your encrypted msg would be: ",encryp_text)


#try to decrypt text after encrypt
decryted_text = fernet_msg.decrypt(encryp_text).decode()
with open('key.txt','a') as file:
    file.write("the decrypt text is " + str(decryted_text)+"\n")
    
print("your decrypted msg would be: ",decryted_text)

print("the result of all keys and resullt will be showed in key.txt file")


