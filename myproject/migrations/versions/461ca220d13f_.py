"""empty message

Revision ID: 461ca220d13f
Revises: 3b06dc7663d5
Create Date: 2023-04-15 17:13:03.795611

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '461ca220d13f'
down_revision = '3b06dc7663d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('views', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.drop_column('views')

    # ### end Alembic commands ###