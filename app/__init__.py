# sobrepõe a inicialização da pasta app/__init__.py
from flask import Flask
# render_template

class MyApp(Flask):
    def __init__(self):
        self.app = Flask(__name__, template_folder="views/templates")

    # @self.app.route("/")
    # def home ():
    #     return render_template("base.html", title="Página Inicial")

    def run(self):
        self.app.run(debug=True)