"""Небольшие изменения в Reservations

Revision ID: 6c46df6038b3
Revises: 6b3584f0e2e6
Create Date: 2021-11-18 22:27:35.001413

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c46df6038b3'
down_revision = '6b3584f0e2e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservations', sa.Column('is_read', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservations', 'is_read')
    # ### end Alembic commands ###
