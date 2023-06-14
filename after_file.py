from flask import*
app_after_file = Blueprint('after_file',__name__)

@app_after_file.route("/hello")
def hello():
    return "Hello World from app 1!"