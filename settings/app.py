from flask import Flask
from settings.config import TEMPLATE_DIR, STATIC_DIR
from flask_cors import CORS


app = Flask(
    __name__, 
    template_folder=TEMPLATE_DIR,
    static_folder=STATIC_DIR
)
CORS(app)

app.secret_key = 'super secret key'

