"""empty message

Revision ID: e9c0c8dd8b61
Revises: 
Create Date: 2018-06-11 13:19:44.538784

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9c0c8dd8b61'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('axf_foodtypes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('typeid', sa.Integer(), nullable=True),
    sa.Column('typename', sa.String(length=16), nullable=True),
    sa.Column('childtypenames', sa.String(length=200), nullable=True),
    sa.Column('typesort', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('axf_goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('productid', sa.Integer(), nullable=True),
    sa.Column('productimg', sa.String(length=200), nullable=True),
    sa.Column('productname', sa.String(length=128), nullable=True),
    sa.Column('productlongname', sa.String(length=128), nullable=True),
    sa.Column('isxf', sa.Boolean(), nullable=True),
    sa.Column('pmdesc', sa.Boolean(), nullable=True),
    sa.Column('specifics', sa.String(length=16), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('marketprice', sa.Float(), nullable=True),
    sa.Column('categoryid', sa.Float(), nullable=True),
    sa.Column('childcid', sa.Integer(), nullable=True),
    sa.Column('childcidname', sa.String(length=128), nullable=True),
    sa.Column('dealerid', sa.Integer(), nullable=True),
    sa.Column('storenums', sa.Integer(), nullable=True),
    sa.Column('productnum', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('axf_mainshow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('trackid', sa.Integer(), nullable=True),
    sa.Column('categoryid', sa.Integer(), nullable=True),
    sa.Column('brandname', sa.String(length=32), nullable=True),
    sa.Column('img1', sa.String(length=200), nullable=True),
    sa.Column('childcid1', sa.Integer(), nullable=True),
    sa.Column('productid1', sa.Integer(), nullable=True),
    sa.Column('longname1', sa.String(length=200), nullable=True),
    sa.Column('price1', sa.Float(), nullable=True),
    sa.Column('marketprice1', sa.Float(), nullable=True),
    sa.Column('img2', sa.String(length=200), nullable=True),
    sa.Column('childcid2', sa.Integer(), nullable=True),
    sa.Column('productid2', sa.Integer(), nullable=True),
    sa.Column('longname2', sa.String(length=200), nullable=True),
    sa.Column('price2', sa.Float(), nullable=True),
    sa.Column('marketprice2', sa.Float(), nullable=True),
    sa.Column('img3', sa.String(length=200), nullable=True),
    sa.Column('childcid3', sa.Integer(), nullable=True),
    sa.Column('productid3', sa.Integer(), nullable=True),
    sa.Column('longname3', sa.String(length=200), nullable=True),
    sa.Column('price3', sa.Float(), nullable=True),
    sa.Column('marketprice3', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('axf_mustbuy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('trackid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('axf_nav',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('trackid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('axf_shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('trackid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('axf_wheel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(length=200), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.Column('trackid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('axf_wheel')
    op.drop_table('axf_shop')
    op.drop_table('axf_nav')
    op.drop_table('axf_mustbuy')
    op.drop_table('axf_mainshow')
    op.drop_table('axf_goods')
    op.drop_table('axf_foodtypes')
    # ### end Alembic commands ###
