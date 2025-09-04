from . import db
from datetime import datetime

class ApplicationProgress(db.Model):
    __tablename__ = "application_progress"

    progress_id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey("application.application_id", ondelete="CASCADE"), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    updated_by = db.Column(db.Integer, db.ForeignKey("company_employee.employee_id", ondelete="SET NULL"))
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f"<ApplicationProgress {self.status} @ {self.updated_at}>"
