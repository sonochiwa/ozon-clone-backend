"""set subcategory to category fk prop ondelete as cascade

Revision ID: 3b456ee887a7
Revises: 687d0fbca738
Create Date: 2023-08-19 17:44:04.940527

"""
from alembic import op


revision = '3b456ee887a7'
down_revision = '687d0fbca738'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.drop_constraint('subcategories_category_id_fkey', 'subcategories', type_='foreignkey')
    op.create_foreign_key(None, 'subcategories', 'categories', ['category_id'], ['id'], ondelete='CASCADE')


def downgrade() -> None:
    op.drop_constraint(None, 'subcategories', type_='foreignkey')
    op.create_foreign_key('subcategories_category_id_fkey', 'subcategories', 'categories', ['category_id'], ['id'])
