"""add foreign key in posts table

Revision ID: 3999c1658d2a
Revises: f394c5b85fe6
Create Date: 2022-12-26 09:57:10.780629

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3999c1658d2a'
down_revision = 'f394c5b85fe6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'],
    remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
