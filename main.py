from flask import*
from front_page import app_front_page
from before_file import app_before_file
from after_file import app_after_file


main_app = Flask(__name__)
main_app.register_blueprint(app_front_page)
main_app.register_blueprint(app_before_file)
main_app.register_blueprint(app_after_file)


if __name__ == '__main__':
    main_app.secret_key = "Your Key"
    main_app.run(debug=True)