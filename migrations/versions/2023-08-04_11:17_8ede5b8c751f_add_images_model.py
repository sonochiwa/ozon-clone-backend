"""add images model

Revision ID: 8ede5b8c751f
Revises: c889156bd51e
Create Date: 2023-08-04 11:17:13.004659

"""
import sqlalchemy as sa
from alembic import op

revision = '8ede5b8c751f'
down_revision = 'c889156bd51e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'images',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('path', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('images')
