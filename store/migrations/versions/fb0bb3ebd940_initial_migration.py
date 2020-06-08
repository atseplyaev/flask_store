"""Initial migration.

Revision ID: fb0bb3ebd940
Revises: 
Create Date: 2020-06-08 09:38:01.850078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fb0bb3ebd940'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('display_size', sa.Float(), nullable=False),
    sa.Column('cpu', sa.String(length=32), nullable=False),
    sa.Column('gpu', sa.String(length=32), nullable=False),
    sa.Column('ram_size', sa.Integer(), nullable=False),
    sa.Column('rom_size', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###