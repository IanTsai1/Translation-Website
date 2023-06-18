import openai
import os
#from translating_file import get_percent
import tiktoken
from textwrap import wrap


openai.api_key = os.getenv("OPENAI_API_KEY")

def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = len(encoding.encode(string))
    return num_tokens

#this split won't cut any words in half, so it we can still translate
def split_string(str,num):
    return wrap(str, len(str)//num)

#concatenates all string in an arr into one string
def concatenate_arrstr(arr):
     return ' '.join(arr)

def percent(count,length):
    per = (int)((count/length)*100)
    return per

#["hello im ian im having a bad day"]
def token_valid(arr):
     count = 3
     texts = arr
     if num_tokens_from_string(arr[0]) >= 500: #change 500 to 1780
        texts = split_string(arr[0],count)
        while(num_tokens_from_string(str(max(texts,key=len)))>500):
            count+=2
            texts = split_string(concatenate_arrstr(texts),count-1)
     return texts


def translate(from_lang, to_lang, filename):
    from translating_file import get_percent
    translates = []
    count = 1
    file_path = os.path.join("downloaded_files", filename)
    with open(file_path) as new_file: #need import os to change path to get file
        str = new_file.read()
    texts = token_valid([str])
    length = len(texts)

    history = [
        {"role": "system", "content": "You are a translator. The text might not make sense because it's cut from a larger text"},
        ]

    if from_lang == "detected_language":
        for i in texts:
            prompt = f"Translate: [{i}] to {to_lang}. Only include the translated text. Don't include brackets"
            history.append({"role": "user", "content": prompt})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=history,
                temperature=0.5,
            )
            text = response['choices'][0]['message']['content']
            get_percent(percent(count,length))
            count+=1
            translates.append(text)
        return concatenate_arrstr(translates)
    else:
        for i in texts:
            prompt = f"Translate: [{i}] to {to_lang}. Only include the translated text. Don't include brackets"
            history.append({"role": "user", "content": prompt})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=history,
                temperature=0.5,
            )
            text = response['choices'][0]['message']['content']
            get_percent(percent(count,length))
            count+=1
            translates.append(text)
        return concatenate_arrstr(translates) #need to chagne dictionary value in translating_file not return sth


