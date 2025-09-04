from flask import Blueprint
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# Example route
@auth_bp.route("/test", methods=["GET"])
def test():
    return "Auth Routes Working!"

