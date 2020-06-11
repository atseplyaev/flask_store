"""add product image url

Revision ID: 98c4aaab925a
Revises: 64315d84fb76
Create Date: 2020-06-11 08:16:03.784613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98c4aaab925a'
down_revision = '64315d84fb76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('image_url', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'image_url')
    # ### end Alembic commands ###