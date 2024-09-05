"""Create user table

Revision ID: 9b12eb55a249
Revises: 0626584ff456
Create Date: 2024-09-05 07:14:59.949104

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision: str = '9b12eb55a249'
down_revision: Union[str, None] = '0626584ff456'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user',
        sa.Column('id', sa.UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4),
        sa.Column('email', sa.String, nullable=False, unique=True),
        sa.Column('username', sa.String, nullable=False, unique=True),
        sa.Column('first_name', sa.String, nullable=False),
        sa.Column('last_name', sa.String, nullable=False),
        sa.Column('hashed_password', sa.String, nullable=False),
        sa.Column('is_active', sa.Boolean, nullable=False, default=True),
        sa.Column('is_admin', sa.Boolean, nullable=False, default=False),
        sa.Column('created_at', sa.DateTime, nullable=True),
        sa.Column('updated_at', sa.DateTime, nullable=True)
    )

def downgrade() -> None:
    op.drop_table('user')
