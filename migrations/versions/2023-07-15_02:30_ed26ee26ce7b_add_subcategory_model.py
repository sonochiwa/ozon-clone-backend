"""add subcategory model

Revision ID: ed26ee26ce7b
Revises: 84c80f7cdfd7
Create Date: 2023-07-15 02:30:36.649399

"""
from alembic import op
import sqlalchemy as sa

revision = 'ed26ee26ce7b'
down_revision = '84c80f7cdfd7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'subcategories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('category_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ['category_id'], ['categories.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
    )


def downgrade() -> None:
    op.drop_table('subcategories')
