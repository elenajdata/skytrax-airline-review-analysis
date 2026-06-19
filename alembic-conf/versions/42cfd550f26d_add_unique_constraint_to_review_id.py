"""add unique constraint to review_id

Revision ID: 42cfd550f26d
Revises: 2398c70fadec
Create Date: 2026-03-18 19:07:33.411276

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42cfd550f26d'
down_revision: Union[str, Sequence[str], None] = '2398c70fadec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Use batch mode to safely alter table in SQLite
    with op.batch_alter_table("newzealandairlinereviews", recreate="always") as batch_op:
        batch_op.create_unique_constraint("uq_review_id", ["review_id"])


def downgrade():
    with op.batch_alter_table("newzealandairlinereviews", recreate="always") as batch_op:
        batch_op.drop_constraint("uq_review_id", type_="unique")
