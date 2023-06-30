from flask import*
#from backend import translate_pdf, translate_txtfile(in translate())
import threading
import app.database


app_translating_file = Blueprint('translating_file',__name__)

#default
data = {}
data["translated_file"] = "Translation" #updated after translation ends
data["percent"] = 0


@app_translating_file.route("/translating-file", methods=['GET','POST'])
def updating_essential():
    data["filename"] = str(request.json.get('filename'))
    return render_template("file_translated.html")


#need a fetch to post data from server to user
def translate(from_lang, to_lang, filename):
    from backend import translate_pdf, translate_txtfile, translate_audio
    filetype = data.get("filename")[len(data.get("filename"))-3:]
    if filetype == "pdf":
        translated = translate_pdf.translate(from_lang, to_lang, filename) #calling translate_pdf method
        data["translated_file"] = translated
        return translated
    elif filetype == "txt":
        translated = translate_txtfile.translate(from_lang, to_lang, filename) #calling translate_txt method
        data["translated_file"] = translated
        return translated
    elif filetype == "mp4" or filetype=="mp3":
        translated = translate_audio.translate(from_lang, to_lang, filename) #calling translate_txt method
        data["translated_file"] = translated
        return translated


def get_percent(value):
    data["percent"] = value

@app_translating_file.route("/translating/file")
def index():
    fromLang, toLang = app.database.getLang()
    thread = threading.Thread(target=translate, args=(fromLang, toLang, data.get("filename")))
    thread.start()
    return render_template("file_translated.html") #when it goes to new page, translate() will still be running


#These two are for js to fetch updated % and translated value
@app_translating_file.route('/percent')
def percent():
    return str(data.get("percent"))

@app_translating_file.route('/translated/file')
def translated_file():
    return str(data.get("translated_file"))
