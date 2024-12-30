# from Defs.openai import get_ai_response
import re
import logging

from utils.genai import generate_text

logger = logging.getLogger(__name__)

class SkipCodeCrypt() :
    def __init__(self):
        pass
    
    def _generate_reference_text(self, message) :
        prompt =  "Generate a natural sounding paragraph of about 50 words that is similar to this text: '{}'. The style should be descriptive.".format(message)
        reference_text = generate_text(prompt)
        logger.info("Reference text: {}".format(reference_text))
        return reference_text
    
    def _verify_insertion_count(self, message: str, encrypted_message: str, k: int) -> bool:
        """Verifies that (key) number of words exists in between each pair of original words"""

        original_words = re.findall(r'\b\w+\b', message.lower())
        encrypted_words = re.findall(r'\b\w+\b', encrypted_message.lower())

        # Nothing to verify if there are 0 or 1 original words
        if len(original_words) <= 1:
            return True
        
        for i in range(len(original_words) - 1):
            if not original_words[i] == encrypted_words[i*(k+1)]: 
                return False
        
        return True
    
    # *** Implement some kind of semantic check with nlp or something to give user a better idea about output *** #
    def _semantic_check() :
        pass

    def encrypt(self, message, key, compress) :
        """ Encrypts text by adding words based on key value between each original word.. """

        try : 
            reference_text = self._generate_reference_text(message)

            # reference_words = re.findall(r'\b\w+\b', reference_text.lower()) # makes a list of words for reference para
            words = re.findall(r'\b\w+\b', message.lower()) # makes a list of words of input message

            k = int(key)

            # Return if length of message is 1
            if len(words) <= 1 :
                return " ".join(words)
            
            encrypted_words = [words[0]] # Keeping the first word same as input message. 

            for i in range(len(words) - 1) :
                # *** try using more words in promt to give a bit of context *** #
                # *** Stops repeating owrds in the encrypted message *** #
                prompt = "Generate {0} natural sounding words that fit grammatically and semantically between the words '{1}' and '{2}', based on the context: '{3}' so that the overall sentence makes sense,.".format(k, words[i], words[i+1], reference_text)
                generated_words = generate_text(prompt)
                generated_words_list = re.findall(r'\b\w+\b', generated_words)
                encrypted_words.extend(generated_words_list[:k])
                encrypted_words.append(words[i+1]) # Add the original word.

            encrypted_message = " ".join(encrypted_words) # Join the words.

            # --- Strict Insertion Rule Verification --- #
            try:
               self._verify_insertion_count(message, encrypted_message, k)

            except ValueError as e:
               logger.error("Strict insertion violation detected: {}".format(e))

               # *** Need to fix this - make this a better fallback like regenerating only the problematic section ***
               # *** Create a loop to keep updating the prompt
               return self.encrypt(message, key) # Simplistic regeneration
            
            return encrypted_message
        
        except Exception as e:
            logger.error("Encryption failed: {}".format(e))
            return "Encryption failed: {}".format(e)
    
    def decrypt(self, encrypted_message, key, compress) :
        """Decrypts the skipcode-encrypted text by removing words"""

        try :
            encrypted_words = re.findall(r'\b\w+\b', encrypted_message.lower())
            k = int(key)

            decrypted_words = [encrypted_words[0]]

            for i in range(len(encrypted_words)-1):
                 if len(encrypted_words) > (i * (k+1) +1):
                   decrypted_words.append(encrypted_words[(i * (k+1) +1)]) # Add the words based on the skip key
            
            return " ".join(decrypted_words)
        
        except Exception as e :
            logger.error("Decryption failed: {}".format(e))
            return "Decryption failed: {}".format(e)
    