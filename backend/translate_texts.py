import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_text(text, language_from, language_to):
    history = [
        {"role": "system", "content": "You are a translator."},
        ]

    if(language_from=="detected_language"):
        prompt = f"Translate: [{text}] to {language_to}. Only include the translated text. Don't include brackets"

        history.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history,
            temperature=0.5,
        )
        return response['choices'][0]['message']['content']
    else:
        prompt = f"Translate: [{text}] from {language_from} to {language_to}. Only include the translated text."

        history.append({"role": "user", "content": prompt})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=history,
            temperature=0.5,
        )
        return response['choices'][0]['message']['content']

