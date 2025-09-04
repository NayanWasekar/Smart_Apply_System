from . import db
from datetime import datetime

class Job(db.Model):
    __tablename__ = "job"

    job_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text)
    location = db.Column(db.String(255))
    posted_by = db.Column(db.Integer, db.ForeignKey("company_employee.employee_id", ondelete="SET NULL"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    # Relationships
    applications = db.relationship("Application", backref="job", lazy=True)

    def __repr__(self):
        return f"<Job {self.title}>"
