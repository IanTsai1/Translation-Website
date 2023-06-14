from flask import*
from before_file import app_before_file
from after_file import app_after_file


app_front_page = Blueprint('front_page',__name__)
app_front_page.register_blueprint(app_before_file)
app_front_page.register_blueprint(app_after_file)

data = {}

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
    language = str(request.json.get('lang'))
    if("from" in language):
        data["original_Lang"] = language[5:]
    else:
        data["translatedTo_Lang"] = language[3:]
    return render_template('site.html')


@app_front_page.route("/before_translatate", methods=['GET','POST'])
def getBeforeTranslate():
    text = str(request.json.get("beforeTranslateText"))
    data["beforeTranslateText"] = text
    return redirect(request.url)



