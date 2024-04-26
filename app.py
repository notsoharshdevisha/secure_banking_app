from app_factory import create_app
from flask import redirect, request
from services.user_service import logged_in
from middlewares import check_auth

app = create_app()

check_auth(app)

if __name__ == "__main__":
    app.run()
