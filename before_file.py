from flask import*
from after_file import app_after_file
from translating_file import app_translating_file
from werkzeug.utils import secure_filename
import os

app_before_file = Blueprint('before_file',__name__)
app_before_file.register_blueprint(app_after_file)
app_before_file.register_blueprint(app_translating_file)

@app_before_file.route("/files")
def index():
    return render_template("before_file.html")

@app_before_file.route("/files",methods=['GET','POST'])
def next_path():
    if "text" in request.form:
        return redirect(url_for("front_page.index"))
    elif "file" in request.form:
        return render_template("before_file.html")
    else:
        f = request.files['upload_complete'] #"upload_complete" is the name of the input button
        filename = secure_filename(f.filename)
        file_path = os.path.join('downloaded_files', filename)
        f.save(file_path)
        return redirect(url_for("after_file.index"))


