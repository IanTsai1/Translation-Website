from flask import*
from before_file import app_before_file
from after_file import app_after_file
from translating_file import app_translating_file
from backend import translate_texts
#from langdetect import detect

app_front_page = Blueprint('front_page',__name__)
app_front_page.register_blueprint(app_before_file)
app_front_page.register_blueprint(app_after_file)
app_front_page.register_blueprint(app_translating_file)

data = {}

#default language
data["original_Lang"] = "detected_language"
data["translatedTo_Lang"] = "spanish"
data["translated_text"] = "Translation"

code_to_language = {
    "aa": "Afar",
    "ab": "Abkhazian",
    "af": "Afrikaans",
    "ak": "Akan",
    "am": "Amharic",
    "ar": "Arabic",
    "as": "Assamese",
    "ay": "Aymara",
    "az": "Azerbaijani",
    "ba": "Bashkir",
    "be": "Belarusian",
    "bg": "Bulgarian",
    "bh": "Bihari",
    "bi": "Bislama",
    "bn": "Bengali",
    "bo": "Tibetan",
    "br": "Breton",
    "ca": "Catalan",
    "co": "Corsican",
    "cs": "Czech",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "dz": "Dzongkha",
    "el": "Greek",
    "en": "English",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "eu": "Basque",
    "fa": "Persian",
    "fi": "Finnish",
    "fj": "Fijian",
    "fo": "Faroese",
    "fr": "French",
    "fy": "Western Frisian",
    "ga": "Irish",
    "gd": "Scottish Gaelic",
    "gl": "Galician",
    "gn": "Guaraní",
    "gu": "Gujarati",
    "gv": "Manx",
    "ha": "Hausa",
    "he": "Hebrew",
    "hi": "Hindi",
    "ho": "Hiri Motu",
    "hr": "Croatian",
    "ht": "Haitian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "hz": "Herero",
    "ia": "Interlingua",
    "id": "Indonesian",
    "ie": "Interlingue",
    "ig": "Igbo",
    "ii": "Sichuan Yi",
    "ik": "Inupiaq",
    "io": "Ido",
    "is": "Icelandic",
    "it": "Italian",
    "iu": "Inuktitut",
    "ja": "Japanese",
    "jv": "Javanese",
    "ka": "Georgian",
    "kg": "Kongo",
    "ki": "Kikuyu",
    "kj": "Kwanyama",
    "kk": "Kazakh",
    "kl": "Kalaallisut",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "kr": "Kanuri",
    "ks": "Kashmiri",
    "ku": "Kurdish",
    "kv": "Komi",
    "kw": "Cornish",
    "ky": "Kyrgyz",
    "la": "Latin",
    "lb": "Luxembourgish",
    "lg": "Ganda",
    "li": "Limburgish",
    "ln": "Lingala",
    "lo": "Lao",
    "lt": "Lithuanian",
    "lu": "Luba-Katanga",
    "lv": "Latvian",
    "mg": "Malagasy",
    "mh": "Marshallese",
    "mi": "Māori",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mn": "Mongolian",
    "mo": "Moldavian",
    "mr": "Marathi",
    "ms": "Malay",
    "mt": "Maltese",
    "my": "Burmese",
    "na": "Nauru",
    "nb": "Norwegian Bokmål",
    "nd": "North Ndebele",
    "ne": "Nepali",
    "ng": "Ndonga",
    "nl": "Dutch",
    "nn": "Norwegian Nynorsk",
    "no": "Norwegian",
    "nr": "South Ndebele",
    "nv": "Navajo",
    "ny": "Chichewa",
    "oc": "Occitan",
    "oj": "Ojibwa",
    "om": "Oromo",
    "or": "Oriya",
    "os": "Ossetian",
    "pa": "Panjabi",
    "pi": "Pāli",
    "pl": "Polish",
    "ps": "Pashto",
    "pt": "Portuguese",
    "qu": "Quechua",
    "rm": "Romansh",
    "rn": "Kirundi",
    "ro": "Romanian",
    "ru": "Russian",
    "rw": "Kinyarwanda",
    "sa": "Sanskrit",
    "sc": "Sardinian",
    "sd": "Sindhi",
    "se": "Northern Sami",
    "sg": "Sango",
    "si": "Sinhala",
    "sk": "Slovak",
    "sl": "Slovene",
    "sm": "Samoan",
    "sn": "Shona",
    "so": "Somali",
    "sq": "Albanian",
    "sr": "Serbian",
    "ss": "Swati",
    "st": "Southern Sotho",
    "su": "Sundanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "tg": "Tajik",
    "th": "Thai",
    "ti": "Tigrinya",
    "tk": "Turkmen",
    "tl": "Tagalog",
    "tn": "Tswana",
    "to": "Tonga",
    "tr": "Turkish",
    "ts": "Tsonga",
    "tt": "Tatar",
    "tw": "Twi",
    "ty": "Tahitian",
    "ug": "Uighur",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "ve": "Venda",
    "vi": "Vietnamese",
    "vo": "Volapük",
    "wa": "Walloon",
    "wo": "Wolof",
    "xh": "Xhosa",
    "yi": "Yiddish",
    "yo": "Yoruba",
    "za": "Zhuang",
    "zh": "Chinese",
    "zu": "Zulu"
}


@app_front_page.route("/")
def index():
    return render_template('site.html')

@app_front_page.route("/",methods=['GET','POST'])
def next_path():
    if "text" in request.form:
        return render_template('site.html') #change to redirect?
    elif "file" in request.form:
        return redirect(url_for("before_file.index"))
    return render_template('site.html')


@app_front_page.route("/language", methods=['GET','POST'])
def language():
    from_language = str(request.json.get('fromLang'))
    to_language = str(request.json.get('toLang'))
    data["original_Lang"] = from_language[5:]
    data["translatedTo_Lang"] = to_language[3:]
    return render_template('site.html')

@app_front_page.route("/translated/text", methods=['GET','POST'])
def getBeforeTranslate():
     if request.method == 'POST':
        text = str(request.get_json().get("beforeTranslateText"))
        translated_text = translate_texts.translate_text(text, data.get("original_Lang"), data.get("translatedTo_Lang"))
        data["translated_text"] = translated_text
        return render_template("site.html")
     return render_template("site.html")

@app_front_page.route("/get/translated/text")
def datum():
    return data.get("translated_text")


'''
@app_front_page.route("/detected-language")
def update_language():
    if(len(data.get("beforeTranslateText")) > 0):
        lang_code = detect(data["beforeTranslateText"])
        lang = code_to_language[lang_code]
        return lang + " - Detected"
'''






