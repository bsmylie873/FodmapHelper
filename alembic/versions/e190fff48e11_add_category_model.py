"""Add category model

Revision ID: e190fff48e11
Revises: 
Create Date: 2024-02-19 12:34:56.789012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e190fff48e11'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Drop existing tables
    op.drop_table('foods')
    
    # Create categories table
    op.create_table('categories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_categories_id'), 'categories', ['id'], unique=False)
    op.create_index(op.f('ix_categories_name'), 'categories', ['name'], unique=True)

    # Create foods table with new schema
    op.create_table('foods',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('fodmap_level', sa.Enum('low', 'medium', 'high', name='fodmaplevel'), nullable=False),
        sa.Column('serving_size', sa.String(), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('category_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_foods_id'), 'foods', ['id'], unique=False)
    op.create_index(op.f('ix_foods_name'), 'foods', ['name'], unique=False)


def downgrade() -> None:
    # Drop new tables
    op.drop_index(op.f('ix_foods_name'), table_name='foods')
    op.drop_index(op.f('ix_foods_id'), table_name='foods')
    op.drop_table('foods')
    op.drop_index(op.f('ix_categories_name'), table_name='categories')
    op.drop_index(op.f('ix_categories_id'), table_name='categories')
    op.drop_table('categories')
