from app_factory import create_app
from flask import redirect, request
from services.user_service import logged_in

app = create_app()


@app.before_request
def check_auth():
    if request.path != "/login" and not logged_in():
        return redirect("/login")


if __name__ == "__main__":
    app.run()
