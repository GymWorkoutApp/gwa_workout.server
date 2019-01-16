from gwap_framework.schemas.base import BaseSchema
from schematics.types import StringType, DateTimeType, BooleanType, ListType, ModelType, NumberType, IntType


class WorkoutSequenceExerciseInputSchema(BaseSchema):
    workout_sequence_exercise_id = StringType(required=False, serialized_name='workoutSequenceExerciseId')
    gym_exercise_id = StringType(required=True, serialized_name='gymExerciseId')
    number = IntType(required=True)
    repetitions_of = IntType(required=True, serialized_name='repetitionsOf')
    repetitions_until = IntType(required=True, serialized_name='repetitionsUntil')
    cadence = IntType(required=False)


class WorkoutSequenceInputSchema(BaseSchema):
    workout_sequence_id = StringType(required=False, serialized_name='workoutSequenceId')
    name = StringType(required=True, max_length=100, min_length=1)
    exercises = ListType(field=ModelType(model_spec=WorkoutSequenceExerciseInputSchema, required=False), required=False)


class WorkoutInputSchema(BaseSchema):
    workout_id = StringType(required=False, serialized_name='workoutId')
    name = StringType(required=True, max_length=100, min_length=1)
    start_date = DateTimeType(required=False, serialized_name='startDate')
    end_date = DateTimeType(required=False, serialized_name='endDate')
    gym_id = StringType(required=True, serialized_name='gymId')
    teacher_id = StringType(required=True, serialized_name='teacherId')
    student_id = StringType(required=True, serialized_name='studentId')
    goal_id = StringType(required=True, serialized_name='goalId')
    ready = BooleanType(default=False, required=False)
    liked = BooleanType(default=False, required=False)
    sequences = ListType(field=ModelType(model_spec=WorkoutSequenceInputSchema, required=False), required=False)


class WorkoutSequenceExerciseOutputSchema(BaseSchema):
    workout_sequence_exercise_id = StringType(required=False, serialized_name='workoutSequenceExerciseId')
    gym_exercise_id = StringType(required=True, serialized_name='gymExerciseId')
    number = IntType(required=True)
    repetitions_of = IntType(required=True)
    repetitions_until = IntType(required=True)
    cadence = IntType(required=False)


class WorkoutSequenceOutputSchema(BaseSchema):
    workout_sequence_id = StringType(required=False, serialized_name='workoutSequenceId')
    name = StringType(required=True, max_length=100, min_length=1)
    exercises = ListType(field=ModelType(model_spec=WorkoutSequenceExerciseOutputSchema, required=False),
                         required=False)


class WorkoutOutputSchema(BaseSchema):
    workout_id = StringType(required=False, serialized_name='workoutId')
    name = StringType(required=True, max_length=100, min_length=1)
    start_date = DateTimeType(required=False, serialized_name='startDate')
    end_date = DateTimeType(required=False, serialized_name='endDate')
    gym_id = StringType(required=True, serialized_name='gymId')
    teacher_id = StringType(required=True, serialized_name='teacherId')
    student_id = StringType(required=True, serialized_name='studentId')
    goal_id = StringType(required=True, serialized_name='goalId')
    ready = BooleanType(default=False, required=False)
    liked = BooleanType(default=False, required=False)
    sequences = ListType(field=ModelType(model_spec=WorkoutSequenceOutputSchema, required=False), required=False)
