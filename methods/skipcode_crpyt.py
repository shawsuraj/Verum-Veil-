from Defs.openai import get_ai_response

class SkipCodeCrypt() :
    def encrypt(message, key) :
        crypt_prompt = "Take the sentence '{0}', and for each pair of consecutive words, add exactly {1} natural-sounding words between them to make the sentence still sound natural. Return the modified sentence.".format(message, key)
        encrypted_message = get_ai_response(crypt_prompt)

        return encrypted_message
    
    def decrypt(self, message, key) :
        return("decrypted message")
    