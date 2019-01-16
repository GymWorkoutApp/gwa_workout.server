from datetime import datetime
from uuid import uuid4

from gwap_framework.models.base import BaseModel
from pytz import timezone
from sqlalchemy import Column, DateTime, String, Boolean, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class WorkoutModel(BaseModel):
    __tablename__ = 'workouts'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(100), nullable=False)
    start_date = Column(DateTime, nullable=False, default=datetime.now(tz=timezone('America/Sao_Paulo')))
    end_date = Column(DateTime, nullable=False, default=datetime.now(tz=timezone('America/Sao_Paulo')))
    gym_id = Column(UUID(as_uuid=True), nullable=False)
    teacher_id = Column(UUID(as_uuid=True), nullable=False)
    student_id = Column(UUID(as_uuid=True), nullable=False)
    goal_id = Column(UUID(as_uuid=True), nullable=False)
    ready = Column(Boolean, default=False, nullable=False)
    liked = Column(Boolean, default=False, nullable=False)
    sequences = relationship("WorkoutSequenceModel", backref="workouts")


class WorkoutSequenceModel(BaseModel):
    __tablename__ = 'workouts_sequences'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    workout_id = Column(UUID(as_uuid=True), ForeignKey('workouts.id'), nullable=False)
    workout = relationship("WorkoutModel", back_populates="sequences")
    name = Column(String(100), nullable=False)
    exercises = relationship("WorkoutSequenceExerciseModel", backref="workouts_sequences")


class WorkoutSequenceExerciseModel(BaseModel):
    __tablename__ = 'workouts_sequences_exercises'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    workout_sequence_id = Column(UUID(as_uuid=True), ForeignKey('workouts_sequences.id'), nullable=False)
    workout_sequence = relationship("WorkoutSequenceModel", back_populates="exercises")
    gym_exercise_id = Column(UUID(as_uuid=True), nullable=False)
    number = Column(Integer, nullable=False)
    repetitions_of = Column(Integer, nullable=False)
    repetitions_until = Column(Integer, nullable=False)
    cadence = Column(Integer, nullable=False)


