import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def translate(from_lang, to_lang, filename):
    return True