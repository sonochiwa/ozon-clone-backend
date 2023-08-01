"""add products model

Revision ID: c889156bd51e
Revises: ed26ee26ce7b
Create Date: 2023-08-01 16:22:57.579057

"""
import sqlalchemy as sa
from alembic import op

revision = 'c889156bd51e'
down_revision = 'ed26ee26ce7b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'products',
        sa.Column('id', sa.Uuid(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('price', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column('count', sa.Integer(), nullable=False),
        sa.Column('discount', sa.Integer(), nullable=False),
        sa.Column('views', sa.Integer(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('description', sa.String(length=1000), nullable=True),
        sa.Column('subcategory_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['subcategory_id'], ['subcategories.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('products')
