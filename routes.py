from flask import Blueprint, render_template, redirect, request, g, abort, make_response
from services.user_service import get_user_with_credentials, logged_in
from services.account_service import get_balance, do_transfer
from forms import LoginForm, TransferForm
from utils import Transaction

# Create a blueprint
main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET'])
def home():
    return redirect('/login')


@main_bp.route('/login', methods=['GET'])
def login_view():
    if not logged_in():
        form = LoginForm()
        return render_template('login.html', form=form), 200
    return redirect('/dashboard')


@main_bp.route('/login', methods=['POST'])
def login_api():
    email = request.form.get('email')
    password = request.form.get('password')
    user = get_user_with_credentials(email, password)
    if not user:
        form = LoginForm()
        return render_template('login.html', form=form, invalid_cred_message='Invalid Credentials')
    response = make_response(redirect('/dashboard'))
    response.set_cookie('auth_token', user['token'])
    return response, 302


@main_bp.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html', email=g.user)


@main_bp.route('/details', methods=['GET'])
def details():
    account_number = request.args['account']
    return render_template(
        'details.html',
        user=g.user,
        account_number=account_number,
        balance=get_balance(account_number, g.user))


@main_bp.route('/logout', methods=['GET'])
def logout():
    response = make_response(redirect('/login'))
    response.delete_cookie('auth_token')
    return response, 303


@main_bp.route('/transfer', methods=['POST'])
def transfer():
    form = request.form
    if not form:
        return abort(400, "bad request")

    source = form.get('from')
    target = form.get('to')
    amount = form.get('amount')

    transaction = None
    try:
        transaction = Transaction(source, target, amount)
    except Exception:
        return abort(400, "bad request")

    available_balance = get_balance(transaction.get_source(), g.user)
    if available_balance is None:
        abort(400, 'Account not found')

    if transaction.get_amount() > int(available_balance):
        abort(400, 'You don\'t have that much')

    if do_transfer(transaction):
        return redirect('/dashboard')
    else:
        abort(400, 'Something bad happened')


@main_bp.route('/transfer', methods=['GET'])
def transfer_view():
    form = TransferForm()
    return render_template('transfer.html', form=form)
