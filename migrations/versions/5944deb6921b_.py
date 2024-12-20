"""empty message

Revision ID: 5944deb6921b
Revises: 
Create Date: 2024-11-28 12:41:08.243871

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5944deb6921b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('option_1', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('option_2', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('option_3', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('option_4', sa.String(length=255), nullable=False))
        batch_op.alter_column('correct_option',
               existing_type=sa.VARCHAR(length=1),
               type_=sa.Integer(),
               existing_nullable=False)
        batch_op.drop_column('difficulty')
        batch_op.drop_column('option_c')
        batch_op.drop_column('option_b')
        batch_op.drop_column('category')
        batch_op.drop_column('option_d')
        batch_op.drop_column('option_a')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('question', schema=None) as batch_op:
        batch_op.add_column(sa.Column('option_a', sa.VARCHAR(length=200), nullable=False))
        batch_op.add_column(sa.Column('option_d', sa.VARCHAR(length=200), nullable=False))
        batch_op.add_column(sa.Column('category', sa.VARCHAR(length=100), nullable=False))
        batch_op.add_column(sa.Column('option_b', sa.VARCHAR(length=200), nullable=False))
        batch_op.add_column(sa.Column('option_c', sa.VARCHAR(length=200), nullable=False))
        batch_op.add_column(sa.Column('difficulty', sa.VARCHAR(length=50), nullable=False))
        batch_op.alter_column('correct_option',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(length=1),
               existing_nullable=False)
        batch_op.drop_column('option_4')
        batch_op.drop_column('option_3')
        batch_op.drop_column('option_2')
        batch_op.drop_column('option_1')

    # ### end Alembic commands ###
