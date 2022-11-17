"""Se agrega marca

Revision ID: 22d80b19dde4
Revises: 0af9e501f65c
Create Date: 2022-11-17 10:10:25.852796

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '22d80b19dde4'
down_revision = '0af9e501f65c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('city_data', sa.Integer(), nullable=True),
    sa.Column('brand', sa.String(length=45), nullable=True),
    sa.Column('line', sa.String(length=45), nullable=True),
    sa.Column('type_fuel', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['brand'], ['brands.id_runt'], ),
    sa.ForeignKeyConstraint(['city_data'], ['cities.cod_name'], ),
    sa.ForeignKeyConstraint(['line'], ['lines.name'], ),
    sa.ForeignKeyConstraint(['type_fuel'], ['type_fuel.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vehicle_id'), 'vehicle', ['id'], unique=False)
    op.create_index(op.f('ix_vehicle_name'), 'vehicle', ['name'], unique=True)
    op.drop_constraint('lines_ibfk_1', 'lines', type_='foreignkey')
    op.drop_column('lines', 'id_brand')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lines', sa.Column('id_brand', mysql.VARCHAR(length=45), nullable=True))
    op.create_foreign_key('lines_ibfk_1', 'lines', 'brands', ['id_brand'], ['id_runt'])
    op.drop_index(op.f('ix_vehicle_name'), table_name='vehicle')
    op.drop_index(op.f('ix_vehicle_id'), table_name='vehicle')
    op.drop_table('vehicle')
    # ### end Alembic commands ###
