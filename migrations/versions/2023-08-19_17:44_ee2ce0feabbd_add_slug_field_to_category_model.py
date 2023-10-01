"""add slug field to category model

Revision ID: ee2ce0feabbd
Revises: 3b456ee887a7
Create Date: 2023-08-19 17:44:57.354802

"""
from alembic import op
import sqlalchemy as sa


revision = 'ee2ce0feabbd'
down_revision = '3b456ee887a7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('categories', sa.Column('slug', sa.String(length=255), nullable=False))
    op.create_unique_constraint(None, 'categories', ['slug'])


def downgrade() -> None:
    op.drop_constraint(None, 'categories', type_='unique')
    op.drop_column('categories', 'slug')
