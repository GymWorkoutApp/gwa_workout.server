from typing import Dict
from uuid import uuid4

from gwap_framework.resource.base import BaseResource
from gwap_framework.utils.decorators import validate_schema

from src.cache import cache
from src.database import master_async_session, read_replica_async_session
from src.models import WorkoutModel, WorkoutSequenceModel, WorkoutSequenceExerciseModel
from src.schemas import WorkoutInputSchema, WorkoutOutputSchema, WorkoutSequenceOutputSchema, \
    WorkoutSequenceExerciseOutputSchema


class WorkoutResource(BaseResource):
    cache = cache
    method_decorators = {
        'create': [validate_schema(WorkoutInputSchema)],
        'update': [validate_schema(WorkoutInputSchema)],
    }

    def create(self, request_model: 'WorkoutInputSchema') -> Dict:
        workout = WorkoutModel()
        workout.id = request_model.workout_id or str(uuid4())
        workout.name = request_model.name
        workout.start_date = request_model.start_date
        workout.end_date = request_model.end_date
        workout.gym_id = request_model.gym_id
        workout.teacher_id = request_model.teacher_id
        workout.student_id = request_model.student_id
        workout.goal_id = request_model.goal_id
        workout.ready = request_model.ready
        workout.liked = request_model.liked
        workout.sequences = []

        for sequence_model in request_model.sequences:
            sequence = WorkoutSequenceModel()
            sequence.id = str(uuid4())
            sequence.name = sequence_model.name
            sequence.exercises = []

            for exercise_model in sequence_model.exercises:
                exercise = WorkoutSequenceExerciseModel()
                exercise.id = str(uuid4())
                exercise.gym_exercise_id = exercise_model.gym_exercise_id
                exercise.number = exercise_model.number
                exercise.repetitions_of = exercise_model.repetitions_of
                exercise.repetitions_until = exercise_model.repetitions_until
                exercise.cadence = exercise_model.cadence
                sequence.exercises.append(exercise)

            workout.sequences.append(sequence)

        with master_async_session() as session:
            session.add(workout)
            output = WorkoutOutputSchema()
            output.workout_id = workout.id
            output.name = workout.name
            output.start_date = workout.start_date
            output.end_date = workout.end_date
            output.gym_id = workout.gym_id
            output.teacher_id = workout.teacher_id
            output.student_id = workout.student_id
            output.goal_id = workout.goal_id
            output.ready = workout.ready
            output.liked = workout.liked
            output.sequences = []

            for sequence in workout.sequences:
                output_sequence = WorkoutSequenceOutputSchema()
                output_sequence.workout_sequence_id = sequence.id
                output_sequence.name = sequence.name
                output_sequence.exercises = []

                for exercise in sequence.exercises:
                    output_exercise = WorkoutSequenceExerciseOutputSchema()
                    output_exercise.workout_sequence_exercise_id = exercise.gym_exercise_id
                    output_exercise.gym_exercise_id = exercise.gym_exercise_id
                    output_exercise.number = exercise.number
                    output_exercise.repetitions_of = exercise.repetitions_of
                    output_exercise.repetitions_until = exercise.repetitions_until
                    output_exercise.cadence = exercise.cadence
                    output_exercise.validate()
                    output_sequence.exercises.append(output_exercise)

                output_sequence.validate()
                output.sequences.append(output_sequence)

            output.validate()
            return output.to_primitive()

    def update(self, request_model: 'WorkoutInputSchema', workout_id=None):
        workout = WorkoutModel()
        workout.id = workout_id
        workout.name = request_model.name
        workout.start_date = request_model.start_date
        workout.end_date = request_model.end_date
        workout.gym_id = request_model.gym_id
        workout.teacher_id = request_model.teacher_id
        workout.student_id = request_model.student_id
        workout.goal_id = request_model.goal_id
        workout.ready = request_model.ready
        workout.liked = request_model.liked
        workout.sequences = []

        for sequence_model in request_model.sequences:
            sequence = WorkoutSequenceModel()
            sequence.id = sequence_model.id
            sequence.name = sequence_model.name
            sequence.workout = workout
            sequence.exercises = []

            for exercise_model in sequence_model.exercises:
                exercise = WorkoutSequenceExerciseModel()
                exercise.id = exercise_model.id
                exercise.gym_exercise_id = exercise_model.gym_exercise_id
                exercise.number = exercise_model.number
                exercise.repetitions_of = exercise_model.repetitions_of
                exercise.repetitions_until = exercise_model.repetitions_until
                exercise.cadence = exercise_model.cadence
                exercise.workout_sequence = sequence
                sequence.exercises.append(exercise)

            workout.sequences.append(sequence)
        with master_async_session() as session:
            session.merge(workout)
            output = WorkoutOutputSchema()
            output.workout_id = workout.id
            output.name = workout.name
            output.start_date = workout.start_date
            output.end_date = workout.end_date
            output.gym_id = workout.gym_id
            output.teacher_id = workout.teacher_id
            output.student_id = workout.student_id
            output.goal_id = workout.goal_id
            output.ready = workout.ready
            output.liked = workout.liked
            output.sequences = []

            for sequence in workout.sequences:
                output_sequence = WorkoutSequenceOutputSchema()
                output_sequence.workout_sequence_id = sequence.id
                output_sequence.name = sequence.name
                output_sequence.exercises = []

                for exercise in sequence.exercises:
                    output_exercise = WorkoutSequenceExerciseOutputSchema()
                    output_exercise.workout_sequence_exercise_id = exercise.gym_exercise_id
                    output_exercise.gym_exercise_id = exercise.gym_exercise_id
                    output_exercise.number = exercise.number
                    output_exercise.repetitions_of = exercise.repetitions_of
                    output_exercise.repetitions_until = exercise.repetitions_until
                    output_exercise.cadence = exercise.cadence
                    output_exercise.validate()
                    output_sequence.exercises.append(output_exercise)

                output_sequence.validate()
                output.sequences.append(output_sequence)

            output.validate()
            return output.to_primitive()

    def list(self, args=None, kwargs=None):
        with read_replica_async_session() as session:
            results = []
            for workout in session.query(WorkoutModel).all():
                output = WorkoutOutputSchema()
                output.workout_id = workout.id
                output.name = workout.name
                output.start_date = workout.start_date
                output.end_date = workout.end_date
                output.gym_id = workout.gym_id
                output.teacher_id = workout.teacher_id
                output.student_id = workout.student_id
                output.goal_id = workout.goal_id
                output.ready = workout.ready
                output.liked = workout.liked
                output.sequences = []

                for sequence in workout.sequences:
                    output_sequence = WorkoutSequenceOutputSchema()
                    output_sequence.workout_sequence_id = str(sequence.id)
                    output_sequence.name = sequence.name
                    output_sequence.exercises = []

                    for exercise in sequence.exercises:
                        output_exercise = WorkoutSequenceExerciseOutputSchema()
                        output_exercise.workout_sequence_exercise_id = str(exercise.id)
                        output_exercise.gym_exercise_id = str(exercise.gym_exercise_id)
                        output_exercise.number = exercise.number
                        output_exercise.repetitions_of = exercise.repetitions_of
                        output_exercise.repetitions_until = exercise.repetitions_until
                        output_exercise.cadence = exercise.cadence
                        output_exercise.validate()
                        output_sequence.exercises.append(output_exercise)

                    output_sequence.validate()
                    output.sequences.append(output_sequence)

                output.validate()
                results.append(output.to_primitive())
        return results

    def retrieve(self, workout_id):
        with read_replica_async_session() as session:
            workout = session.query(WorkoutModel).filter_by(id=workout_id).first()
            output = WorkoutOutputSchema()
            output.id = workout.id
            output.name = workout.name
            output.start_date = workout.start_date
            output.end_date = workout.end_date
            output.gym_id = workout.gym_id
            output.teacher_id = workout.teacher_id
            output.student_id = workout.student_id
            output.goal_id = workout.goal_id
            output.ready = workout.ready
            output.liked = workout.liked
            output.sequences = []

            for sequence in workout.sequences:
                output_sequence = WorkoutSequenceOutputSchema()
                output_sequence.workout_sequence_id = sequence.id
                output_sequence.name = sequence.name
                output_sequence.exercises = []

                for exercise in sequence.exercises:
                    output_exercise = WorkoutSequenceExerciseOutputSchema()
                    output_exercise.workout_sequence_exercise_id = exercise.gym_exercise_id
                    output_exercise.gym_exercise_id = exercise.gym_exercise_id
                    output_exercise.number = exercise.number
                    output_exercise.repetitions_of = exercise.repetitions_of
                    output_exercise.repetitions_until = exercise.repetitions_until
                    output_exercise.cadence = exercise.cadence
                    output_exercise.validate()
                    output_sequence.exercises.append(output_exercise)

                output_sequence.validate()
                output.sequences.append(output_sequence)

            output.validate()
            return output.to_primitive()

    def destroy(self, workout_id):
        with master_async_session() as session:
            session.query(WorkoutModel).filter_by(id=workout_id).delete()
            return None


resources_v1 = [
    {'resource': WorkoutResource, 'urls': ['/workouts/<workout_id>'], 'endpoint': 'Workouts WorkoutId',
     'methods': ['GET', 'PUT', 'PATCH', 'DELETE']},
    {'resource': WorkoutResource, 'urls': ['/workouts'], 'endpoint': 'Workouts',
     'methods': ['POST', 'GET']},
]
