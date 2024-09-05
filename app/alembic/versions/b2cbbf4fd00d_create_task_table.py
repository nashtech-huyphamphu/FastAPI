"""Create task table

Revision ID: b2cbbf4fd00d
Revises: 9b12eb55a249
Create Date: 2024-09-05 11:39:24.593208

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid


# revision identifiers, used by Alembic.
revision: str = 'b2cbbf4fd00d'
down_revision: Union[str, None] = '9b12eb55a249'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'task',
        sa.Column('id', sa.UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4),
        sa.Column('summary', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=True),
        sa.Column('status', sa.String, nullable=False),
        sa.Column('priority', sa.String, nullable=False),
        sa.Column('user_id', sa.UUID, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=True),
        sa.Column('updated_at', sa.DateTime, nullable=True)
    )
    op.create_foreign_key('fk_task_user', 'task', 'user', ['user_id'], ['id'])

def downgrade() -> None:
    op.drop_table('task')