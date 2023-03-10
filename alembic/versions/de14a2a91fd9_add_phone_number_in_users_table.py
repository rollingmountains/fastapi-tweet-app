"""add phone number in users table

Revision ID: de14a2a91fd9
Revises: 8b6df546ac39
Create Date: 2022-12-26 10:51:57.359500

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de14a2a91fd9'
down_revision = '8b6df546ac39'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.String(), nullable=False))
    op.create_unique_constraint(None, 'users', ['phone_number'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###
