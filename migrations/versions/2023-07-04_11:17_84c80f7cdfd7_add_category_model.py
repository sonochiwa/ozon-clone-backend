"""add category model

Revision ID: 84c80f7cdfd7
Revises: ac335de4a67e
Create Date: 2023-07-04 11:17:56.262313

"""
import sqlalchemy as sa
from alembic import op

revision = '84c80f7cdfd7'
down_revision = 'ac335de4a67e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )


def downgrade() -> None:
    op.drop_table('categories')
