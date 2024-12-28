import pytest
from unittest.mock import patch

from modules.skipcode_crypt import SkipCodeCrypt

class TestSkipCodeCrypt:
    @pytest.fixture
    def skipcode_crypt(self):
       return SkipCodeCrypt()
    
    @patch('modules.skipcode_crypt.generate_text')
    def test_generate_reference_text(self, mock_generate_text, skipcode_crypt) :
        """Test if it genrates reference text with the message."""
        test_message = "this is a message"
        mock_generate_text.return_value = "This is the generated mock reference" # mock the generate_text function

        reference = skipcode_crypt._generate_reference_text(test_message)

        assert len(reference) > 0, "Output string is empty" # Check for non empty output
        assert isinstance(reference, str), "Output's a string" # Check if the output is a string
        assert reference == "This is the generated mock reference", "Outputs the correct generated reference." #Check if output is correct

        mock_generate_text.assert_called_once() # Mock is used only once
    
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
    
    def test_verify_insertion_count_valid(self, skipcode_crypt, valid_encrypted_message):
        """Test verify insertion count."""
        message, encrypted_message, key = valid_encrypted_message
        result = skipcode_crypt._verify_insertion_count(message, encrypted_message, key)
        assert result == True, "Expected True but got {}".format(result)

    def test_verify_insertion_count_invalid(self, skipcode_crypt, invalid_encrypted_messages):
        """Test verify insertion count."""

        for message, encrypted_message, key in invalid_encrypted_messages :
            result = skipcode_crypt._verify_insertion_count(message, encrypted_message, key)
            assert result == False, "Expected False but got {}".format(result)
        
