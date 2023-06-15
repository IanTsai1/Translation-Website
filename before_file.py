from flask import*
from after_file import app_after_file

app_before_file = Blueprint('before_file',__name__)
#app_before_file.register_blueprint(app_front_page)
app_before_file.register_blueprint(app_after_file)

@app_before_file.route("/files")
def index():
    return render_template("before_file.html")

@app_before_file.route("/files",methods=['GET','POST'])
def next_path():
    print("HELLO")
    if "text" in request.form:
        return redirect(url_for("front_page.index"))
    elif "file" in request.form:
        return render_template("before_file.html")
    else:
        return redirect(url_for("after_file.index"))


