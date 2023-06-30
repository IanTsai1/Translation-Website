import openai
import os


openai.api_key = os.getenv("OPENAI_API_KEY")


def transcribe(filename):
    file_path = os.path.join("downloaded_files", filename)
    audio_file= open(file_path, "rb")
    transcript = openai.Audio.transcribe(
        model = "whisper-1",
        file = audio_file,
        task= "transcribe"
    )
    return transcript.text


def translate(fromLang, toLang, filename):
    from backend import translate_texts
    from app.translating_file import get_percent
    transcribed = transcribe(filename)
    translated = translate_texts.translate(transcribed, fromLang, toLang)
    get_percent(100)
    return translated




