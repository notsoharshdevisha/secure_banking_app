from flask import request, redirect
from services.user_service import logged_in


def check_auth(app):
    @app.before_request
    def use_check_auth():
        if request.path != "/login" and not logged_in():
            return redirect("/login")
