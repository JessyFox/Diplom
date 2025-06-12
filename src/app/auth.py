from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required
from models import db, Order

bp = Blueprint('auth', __name__, url_prefix='/auth')

def init_login_manager(app):
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Для доступа к данной странице необходимо пройти процедуру аутентификации.'
    login_manager.login_message_category = 'warning'
    login_manager.user_loader(load_order)
    login_manager.init_app(app)

def load_order(order_id):
    order = db.session.execute(db.select(Order).filter_by(id=order_id)).scalar()
    return order

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        order_id = request.form.get('order_id')
        password = request.form.get('password')
        if login and password:
            order = db.session.execute(db.select(Order).filter_by(id=order_id)).scalar()
            if order and order.check_password(password):
                login_user(order)
                flash('Вы успешно аутентифицированы.', 'success')
                next = request.args.get('next')
                return redirect(next or url_for('index'))
        flash('Введены неверные логин и/или пароль.', 'danger')
    return render_template('auth/login.html')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
