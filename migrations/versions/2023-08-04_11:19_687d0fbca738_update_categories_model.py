"""update categories model

Revision ID: 687d0fbca738
Revises: 8ede5b8c751f
Create Date: 2023-08-04 11:19:11.851781

"""
from alembic import op
import sqlalchemy as sa


revision = '687d0fbca738'
down_revision = '8ede5b8c751f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('categories', sa.Column('image_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'categories', 'images', ['image_id'], ['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint(None, 'categories', type_='foreignkey')
    op.drop_column('categories', 'image_id')
