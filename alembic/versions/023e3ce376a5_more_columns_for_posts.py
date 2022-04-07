"""more columns for posts

Revision ID: 023e3ce376a5
Revises: 85c13f797a06
Create Date: 2022-04-07 14:50:15.497846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '023e3ce376a5'
down_revision = '85c13f797a06'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
        nullable=False, server_default="TRUE"))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
