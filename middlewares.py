from flask import request, redirect
from services.user_service import logged_in


def check_auth(app):
    @app.before_request
    def use_check_auth():
        # check if user is authenticated before visiting authenticated routes
        if request.path != "/login" and not logged_in():
            return redirect("/login")
