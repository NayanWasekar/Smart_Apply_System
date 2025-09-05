from app import create_app
from models import db
from models.company_employee import CompanyEmployee

# Create app and push context
app = create_app()
with app.app_context():
    # Find the Admin you want to delete
    admin = CompanyEmployee.query.filter_by(email="admin1@gmail.com").first()

    # Delete if it exists
    if admin:
        db.session.delete(admin)
        db.session.commit()
        print("Admin deleted")
    else:
        print("Admin not found")
