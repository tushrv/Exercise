

import os
from openai import OpenAI
import random

def generate_band_name(city, pet):
    """Generates a band name using OpenAI's ChatCompletion API."""
    
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a creative assistant that generates band names."},
            {"role": "user", "content": f"Suggest a band name based on the city '{city}' and the pet '{pet}'."}
        ],
        max_tokens=50,
        n=5,
        stop=None,
        temperature=0.7
    )

    band_names = [choice.message.content.strip() for choice in completion.choices]
    return random.choice(band_names)

if __name__ == "__main__":
    print("Welcome to the AI-Powered Band Name Generator!")
    street = input("What's the name of the city you grew up in?\n")
    pet = input("What's your pet's name?\n")

    try:
        band_name = generate_band_name(street, pet)
        print(f"\nYour AI-suggested band name is: {band_name}")
    except Exception as e:
        if "OPENAI_API_KEY" in str(e): 
            print("Error: Please make sure the OPENAI_API_KEY environment variable is set correctly.")
        else:
            print(f"An error occurred: {e}")


