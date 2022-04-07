"""add foreign key to posts table

Revision ID: 85c13f797a06
Revises: d6f2119563a6
Create Date: 2022-04-07 14:43:03.005692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85c13f797a06'
down_revision = 'd6f2119563a6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), sa.ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
        'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
