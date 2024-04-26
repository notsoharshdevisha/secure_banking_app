from app_factory import create_app
from middlewares import check_auth
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = create_app()

Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per hour", "2 per second"],
    storage_uri="memory://",
)

check_auth(app)

if __name__ == "__main__":
    app.run()
