from flask import Blueprint
hr_bp = Blueprint("hr", __name__, url_prefix="/hr")

# Example route
@hr_bp.route("/dashboard", methods=["GET"])
def dashboard():
    return jsonify({"message": "HR Dashboard is working!"})

# Example route: job create (dummy for now)
@hr_bp.route("/create-job", methods=["POST"])
def create_job():
    data = request.get_json()
    return jsonify({"message": f"Job created with title {data.get('title')}"})


