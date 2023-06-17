from flask import*
from backend import translate_pdf, translate_txtfile
import threading


app_translating_file = Blueprint('translating_file',__name__)
data = {"percent":0, "translated_text": ""}

data = {}

#default language
data["fromLang"] = "detected_language"
data["toLang"] = "spanish"
data["translated_file"] = "Translation" #updated after translation ends
data["percent"] = 0


@app_translating_file.route("/translating-file")
def updating_essential():
    from_language = str(request.json.get('fromLang'))
    to_language = str(request.json.get('toLang'))

    data["fromLang"] = from_language[5:]
    data["toLang"] = to_language[3:]
    data["filename"] = str(request.json.get('filename'))


#need a fetch to post data from server to user
def translate(from_lang, to_lang, filename):
    filetype = data.get("filename")[len(data.get("filename"))-3:]
    if filetype == "pdf":
        translated = translate_pdf.translate(from_lang, to_lang, filename)
    elif filetype == "txt":
        translated = translate_txtfile.translate(from_lang, to_lang, filename)
    data["translated_text"] = translated
    return translated

def get_percent(value):
    data["percent"] = value

@app_translating_file.route("/translating/file")
def index():
    updating_essential()
    thread = threading.Thread(target=translate, args=(data.get("fromLang"),data.get("toLang"),data.get("filename")))
    thread.start()
    return render_template("file_translated.html") #when it goes to new page, translate() will still be running

@app_translating_file.route('/percent')
def percent():
    return str(data.get("percent"))

@app_translating_file.route('/translated/file')
def translated_file():
    return str(data.get("translated_file"))


