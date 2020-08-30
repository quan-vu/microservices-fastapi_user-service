"""create users table

Revision ID: 826c882edb81
Revises: 
Create Date: 2020-08-30 11:39:47.191510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '826c882edb81'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('email', sa.String(100), nullable=False),
        sa.Column('password', sa.String(100), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=False),
    )

def downgrade():
    op.drop_table('users')

