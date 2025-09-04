from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import models
from .company_employee import CompanyEmployee
from .job import Job
from .candidate import Candidate
from .application import Application
from .application_progress import ApplicationProgress
from .email_log import EmailLog
