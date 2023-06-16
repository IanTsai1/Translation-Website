from flask import*
from backend import translate_pdf, translate_txtfile
import threading


app_translating_file = Blueprint('translating_file',__name__)
data = {"percent":0, "translated_text": ""}

data = {}

#default language
data["fromLang"] = "detected_language"
data["toLang"] = "spanish"
data["translated_text"] = "Translation" #updated after translation ends
data["percent"] = 0


'''
grab essentials
start thread
call translate text
    while iteraitng call get_percent() from this file after every iteration
update % using previous code
update translate text when everything finishes
'''



@app_translating_file.route("/translating-file")
def grabbing_essential():
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
    return translated

def get_percent(value):
    data["percent"] = value

@app_translating_file.route("/translating/file")
def index():
    grabbing_essential() #updating values
    thread = threading.Thread(target=translate, args=(data.get("fromLang"),data.get("toLang"),data.get("filename")))
    thread.start()
    return render_template("file_translated.html") #when it goes to new page, translate() will still be running

@app.route('/data')
def data():
    return str(data.get("percent"))
