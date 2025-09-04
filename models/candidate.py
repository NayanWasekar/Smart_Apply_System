from . import db
from datetime import datetime

class Candidate(db.Model):
    __tablename__ = "candidate"

    candidate_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(50))
    resume_path = db.Column(db.String(255))  # file storage path
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    applications = db.relationship("Application", backref="candidate", lazy=True)

    def __repr__(self):
        return f"<Candidate {self.name}>"
