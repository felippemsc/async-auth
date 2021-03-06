"""empty message

Revision ID: c056ef9b223e
Revises: 
Create Date: 2019-12-26 22:44:44.879309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c056ef9b223e"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("key", sa.String(length=8), nullable=False),
        sa.Column("email", sa.String(length=100), nullable=False),
        sa.Column("password", sa.String(length=200), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        schema="auth",
    )
    op.create_index(
        op.f("ix_auth_user_key"), "user", ["key"], unique=True, schema="auth"
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_auth_user_key"), table_name="user", schema="auth")
    op.drop_table("user", schema="auth")
    # ### end Alembic commands ###
