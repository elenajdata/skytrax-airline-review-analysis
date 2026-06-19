"""create newzelanairlinereviews with unique id

Revision ID: 2398c70fadec
Revises: 
Create Date: 2026-03-13 20:37:26.179379

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2398c70fadec'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "newzealandairlinereviews",
        sa.Column("review_id", sa.Text, primary_key=True),
        sa.Column("author_name", sa.Text),
        sa.Column("date_of_review", sa.Text),
        sa.Column("title", sa.Text),
        sa.Column("review_body",sa.Text),
        sa.Column("trip_verified", sa.Boolean),
        sa.Column("rating", sa.Integer),
        sa.Column("route", sa.Text),
        sa.Column("date_flown", sa.Text),
        sa.Column("trip_type", sa.Text),
        sa.Column("page_number", sa.Integer)
    )


def downgrade() -> None:
    op.drop_table("newzelandairlinereviews")
