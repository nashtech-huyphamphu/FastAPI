"""Create company table

Revision ID: 0626584ff456
Revises: 
Create Date: 2024-09-05 01:11:37.843889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from enum import Enum
import uuid


# revision identifiers, used by Alembic.
revision: str = '0626584ff456'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

class CompanyMode(Enum):
    ONLINE = 'online'
    OFFLINE = 'offline'
    HYBRID = 'hybrid'

# Upgrade script
def upgrade() -> None:
    op.create_table(
        'company',
        sa.Column('id', sa.UUID(as_uuid=True), nullable=False, primary_key=True, default=uuid.uuid4),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('description', sa.String, nullable=True),
        sa.Column('mode', sa.Enum(CompanyMode), nullable=False, default=CompanyMode.ONLINE),
        sa.Column('rating', sa.Float, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=True),
        sa.Column('updated_at', sa.DateTime, nullable=True)
    )


# Downgrade script
def downgrade() -> None:
    op.drop_table('company')
    op.execute("DROP TYPE companymode;")
