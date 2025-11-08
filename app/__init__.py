# sobrepõe a inicialização da pasta app/__init__.py
from flask import Flask
import secrets
# render_template

class MyApp():
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = secrets.token_hex(16)
    
        # from controllers.auth.routes import auth_blueprint
        from app.controllers.main.routes import main_blueprint

        # self.app.register_blueprint (auth_blueprint)
        self.app.register_blueprint (main_blueprint)

    def run(self):
        self.app.run(debug=True)