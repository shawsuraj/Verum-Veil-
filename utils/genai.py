import google.generativeai as genai

# Configure API Key
genai.configure(api_key="AIzaSyBkXkMNqwbs0Fo7veFNCLE9cxpftG2rklU") #dummy_api

# Function to generate text
def generate_text(prompt, key="", max_tokens=3000, temperature=1.0):
    try:
        
        # Generate text using Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                # Only one candidate for now.
                candidate_count=1,
                stop_sequences=["x"],
                max_output_tokens=max_tokens,
                temperature=temperature
            ),
        )
        return response.text
    
    except Exception as e:
        print(f"Error: {e}")
        return None
    
# Backup function that only uses AI to generate for skip code encryption - not very reliable    
def generate_text_back(message, key, max_tokens=3000, temperature=1.0):
    try:
        prompt = """Task: Transform a given sentence by inserting exactly {1} words between each consecutive pair of words. Prioritize strict adherence to the {1} word insertion rule above all other factors, including naturalness or semantic flow.
        
        Input: {0}

        Instructions:
        1. Word Insertion: For every pair of consecutive words in the input sentence, insert exactly {1} additional words between them.
        2. Primary Constraint: The insertion of precisely {1} words between every word pair is a mandatory requirement.
        3. Secondary Goal: Natural Language: While adhering strictly to the {1} word insertion, attempt to select words that create a sentence that sounds as natural, fluent, and grammatically correct as possible.
        4. Grammar: The resulting sentence must be grammatically valid.
        5. No Deletion: Do not delete or remove any original words in the sentence.
        6. Balancing Act: If a conflict arises between the {1} word insertion and natural sounding language, prioritize the {1} word insertion rule, but always strive to use the best words possible to ensure the resulting sentence isn't overly awkward.

        Output: Provide the modified sentence as a single line of text.

        Example:

        Input Sentence: canvas request completion

        Output Sentence: canvas for now request to quickly completion is done

        Note:
        * The core focus is on the exact insertion of two words between each pair of original words.
        * While adhering to this rule, strive to use the most natural-sounding and coherent language possible.
        * If completely natural language is impossible while adhering to the {1} word insertion rule, prioritize the {1} word insertion rule.
        """.format(message, key)
        
        # Generate text using Gemini model
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(
            prompt,
            generation_config=genai.types.GenerationConfig(
                # Only one candidate for now.
                candidate_count=1,
                stop_sequences=["x"],
                max_output_tokens=max_tokens,
                temperature=temperature
            ),
        )
        return response.text
    
    except Exception as e:
        print(f"Error: {e}")
        return None