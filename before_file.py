from flask import*

app_before_file = Blueprint('before_file',__name__)

@app_before_file.route("/files")
def hello():
    return render_template("before_file.html")