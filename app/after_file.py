from flask import*
from app.translating_file import app_translating_file

app_after_file = Blueprint('after_file',__name__)
app_after_file.register_blueprint(app_translating_file)

data = {"percent":0, "translated_text": ""}

@app_after_file.route("/upload-success")
def index():
    return render_template("after_file.html")

@app_after_file.route("/next",methods=['GET','POST'])
def next_path():
     if "text" in request.form:
        return redirect(url_for("front_page.index"))
     elif "file" in request.form:
           return redirect(url_for("before_file.index"))
     elif "cancel" in request.form:
          return redirect(url_for("before_file.index"))
     return render_template("after_file.html")

@app_after_file.route("/translate",methods=['GET','POST'])
def translate():
     return redirect(url_for("translating_file.index"))



