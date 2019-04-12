class Cipher(object):    
    def format_str(self, text):        
        return text.replace(' ', '').upper() 
        
    def shift_alphabet(self, alphabet, shift):        
        return alphabet[shift:] + alphabet[:shift]

