# from Defs.openai import get_ai_response
from utils.genai import generate_text

class SkipCodeCrypt() :
    def encrypt(message, key, compress) :
        # crypt_prompt = "Take the sentence '{0}', and for each pair of consecutive words, add exactly {1} natural-sounding words between them to make the sentence still sound natural. Return the modified sentence.".format(message, key)
        encrypted_message = generate_text(message, key)

        print(encrypted_message)

        # encrypted_message['choices'][0]['message']['content'].strip()

        return encrypted_message
    
    def decrypt(self, message, key, compress) :
        return("decrypted message")
    