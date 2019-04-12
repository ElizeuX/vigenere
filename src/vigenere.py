# -*- coding: utf-8 -*-
from cipher import Cipher
import argparse                        

 
class Vigenere(Cipher):
    
    def __init__(self):
        self.plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
    def repeat_password(self, password, text):        
        if len(password) < len(text):
            new_pass = password * int((len(text)/len(password)))
            if len(new_pass):
                new_pass += password[:len(new_pass)]
            return new_pass.upper()
        return password.upper()
 
    def encrypt(self):    
        password = self.repeat_password(gl_args.key , gl_args.crypt)
        plaintext = self.format_str(gl_args.crypt)
        textout = ''
        for idx, char in enumerate(plaintext.upper()):
            # indice da letra da cifra
            idx_key = self.plain.find(password[idx])
            # gera alfabeto cifrado
            c_alphabet = self.shift_alphabet(self.plain, idx_key) 
            idx_p = self.plain.find(char)
            textout += c_alphabet[idx_p]
 
        return textout
 
    def decrypt(self):        
        password = self.repeat_password(gl_args.key , gl_args.decrypt)
        plaintext = self.format_str(gl_args.decrypt)
        textout = ''
        for idx, char in enumerate(plaintext.upper()):
            # indice da letra da cifra
            idx_key = self.plain.find(password[idx])
            # gera alfabeto cifrado
            c_alphabet = self.shift_alphabet(self.plain, idx_key) 
            idx_p = c_alphabet.find(char)
            textout += self.plain[idx_p] 
        return textout 

    def ParseCommandLine(self):
        
        parser = argparse.ArgumentParser('Python file system hashing .. vigenere')        
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('-c', '--crypt', help="palavra a ser criptografada")
        group.add_argument('-d', '--decrypt',   help="palavra a ser descriptografada")   
        parser.add_argument('-v', "--verbose",  help="allows progress messages to be displayed", action='store_true')
        parser.add_argument('-k', '--key', required=True, help="especifica a palavra-chave")

        global gl_args                

        gl_args = parser.parse_args()           
        
        return

if __name__ == "__main__":
    cifra = Vigenere()
    cifra.ParseCommandLine()

    if gl_args.crypt != None :
        txt_cifrado = cifra.encrypt() 
    else:
        txt_cifrado = cifra.decrypt() 

    print(txt_cifrado)
