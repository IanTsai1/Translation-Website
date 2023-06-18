from flask import*
#from backend import translate_pdf, translate_txtfile(in translate())
import threading


app_translating_file = Blueprint('translating_file',__name__)
data = {"percent":0, "translated_text": ""}

data = {}

#default language
data["fromLang"] = "detected_language"
data["toLang"] = "spanish"
data["translated_file"] = "Translation" #updated after translation ends
data["percent"] = 0


@app_translating_file.route("/translating-file", methods=['GET','POST'])
def updating_essential():
    print("start of updating filename")
    data["filename"] = str(request.json.get('filename'))
    print("end of updating filename")
    return render_template("file_translated.html")


#need a fetch to post data from server to user
def translate(from_lang, to_lang, filename):
    print("start of translate")
    from backend import translate_pdf, translate_txtfile
    filetype = data.get("filename")[len(data.get("filename"))-3:]
    if filetype == "pdf":
        translated = translate_pdf.translate(from_lang, to_lang, filename) #calling translate_pdf method
        data["translated_file"] = translated
        return translated
    elif filetype == "txt":
        translated = translate_txtfile.translate(from_lang, to_lang, filename) #calling translate_txt method
        data["translated_file"] = translated
        return translated



def get_percent(value):
    data["percent"] = value

@app_translating_file.route("/translating/file")
def index():
    print("Filename:", data.get("filename"))
    thread = threading.Thread(target=translate, args=(data.get("fromLang"),data.get("toLang"),data.get("filename")))
    thread.start()
    print("start of threading")
    return render_template("file_translated.html") #when it goes to new page, translate() will still be running


#These two are for js to fetch updated % and translated value
@app_translating_file.route('/percent')
def percent():
    return str(data.get("percent"))

@app_translating_file.route('/translated/file')
def translated_file():
    return str(data.get("translated_file"))


'''
Translating_file
    External calls:
        pdf.translate()
        txt.translate()

    Internal methods:
        get_percent()

translate pdf
    External calls:
        get_percent()

    Internal methods:
        translate()

translate txt
    External calls:
        get_percent()

    Internal methods:
        translate()






'''