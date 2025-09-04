from . import db
from datetime import datetime

class EmailLog(db.Model):
    __tablename__ = "email_log"

    email_id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey("application.application_id", ondelete="CASCADE"), nullable=False)
    recipient = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)
    type = db.Column(db.String(50))  
    # rejection / interview / offer / custom

    def __repr__(self):
        return f"<EmailLog {self.type} to {self.recipient}>"
