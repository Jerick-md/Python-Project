#This program Encrypt and Decrypt Tha data
from cryptography.fernet import Fernet
       
class Encrypt():
    #Generating Key for Encryption and decryption
    key = Fernet.generate_key()
    cipher = Fernet(key)
    def __init__(self):
         ask_user = input("Enter a message: ")
         self.convertbytes = ask_user.encode()

    def processOfEncryption(self):
        #Process for encryption
         self.encryption = self.cipher.encrypt(self.convertbytes)
         print("Encrypted message: ", self.encryption)
                
    def processOfDecryption(self):
          #Process for Decryption
         self.decryption = self.cipher.decrypt(self.encryption).decode()
         print("Decrypted message: ", self.decryption)
         
encryp = Encrypt()
encryp.processOfEncryption()      
encryp.processOfDecryption()        
        
        
            