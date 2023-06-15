from flask import*

app_after_file = Blueprint('after_file',__name__)

@app_after_file.route("/upload-success")
def index():
    return render_template("after_file.html")
