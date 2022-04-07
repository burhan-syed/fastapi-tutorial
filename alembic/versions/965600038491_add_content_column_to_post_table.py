"""add content column to post table

Revision ID: 965600038491
Revises: 59b87f4a8039
Create Date: 2022-04-07 14:23:15.455156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '965600038491'
down_revision = '59b87f4a8039'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
