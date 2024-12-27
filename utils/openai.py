from openai import OpenAI

client = OpenAI(api_key="key")


def get_ai_response(crypt_prompt) :

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[
        {"role": "system", "content": "You are a helpful assistant that assists with sentence manipulation tasks."},
        {"role": "user", "content": crypt_prompt}
            ]   ,
        max_tokens=50,  # Output limit
        temperature=0.7,  # Controlled randomness for more coherent outputs
        n=1  # Only one result needed
    )

    return response