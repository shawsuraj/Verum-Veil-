import pytest

from modules.skipcode_crypt import SkipCodeCrypt

class TestSkipCodeCrypt:
    @pytest.fixture
    def skipcode_crypt(self):
       return SkipCodeCrypt()
    
    @pytest.fixture
    def valid_encrypted_message(self) :
        message = "Black coffee hot"
        key = 2
        encrypted_message = "Black kind of coffee is very hot"

        return message, encrypted_message, key

    @pytest.fixture
    def invalid_encrypted_messages(self):
        return [
            ("Black coffee hot", "black coffee is hot", 2),   # less than k
            ("Black coffee hot", "black a b c coffee is very hot", 2), # more than k
            # ("Black coffee hot", "black coffee hot", 2),# no words - have to handle this error seperately for IndexError: list index out of range
            ("Black coffee hot", "banana is a coffee is very hot", 2) # changed words.
        ]   


    def test_verify_insertion_count_valid(self, valid_encrypted_message):
        """Test verify insertion count."""
        message, encrypted_message, key = valid_encrypted_message
        result = SkipCodeCrypt.verify_insertion_count(message, encrypted_message, key)
        assert result == True, "Expected True but got {}".format(result)

    def test_verify_insertion_count_invalid(self, invalid_encrypted_messages):
        """Test verify insertion count."""

        for message, encrypted_message, key in invalid_encrypted_messages :
            result = SkipCodeCrypt.verify_insertion_count(message, encrypted_message, key)
            assert result == False, "Expected False but got {}".format(result)

        
