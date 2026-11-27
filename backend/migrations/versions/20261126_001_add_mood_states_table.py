"""Add mood states table

Revision ID: 20261126_001
Revises: 8884d2169438
Create Date: 2026-11-26 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '20261126_001'
down_revision = '8884d2169438'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'mood_states',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('conversation_id', sa.Integer(), nullable=False),
        sa.Column('current_mood', sa.String(length=50), nullable=False, server_default='calm'),
        sa.Column('intensity', sa.Integer(), nullable=False, server_default='50'),
        sa.Column('baseline_intensity', sa.Integer(), nullable=False, server_default='50'),
        sa.Column('enable_mood_system', sa.Boolean(), nullable=False, server_default=True),
        sa.Column('cooldown_until', sa.DateTime(), nullable=True),
        sa.Column('last_mood_change', sa.DateTime(), server_default=sa.text('now()'), onupdate=sa.text('now()')),
        sa.Column('last_updated', sa.DateTime(), server_default=sa.text('now()'), onupdate=sa.text('now()')),
        sa.ForeignKeyConstraint(['conversation_id'], ['conversations.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('conversation_id')
    )

    op.create_table(
        'mood_history',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('mood_state_id', sa.Integer(), nullable=False),
        sa.Column('mood', sa.String(length=50), nullable=False),
        sa.Column('intensity', sa.Integer(), nullable=False),
        sa.Column('trigger_message', sa.Text(), nullable=True),
        sa.Column('reason', sa.Text(), nullable=True),
        sa.Column('timestamp', sa.DateTime(), server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['mood_state_id'], ['mood_states.id'], ),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('mood_history')
    op.drop_table('mood_states')