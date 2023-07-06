from flask import Flask
import schemas
from database import db
from strawberry.flask.views import GraphQLView
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Password0#@localhost/E-com?port=5432'

# Initialize the database
db.init_app(app)

@app.route('/')
def index():
    return 'Stocks Management System'

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

app.add_url_rule('/SMS', view_func=GraphQLView.as_view('graphql', schema=schemas))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)