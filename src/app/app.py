from flask import Flask, render_template
from flask_migrate import Migrate
from sqlalchemy.exc import SQLAlchemyError
from models import db, Product
from auth import bp as auth_bp, init_login_manager
from flask_login import login_required, current_user

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')

db.init_app(app)
migrate = Migrate(app, db)

init_login_manager(app)


@app.errorhandler(SQLAlchemyError)
def handle_sqlalchemy_error(err):
    error_msg = ('Возникла ошибка при подключении к базе данных. '
                 'Повторите попытку позже.')
    return f'{error_msg} (Подробнее: {err})', 500


app.register_blueprint(auth_bp)


@app.route('/')
def index():
    products = db.session.execute(db.select(Product)).scalars()
    return render_template('index.html',products=products)

@app.route('/order')
@login_required
def order():
    return render_template('show.html', order=current_user)
