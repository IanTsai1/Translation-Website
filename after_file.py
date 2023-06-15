from flask import*

app_after_file = Blueprint('after_file',__name__)

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
     return redirect(request.url)
@app_after_file.route("/translate",methods=['GET','POST'])
def translate():
     print("NEW NEW TEST!")
     return render_template("after_file.html")
