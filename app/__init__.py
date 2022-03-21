from flask import Flask

admin_ui_service = Flask(__name__)

import app.views
