import openai
import os
from PyPDF3 import PdfFileReader
import tiktoken
from textwrap import wrap
import time
#from translating_file import get_percent


openai.api_key = os.getenv("OPENAI_API_KEY")

#Returns the number of tokens in a text string.
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

#concatenate all string for 2d array
def concatenate_arr(arr):
    str = ""
    for i in arr:
        str = str + ''.join(i[1]) + ' '
    return str

#["hello im ian im having a bad day"]
def token_valid(arr):
    count = 3
    texts = arr
    #changed token to test if % works
    if num_tokens_from_string(arr[0]) >= 500:
        texts = split_string(arr[0],count) #["hello im ian", "im having a bad day"]
        while(num_tokens_from_string(str(max(texts,key=len)))>500):
            count+=2
            texts = split_string(concatenate_arrstr(texts),count-1)
    return texts

def percent(count,length):
    per = (int)((count/length)*100)
    return per


def pdf_reader(filename):
    pdf_obj = PdfFileReader(open(filename, "rb"))
    pages = []
    length = pdf_obj.numPages

    for i in range(0,length):
        pdf_pg = pdf_obj.getPage(i)
        text = pdf_pg.extractText().replace("\n","")
        pages.append([i,[text]])
    return [pages,length]

def translating(page,fromLang,toLang,count):
    if count%2==0:
        time.sleep(20) #may need to change to 3 minutes
    translated = [f"\n<------------------Page {count}------------------------------>\n"]

    history = [
        {"role": "system", "content": "You are a translator. The text might not make sense because it's cut from a larger text"},
        ]
    if fromLang == "detected_language":
        for j in page[1]:
            prompt = f"Translate: [{j}] to {toLang}. Only include the translated text."
            history.append({"role": "user", "content": prompt})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=history,
                temperature=0.5,
            )
            translated.append(response['choices'][0]['message']['content'])
        return concatenate_arrstr(translated)
    else:
        for j in page[1]:
            prompt = f"Translate: [{j}] from {fromLang} to {toLang}. Only include the translated text."
            history.append({"role": "user", "content": prompt})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=history,
                temperature=0.5,
            )
            translated.append(response['choices'][0]['message']['content'])
        return concatenate_arrstr(translated)


def translate(from_lang, to_lang, filename):
    from app.translating_file import get_percent
    count = 1
    file_path = os.path.join("downloaded_files", filename)
    page_length = pdf_reader(file_path)
    pages = page_length[0]
    length = page_length[1]
    pages = token_valid(pages)

    for i in pages:
        i[1] = translating(i,from_lang,to_lang,count) #internal
        get_percent(percent(count,length)) #calling get_percent from translating_file
        count += 1

    return concatenate_arr(pages)