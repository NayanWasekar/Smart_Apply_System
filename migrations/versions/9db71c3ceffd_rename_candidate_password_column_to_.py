"""Rename candidate password column to password_hash safely

Revision ID: 9db71c3ceffd
Revises: 
Create Date: 2025-09-08 17:29:34.861690
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy import text

# revision identifiers, used by Alembic.
revision = '9db71c3ceffd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('candidate', schema=None) as batch_op:
        # Step 1: Add the column as nullable
        batch_op.add_column(sa.Column('password_hash', sa.String(length=255), nullable=True))

    # Step 2: Fill existing passwords if old column exists
    try:
        op.execute(text("UPDATE candidate SET password_hash = password"))
    except Exception:
        # If no old 'password' column exists, just skip
        pass

    # Step 3: Alter column to NOT NULL
    with op.batch_alter_table('candidate', schema=None) as batch_op:
        batch_op.alter_column('password_hash', nullable=False)

    # Step 4: Drop old column if exists
    try:
        with op.batch_alter_table('candidate', schema=None) as batch_op:
            batch_op.drop_column('password')
    except Exception:
        pass


def downgrade():
    # Reverse upgrade
    with op.batch_alter_table('candidate', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=255), nullable=True))

    try:
        op.execute(text("UPDATE candidate SET password = password_hash"))
    except Exception:
        pass

    with op.batch_alter_table('candidate', schema=None) as batch_op:
        batch_op.alter_column('password', nullable=False)

    with op.batch_alter_table('candidate', schema=None) as batch_op:
        batch_op.drop_column('password_hash')
