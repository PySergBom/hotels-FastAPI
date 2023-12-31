"""test migration

Revision ID: 6bc7b86bce8c
Revises: 58336ecca3ec
Create Date: 2023-09-06 23:51:55.721945

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6bc7b86bce8c'
down_revision: Union[str, None] = '58336ecca3ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('image_idd', sa.Integer(), nullable=True))
    op.drop_column('hotels', 'image_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('image_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('hotels', 'image_idd')
    # ### end Alembic commands ###
