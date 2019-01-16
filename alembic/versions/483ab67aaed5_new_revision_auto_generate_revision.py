"""New revision: Auto generate revision.

Revision ID: 483ab67aaed5
Revises: 
Create Date: 2019-01-15 14:34:08.917332

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '483ab67aaed5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workouts',
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('deleted', sa.Boolean(), nullable=False),
                    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('start_date', sa.DateTime(), nullable=False),
                    sa.Column('end_date', sa.DateTime(), nullable=False),
                    sa.Column('gym_id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('teacher_id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('student_id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('goal_id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('ready', sa.Boolean(), nullable=False),
                    sa.Column('liked', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('workouts_sequences',
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('deleted', sa.Boolean(), nullable=False),
                    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('workout_id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.ForeignKeyConstraint(['workout_id'], ['workouts.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('workouts_sequences_exercises',
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('deleted', sa.Boolean(), nullable=False),
                    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('workout_sequence_id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('gym_exercise_id', postgresql.UUID(as_uuid=True), nullable=False),
                    sa.Column('number', sa.Integer(), nullable=False),
                    sa.Column('repetitions_of', sa.Integer(), nullable=False),
                    sa.Column('repetitions_until', sa.Integer(), nullable=False),
                    sa.Column('cadence', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['workout_sequence_id'], ['workouts_sequences.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('workouts_sequences_exercises')
    op.drop_table('workouts_sequences')
    op.drop_table('workouts')
    # ### end Alembic commands ###