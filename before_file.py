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
    if "text" in request.form:
        return redirect(url_for("front_page.index"))
    else:
        return render_template("before_file.html")


