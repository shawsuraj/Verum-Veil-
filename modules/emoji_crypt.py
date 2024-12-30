import logging
import emoji
import hashlib

logger = logging.getLogger(__name__)

# A very inefficient, simple and unsecure encryption algorithm using emojis
# This is just to create a base for the project and will be replaced by a more secure algorithm in the future

class EmojiCrypt() :
    def __init__(self) :
        self.emoji_map = self._emoji_map()
        self.reverse_emoji_map = self._reverse_emoji_mapping()


    def _emoji_map(self) :
        emoji_map = {}
        
        for i, emoji_char in enumerate(list(emoji.EMOJI_DATA.keys())[:100000]):
            emoji_map[i] = emoji_char
            # print(emoji_map)
        
        return emoji_map

    def _reverse_emoji_mapping(self):
        reverse_emoji_map = {}

        for k, v in self.emoji_map.items():
            reverse_emoji_map[v] = k

        self.reverse_emoji_map = reverse_emoji_map
    
    def _get_key(self, password) :
        password_bytes = password.encode()
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password_bytes,
            b'salt', # salt
            100000,  # ierations
            32  # key length
        )
        return key
        

    def encrypt(self, message, password, compress) :
        key = self._get_key(password)
        encypted_message = ""

        for char in message:
            char_code = ord(char)
            key_index = char_code % len(key)
            key_value = key[key_index]

            emoji_index = (char_code + key_value) % len(self.emoji_map)
            encypted_message += self.emoji_map[emoji_index]

        with open("output.txt", "a") as f:
            f.write(encypted_message)

        return encypted_message
        # return ("encrypted message")
    
    def decrypt(self, message, password, compress) :
        key = self._get_key(password)
        decrypted_message = ""

        for i, emoji_char in enumerate(message):
            emoji_index = self.reverse_emoji_map[emoji_char]

            key_index = i % len(key)  
            key_value = key[key_index]

            char_code = (emoji_index - key_value) % len(self.emoji_map)
            decrypted_char = chr(char_code)
            decrypted_message += decrypted_char
        
        return decrypted_message
