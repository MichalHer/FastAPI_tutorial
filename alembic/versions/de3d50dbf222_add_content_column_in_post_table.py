"""add content column in post table

Revision ID: de3d50dbf222
Revises: 0e053daab9e1
Create Date: 2022-03-07 22:25:57.209219

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de3d50dbf222'
down_revision = '0e053daab9e1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
