from flask import*

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('site.html')

if __name__ == '__main__':
    app.secret_key = "Your Key"
    app.run(debug=True)