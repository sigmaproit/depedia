import os

from flask import Flask
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from celery_worker import make_celery

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(os.environ['APP_SETTINGS'])
app.app_context()
db = SQLAlchemy(app)
ma = Marshmallow(app)
celery = make_celery(app)

cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

if __name__ == '__main__':
    from views.auth import *
    from views.views import *

    app.run(debug=os.getenv('DEBUG', False), host='0.0.0.0', port=os.getenv('PORT', 5000))
